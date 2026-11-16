# RAGbase Shield pour Claude (Windows)

**Claude travaille sur vos dossiers clients sans voir les vrais noms.**

[Français](#français) · [English](#english) · [Technical details](#technical-details)

## Français

### Ce que fait Shield

- Sur votre PC, Shield remplace les noms et les autres données privées de vos documents par des codes, comme `PERSONNE_A` ou `SOCIETE_B`.
- Claude lit et rédige avec ces codes. Il ne voit pas les vrais noms.
- Le document final revient sur votre PC, avec les vrais noms.

Gratuit et open source. Rien d'autre à installer.

### Ajouter Shield à Claude

Il vous faut l'application Claude pour Windows.

- **Le plus simple :** sur [shield.ragbase.ai](https://shield.ragbase.ai), cliquez sur le bouton pour Windows. L'application Claude s'ouvre : cliquez sur **Synchro**, puis sur **Ajouter** à droite de « RAGbase Shield (Windows) ». Si votre Claude est en anglais, ces boutons s'appellent **Sync** et **Add**.
- **Autre façon :** dans l'application Claude, ouvrez **Personnalisation > Plug-ins > Ajouter > Ajouter une marketplace > Ajouter depuis un dépôt**. Écrivez `ragbase/ragbase-shield-windows` et cliquez sur **Synchro**. Dans l'onglet **Découvrir**, cliquez ensuite sur **Ajouter** à droite de « RAGbase Shield (Windows) ». Si votre Claude est en anglais : **Customize > Plugins > Add > Add marketplace > Add from a repository**, puis **Sync**, **Discover** et **Add**.

### Utiliser Shield en 3 étapes

1. Dans une conversation, écrivez : « Protège un dossier avec Shield ». Une fenêtre RAGbase Shield s'ouvre par-dessus Claude : cliquez dedans et choisissez le dossier d'un seul client (2 000 fichiers ou 2 Go au plus). Shield lit le dossier sur votre PC : pour un gros dossier, cette première lecture prend quelques minutes et Claude vous dit où elle en est. Claude reçoit seulement un code, par exemple `DOSSIER_1`.
2. Demandez votre travail, par exemple : « Fais une synthèse du dossier » ou « Rédige une mise en demeure ». Claude lit les documents avec les codes.
3. Écrivez : « Enregistre le document final avec Shield ». Shield remet les vrais noms sur votre PC. Le document est dans le dossier « Shield - sorties » de votre dossier client.

### Ce qui est protégé

Dans les documents du dossier choisi (Word, PDF avec du texte, Excel, texte, e-mails, pages web) : les noms de personnes et de sociétés, les adresses, les téléphones, les e-mails, les dates et lieux de naissance, les IBAN, les numéros de carte, de sécurité sociale, SIREN, SIRET et TVA, les références de procédure. Les noms des fichiers et des sous-dossiers sont protégés aussi.

**Attention :** un texte que vous tapez ou un fichier que vous déposez directement dans la conversation n'est pas masqué par Shield. Il part tel quel.

La détection n'est jamais parfaite : relisez les passages sensibles. Un PDF scanné (une image sans texte) ne peut pas être lu.

### Où restent vos données

- Vos documents d'origine et les vrais noms restent sur votre PC. Claude ne reçoit que le texte avec les codes. Shield n'utilise pas internet.
- Le lien entre les codes et les vrais noms est gardé dans un coffre chiffré, sur votre PC : le dossier « RAGbase Shield » de votre dossier personnel (`C:\Users\<votre nom>\RAGbase Shield`).
- La clé du coffre est dans le Gestionnaire d'identification de Windows, sous le nom « ragbase-shield-plugin ».

### Retirer Shield

1. Dans l'application Claude, ouvrez **Customize > Plugins**, puis retirez « RAGbase Shield (Windows) ».
2. Pour effacer aussi le coffre : supprimez le dossier `C:\Users\<votre nom>\RAGbase Shield` et l'élément « ragbase-shield-plugin » du Gestionnaire d'identification de Windows.
3. Vous pouvez aussi supprimer le dossier `C:\Users\<votre nom>\AppData\Local\RAGbase Shield` : il ne contient que les fichiers de démarrage de Shield, refaits au besoin.

Vos dossiers clients et les documents de « Shield - sorties » restent à leur place.

## English

### What Shield does

- On your PC, Shield replaces names and other private data in your documents with codes such as `PERSONNE_A` or `SOCIETE_B`.
- Claude reads and writes with these codes. It does not see the real names.
- The final document comes back to your PC with the real names.

Free and open source. Nothing else to install.

### Add Shield to Claude

You need the Claude app for Windows.

- **Easiest:** on [shield.ragbase.ai](https://shield.ragbase.ai), click the button for Windows. The Claude app opens: click **Sync**, then **Add** next to "RAGbase Shield (Windows)".
- **Other way:** in the Claude app, open **Customize > Plugins > Add > Add marketplace > Add from a repository**. Type `ragbase/ragbase-shield-windows` and click **Sync**. Then, in the **Discover** tab, click **Add** next to "RAGbase Shield (Windows)".

### Use Shield in 3 steps

1. In a conversation, write: "Protège un dossier avec Shield" (or "Protect a folder with Shield"). A RAGbase Shield window opens on top of Claude: click in it and choose the folder of one client (2,000 files or 2 GB at most). Shield reads the folder on your PC: for a large folder this first reading takes some minutes, and Claude tells you where it is. Claude only gets a code, for example `DOSSIER_1`.
2. Ask for your work, for example: "Summarise the file" or "Draft a formal notice". Claude reads the documents with the codes.
3. Write: "Save the final document with Shield". Shield puts the real names back on your PC. The document is in the "Shield - sorties" folder of your client folder.

### What is protected

In the documents of the chosen folder (Word, PDF with text, Excel, text, e-mails, web pages): names of people and companies, addresses, phone numbers, e-mail addresses, dates and places of birth, IBANs, card, social security, SIREN, SIRET and VAT numbers, case references. File and sub-folder names are protected too.

**Note:** text you type, or a file you drop, directly into the conversation is not masked by Shield. It is sent as it is.

Detection is never perfect: check sensitive passages. A scanned PDF (an image with no text) cannot be read.

### Where your data stays

- Your original documents and the real names stay on your PC. Claude only gets the text with the codes. Shield does not use the internet.
- The link between codes and real names is kept in an encrypted vault on your PC: the "RAGbase Shield" folder in your user folder (`C:\Users\<your name>\RAGbase Shield`).
- The vault key is in Windows Credential Manager, under the name "ragbase-shield-plugin".

### Remove Shield

1. In the Claude app, open **Customize > Plugins** and remove "RAGbase Shield (Windows)".
2. To also erase the vault: delete the folder `C:\Users\<your name>\RAGbase Shield` and the item "ragbase-shield-plugin" in Windows Credential Manager.
3. You can also delete the folder `C:\Users\<your name>\AppData\Local\RAGbase Shield`: it only holds Shield's start files, made again when needed.

Your client folders and the documents in "Shield - sorties" stay where they are.

## Technical details

- **Engine source:** [github.com/ragbase/ragbase-shield](https://github.com/ragbase/ragbase-shield), branch `plugin-claude-tab`, commit `fcde0ac5f4fae092d4392b2651ac56bedab3cfc3`. The plugin runs the module `ragbase_shield.claude_tab` (RAGbase Shield 0.4.3): seven MCP tools in French, detection rules only (no model).
- **Start:** `.mcp.json` runs `${CLAUDE_PLUGIN_ROOT}/engine/shield.exe` (the python.org `pythonw.exe`, renamed: no console window) with `-I -B -X utf8 -m shield_boot`. The start module `shield_boot` (standard library only; compiled in `engine/shield_boot.pyc`, source in `engine/boot-src/shield_boot.py`) unpacks `engine/pkgs.bin` (a zip archive) once into `%LOCALAPPDATA%\RAGbase Shield\engine\0.4.3-<id>` (folder from the system, `<id>` = the first 12 hex characters of the archive's SHA-256, in `engine/pkgs.id`), then runs `ragbase_shield.claude_tab`. Why: the Claude app puts the plugin about 180 to 230 characters deep, and Windows cannot open a path of 260 characters or more by default; every file of the plugin folder has a relative path of 32 characters or less. Each file is written under a temporary name, then renamed; a start that is stopped goes on at the next start; the cache folder can be deleted at any time.
- **Runtime:** Python 3.14.10 for Windows 64-bit, the python.org embeddable package (PSF-2.0), in `engine/`. The standard library is in `engine/python314.bin` (the python.org archive of compiled files, a zip archive under a name that the Claude app accepts; named in `engine/python314._pth`); the packages are in `engine/pkgs.bin`.
- **Data folder:** the vault and the list of dossiers are in `%USERPROFILE%\RAGbase Shield` (profile folder from the system, `FOLDERID_Profile`), not under `AppData`: the packaged Claude app can redirect what its programs write under `AppData` to a folder that Windows deletes with the app.
- **No network:** nothing is downloaded at install or at run time, and the engine opens no network connection. The Mac build is tested with every network access denied by the system.
- **No hooks:** the plugin has no hooks. It can never block or change a message you send to Claude.
- **Integrity:** `SHA256SUMS` at the root of this repository gives the SHA-256 of every file of `plugins/ragbase-shield-windows/`. Check with `shasum -a 256 -c SHA256SUMS` (Mac) or `Get-FileHash` (Windows).
- **Licences:** RAGbase Shield is under the Apache License 2.0 (`LICENSE`, `NOTICE`). The runtime and the packages keep their own licences: full texts in `THIRD_PARTY_LICENSES` (also inside the plugin folder).

Bundled Python packages (41):

| Package | Version | Licence |
|---|---|---|
| annotated-types | 0.8.0 | MIT |
| anyio | 4.15.1 | MIT |
| attrs | 26.1.0 | MIT |
| cffi | 2.1.1 | MIT-0 |
| charset-normalizer | 3.5.2 | MIT |
| click | 8.5.0 | BSD-3-Clause |
| cryptography | 50.0.2 | Apache-2.0 OR BSD-3-Clause |
| h11 | 0.16.0 | MIT |
| httpcore2 | 2.16.0 | BSD-3-Clause |
| httpx2 | 2.16.0 | BSD-3-Clause |
| idna | 3.20 | BSD-3-Clause |
| jaraco.classes | 3.4.0 | MIT License |
| jaraco.context | 6.1.2 | MIT |
| jaraco.functools | 4.6.0 | MIT |
| jsonschema | 4.26.0 | MIT |
| jsonschema-specifications | 2025.9.1 | MIT |
| keyring | 25.7.0 | MIT |
| lxml | 6.1.3 | BSD-3-Clause |
| mcp | 2.3.0 | MIT |
| mcp-types | 2.3.0 | MIT |
| more-itertools | 11.2.1 | MIT |
| opentelemetry-api | 1.45.1 | Apache-2.0 |
| pdfminer.six | 20260107 | MIT |
| pdfplumber | 0.11.10 | MIT License |
| pycparser | 3.12 | BSD-3-Clause |
| pydantic | 2.14.1 | MIT |
| pydantic_core | 2.50.1 | MIT |
| PyJWT | 2.15.1 | MIT |
| pypdf | 6.21.2 | BSD-3-Clause |
| python-docx | 1.2.0 | MIT |
| python-multipart | 0.0.32 | Apache-2.0 |
| pywin32 | 312 | PSF |
| pywin32-ctypes | 0.2.3 | BSD-3-Clause |
| referencing | 0.37.0 | MIT |
| rpds-py | 2026.9.1 | MIT |
| sse-starlette | 3.6.0 | BSD-3-Clause |
| starlette | 1.10.0 | BSD-3-Clause |
| truststore | 0.10.5 | MIT |
| typing_extensions | 4.16.0 | PSF-2.0 |
| typing-inspection | 0.4.4 | MIT |
| uvicorn | 0.54.0 | BSD-3-Clause |
