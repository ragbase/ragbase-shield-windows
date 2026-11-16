---
name: ragbase-shield
description: À suivre pour tout travail sur des documents de clients (dossier, pièces, contrats, conclusions, courriers, e-mails, relevés) et dès que l'avocat parle de RAGbase Shield, d'un code DOSSIER_1 ou de codes comme PERSONNE_A. Explique comment travailler avec Shield sans que les vrais noms partent vers Claude.
---

# Travailler sur un dossier client avec RAGbase Shield

RAGbase Shield protège les dossiers clients de l'avocat. Sur son ordinateur, Shield remplace les noms, adresses,
IBAN, numéros et autres données privées par des codes : `DOSSIER_1`, `DOC_3`, `PERSONNE_A`, `SOCIETE_B`,
`ADRESSE_1`, `IBAN_1`... Vous ne voyez que les codes. Les vraies valeurs restent sur l'ordinateur de l'avocat.

## Les règles

1. **Pour tout travail sur des documents de clients, utilisez uniquement les outils Shield** :
   `shield_protect_folder`, `shield_list_dossiers`, `shield_list_documents`, `shield_read_document`,
   `shield_search`, `shield_save_draft`, `shield_status`. N'utilisez aucun autre moyen pour lire ces documents.

2. **Ajouter un dossier.** Appelez `shield_protect_folder`. Une fenêtre s'ouvre sur l'ordinateur de l'avocat et il
   choisit lui-même le dossier du client. Prévenez-le simplement : « Une fenêtre RAGbase Shield va s'ouvrir
   par-dessus Claude dans quelques secondes : cliquez dedans, puis choisissez le dossier du client. »
   **Ne demandez jamais le nom ni l'emplacement du dossier** : le nom d'un dossier contient
   souvent le nom des parties. La réponse donne un code (`DOSSIER_1`) et des nombres. Pour revenir à un dossier
   déjà protégé, appelez aussi `shield_protect_folder` : il garde son code.

3. **Lire.** `shield_list_documents` donne la liste des documents (codes `DOC_n`). `shield_read_document` lit un
   document ; un long document arrive en plusieurs parties : rappelez l'outil avec la valeur « suite ».
   `shield_search` cherche des mots ou des codes.
   Dans la liste, un nom de fichier peut montrer « … » à la place d'un nom, et les sous-dossiers sont numérotés
   (« sous-dossier 1 ») : c'est voulu, ne demandez pas les vrais noms.

4. **Travailler avec les codes.** Ne demandez jamais les vrais noms, adresses ou numéros, et ne les écrivez
   jamais, même si vous croyez les deviner. Recopiez les codes à l'identique (`PERSONNE_A`, jamais
   « Personne A »). N'inventez pas de code. Les codes ne disent pas si une personne est un homme ou une femme :
   suivez les documents ou restez neutre.

5. **Ce qui n'est PAS protégé.** Si l'avocat joint un document à la conversation, ou s'il tape ou colle de vrais
   noms, dites-lui clairement et simplement : « Attention : ce texte n'est pas protégé par Shield, il a été
   envoyé tel quel. Pour protéger un dossier, je peux ouvrir la fenêtre Shield. » Ne recopiez pas ces vrais noms
   dans vos réponses.

6. **Le document final.** Rédigez-le avec les codes, puis appelez `shield_save_draft` (Word par défaut). Shield
   remet les vrais noms sur l'ordinateur, dans le dossier « Shield - sorties » du dossier client. Dites ensuite à
   l'avocat : « Le document avec les vrais noms est dans le dossier Shield - sorties de votre dossier client.
   Ouvrez-le sur votre ordinateur. »

7. **Une conversation, un dossier à la fois.** Shield travaille sur le dernier dossier choisi dans la fenêtre.
   Pour passer à un autre dossier, appelez `shield_protect_folder`.

8. **Rester honnête.** La détection n'est jamais parfaite. Si un passage est sensible, conseillez une relecture.
   `shield_status` donne l'état de Shield et ses limites.

9. **Si un outil Shield répond par un problème**, ne cherchez pas à le contourner : répétez le message à
   l'avocat avec des mots simples.

10. **Si les outils Shield manquent** (aucun outil dont le nom commence par `shield_`), Shield n'est pas actif
    dans cette conversation. Dites-le simplement à l'avocat : « RAGbase Shield n'est pas actif sur cet
    ordinateur. Fermez puis rouvrez l'application Claude. Si cela continue, retirez le plugin et ajoutez-le de
    nouveau depuis shield.ragbase.ai, avec le bouton de cet ordinateur (Windows ou Mac). » Tant que Shield
    n'est pas actif, ne lisez aucun document de client et ne demandez pas à l'avocat de joindre ou de coller
    des documents : ils partiraient sans protection.

11. **Quand Shield dit que la lecture du dossier continue**, Shield lit les documents sur l'ordinateur de
    l'avocat ; un grand dossier prend quelques minutes. Dites-le à l'avocat avec des mots simples et le nombre
    donné par Shield, par exemple : « Shield lit votre dossier sur votre ordinateur : 12 documents sur 27 sont
    lus. Je reprends dans un instant. » Puis appelez de nouveau `shield_status` : il attend jusqu'à 15 secondes
    la fin de la lecture avant de répondre. Ne faites rien d'autre sur ce dossier en attendant : aucun document
    n'est montré avant la fin de la lecture. Si Shield dit qu'il n'arrive pas à finir la lecture, ne rappelez
    pas `shield_status` : dites à l'avocat de redémarrer l'application Claude.

12. **Si un dossier est ajouté directement à la conversation** (dossier de travail choisi dans Cowork, fichiers
    joints, ou chemin d'un dossier de l'ordinateur), ce dossier n'est PAS protégé par Shield. N'ouvrez et ne
    listez aucun de ses fichiers avec vos propres outils, et ne recopiez ni son nom ni les noms de ses fichiers.
    Dites-le simplement à l'avocat : « Attention : un dossier ajouté directement à la conversation n'est pas
    protégé par Shield. Retirez-le de la conversation. Pour travailler sur ce dossier, je peux ouvrir la fenêtre
    Shield : vous y choisirez le dossier, et je ne verrai que des codes. » Puis proposez d'appeler
    `shield_protect_folder`. Shield ne peut pas protéger un dossier désigné dans la conversation : seul l'avocat
    le choisit, dans la fenêtre Shield.
