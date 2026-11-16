"""Start of the RAGbase Shield engine in the Windows plugin for the Claude desktop app (standard library only).

The Claude app copies the plugin into a deep folder (about 180 to 230 characters before ``engine\\``), and Windows,
by default, cannot open a file whose full path has 260 characters or more. So the plugin ships its Python packages
in ONE archive, ``engine\\pkgs.zip``, and this module unpacks it once into a short folder of the computer:

    <Local AppData>\\RAGbase Shield\\engine\\<version>-<id>

``<id>`` is the first 12 hex characters of the SHA-256 of ``pkgs.zip``, computed at build time and stored in
``engine\\pkgs.id`` (the archive is never hashed at start). The plugin command is

    ${CLAUDE_PLUGIN_ROOT}/engine/shield.exe -I -B -X utf8 -m shield_boot

and this module, in this order: (a) puts SYSTEMROOT back when the app gives a small environment (Winsock, so
asyncio, needs it); (b) finds the cache folder from the system (SHGetKnownFolderPath, never an environment
variable); (c) unpacks the archive when needed: each file under a temporary name, then ``os.replace``; a file that
is already there with the right size is kept, so a start that was killed goes on at the next start; the
"complete" mark is written last and, once there, the archive is not read again; a member name that is absolute or
holds ".." stops the start; (d) adds the folder to ``sys.path`` with the rules of the ``site`` module (so the
pywin32 ``.pth`` lines and ``pywin32_bootstrap`` run) and runs ``ragbase_shield.claude_tab`` as ``-m`` would.

It writes nothing on standard output (the MCP channel) and nothing inside the plugin folder. On failure it writes
one short French sentence on standard error and stops with code 1. The cache can be deleted at any time: the next
start builds it again. The vault (names and codes) is NOT here: see ``ragbase_shield.claude_tab.plugin_home``.
"""
import os
import sys

VERSION = "0.4.2"
APP_DIR_NAME = "RAGbase Shield"
ARCHIVE = "pkgs.zip"
ID_FILE = "pkgs.id"
MARKER = "complete.txt"
MODULE = "ragbase_shield.claude_tab"
FOLDERID_LOCAL_APP_DATA = "{F1B32785-6FBA-4FCF-9D55-7B8E7F157091}"

MSG_REINSTALL = "RAGbase Shield ne peut pas démarrer : réinstallez le plugin."
MSG_UNPACK = ("RAGbase Shield ne peut pas préparer ses fichiers sur cet ordinateur : vérifiez la place libre "
              "sur le disque, puis redémarrez Claude.")


class BootError(Exception):
    """A start failure. ``message`` is the French sentence for standard error."""

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


# ------------------------------------------------------------------------------------------- (a) SYSTEMROOT

def _system_windows_dir() -> str:  # pragma: no cover - Windows
    try:
        import ctypes

        buf = ctypes.create_unicode_buffer(260)
        if ctypes.windll.kernel32.GetSystemWindowsDirectoryW(buf, 260):
            return buf.value
    except Exception:  # noqa: BLE001
        pass
    return ""


def fill_systemroot(environ=None, windows=None, windows_dir=None) -> bool:
    """Windows: SYSTEMROOT from the system when the app did not pass it. Runs before anything imports asyncio."""
    environ = os.environ if environ is None else environ
    windows = (os.name == "nt") if windows is None else windows
    if not windows or environ.get("SYSTEMROOT"):
        return False
    value = (windows_dir or _system_windows_dir)()
    if not value:
        return False
    environ["SYSTEMROOT"] = value
    return True


# ------------------------------------------------------------------------------------------- (b) cache folder

def known_folder(guid: str) -> str:  # pragma: no cover - Windows
    """A Windows known folder from the shell (never from an environment variable). Empty text on failure."""
    try:
        import ctypes
        from ctypes import wintypes

        class GUID(ctypes.Structure):
            _fields_ = [("Data1", wintypes.DWORD), ("Data2", wintypes.WORD), ("Data3", wintypes.WORD),
                        ("Data4", ctypes.c_ubyte * 8)]

        g = GUID()
        ctypes.oledll.ole32.CLSIDFromString(ctypes.c_wchar_p(guid), ctypes.byref(g))
        out = ctypes.c_wchar_p()
        ctypes.oledll.shell32.SHGetKnownFolderPath(ctypes.byref(g), 0, None, ctypes.byref(out))
        try:
            return out.value or ""
        finally:
            ctypes.windll.ole32.CoTaskMemFree(out)
    except Exception:  # noqa: BLE001
        return ""


def local_app_data() -> str:
    """<Local AppData> of the user, from the system. Tests replace this function."""
    path = known_folder(FOLDERID_LOCAL_APP_DATA) if os.name == "nt" else ""
    if not path:
        raise BootError(MSG_UNPACK)
    return path


def engine_dir() -> str:
    """The plugin's ``engine`` folder: where this module, ``pkgs.zip`` and ``pkgs.id`` are."""
    return os.path.dirname(os.path.abspath(__file__))


def archive_id(engine: str) -> str:
    """The 12 hex characters written at build time in ``pkgs.id`` (the archive itself is not read)."""
    try:
        with open(os.path.join(engine, ID_FILE), encoding="ascii") as f:
            ident = f.read().strip()
    except (OSError, ValueError):
        raise BootError(MSG_REINSTALL) from None
    if len(ident) != 12 or any(c not in "0123456789abcdef" for c in ident):
        raise BootError(MSG_REINSTALL)
    return ident


def cache_dir(engine: str) -> str:
    return os.path.join(local_app_data(), APP_DIR_NAME, "engine", f"{VERSION}-{archive_id(engine)}")


# ------------------------------------------------------------------------------------------- (c) unpack

def member_parts(name: str) -> list:
    """The path parts of an archive member. Refuses an absolute name, a drive or stream (":") and "..".
    Empty parts and "." are dropped."""
    if not name or name[0] in "/\\" or ":" in name or "\x00" in name:
        raise BootError(MSG_REINSTALL)
    parts = [p for p in name.replace("\\", "/").split("/") if p not in ("", ".")]
    if not parts or any(p == ".." for p in parts):
        raise BootError(MSG_REINSTALL)
    return parts


def _size(path: str) -> int:
    try:
        return os.stat(path).st_size
    except OSError:
        return -1


def _replace(tmp: str, target: str, size: int) -> None:
    """``os.replace`` with patience: on Windows a file that another start already put there and loaded (a .pyd)
    cannot be replaced. That file is complete (only complete files get their final name): keep it."""
    import time

    for attempt in range(40):
        try:
            os.replace(tmp, target)
            return
        except OSError:
            if _size(target) == size:
                try:
                    os.remove(tmp)
                except OSError:
                    pass
                return
            time.sleep(0.05)
    os.replace(tmp, target)  # last try: its error is the real one


def is_complete(dest: str) -> bool:
    return os.path.isfile(os.path.join(dest, MARKER))


def unpack(archive: str, dest: str) -> int:
    """Unpack ``archive`` into ``dest`` unless the complete mark is there. Returns the number of files written now
    (0 when the mark was there: then the archive is not opened). Safe against a kill at any moment and against two
    starts at the same time."""
    if is_complete(dest):
        return 0
    import shutil
    import zipfile

    try:
        z = zipfile.ZipFile(archive)
    except (OSError, zipfile.BadZipFile):
        raise BootError(MSG_REINSTALL) from None
    tmp_name = "~%x.tmp" % os.getpid()  # short: the deepest folders are near the path limit
    written = 0
    with z:
        infos = z.infolist()
        plan = [(info, member_parts(info.filename)) for info in infos]  # every name is checked before any write
        try:
            os.makedirs(dest, exist_ok=True)
            for info, parts in plan:
                target = os.path.join(dest, *parts)
                if info.is_dir():
                    os.makedirs(target, exist_ok=True)
                    continue
                if _size(target) == info.file_size:
                    continue  # complete already (an earlier start, or another start right now)
                folder = os.path.dirname(target)
                os.makedirs(folder, exist_ok=True)
                tmp = os.path.join(folder, tmp_name)
                try:
                    with z.open(info) as src, open(tmp, "wb") as out:
                        shutil.copyfileobj(src, out, 1 << 20)
                    _replace(tmp, target, info.file_size)
                finally:
                    if os.path.exists(tmp):
                        try:
                            os.remove(tmp)
                        except OSError:
                            pass
                written += 1
        except (OSError, zipfile.BadZipFile, EOFError) as exc:
            raise BootError(MSG_UNPACK if isinstance(exc, OSError) else MSG_REINSTALL) from None
    # the mark goes last: before it, every start checks the files again
    mark_tmp = os.path.join(dest, tmp_name)
    mark = f"RAGbase Shield {VERSION}: {len(infos)} entries\n".encode("ascii")
    try:
        with open(mark_tmp, "wb") as f:
            f.write(mark)
        _replace(mark_tmp, os.path.join(dest, MARKER), len(mark))
    except OSError:
        if not is_complete(dest):
            raise BootError(MSG_UNPACK) from None
    return written


# ------------------------------------------------------------------------------------------- (d) run

def add_to_path(dest: str) -> None:
    """The cache folder on sys.path with the site rules: its ``.pth`` files run (pywin32: win32, win32\\lib,
    ``import pywin32_bootstrap``), exactly as for a site-packages folder."""
    import site

    site.addsitedir(dest)


def run() -> None:
    import runpy

    runpy.run_module(MODULE, run_name="__main__", alter_sys=True)


def prepare() -> str:
    """Steps (a) to (d). Returns the cache folder."""
    fill_systemroot()
    engine = engine_dir()
    dest = cache_dir(engine)
    unpack(os.path.join(engine, ARCHIVE), dest)
    add_to_path(dest)
    import importlib.util

    try:
        found = importlib.util.find_spec(MODULE) is not None
    except ImportError:
        found = False
    if not found:
        raise BootError(MSG_REINSTALL)
    return dest


def fail(message: str) -> None:
    try:
        if sys.stderr is not None:
            sys.stderr.write(message + "\n")
            sys.stderr.flush()
    except Exception:  # noqa: BLE001
        pass
    raise SystemExit(1)


def main() -> None:
    try:
        prepare()
    except BootError as exc:
        fail(exc.message)
    except Exception:  # noqa: BLE001 - never a traceback with a path on the protocol side
        fail(MSG_REINSTALL)
    run()


if __name__ == "__main__":
    main()
