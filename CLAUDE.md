# Traduction FR de Crown and Adventure — consignes pour les sessions Claude Code

Tu traduis en **français** les textes anglais du jeu de stratégie / RPG médiéval-fantastique
*Crown and Adventure* (dialogues, narration, quêtes, objets, compétences). Les fichiers
traduits sont réinjectés dans le jeu par un script local ; tu n'as rien d'autre à construire.

## Ce qu'on attend de toi

La personne qui lance la session t'indique soit **« glossaire »**, soit une **plage de lots**
(ex. `c001-c012`). Ne traite que ce qu'on t'a attribué : d'autres sessions travaillent en
parallèle sur d'autres lots, et tu ne dois pas toucher à leurs fichiers.

### Tâche « glossaire » (à faire une seule fois, avant les lots)

1. Lis `glossary/term_candidates.tsv` (termes anglais fréquents) et `glossary/ui_terms.json`
   (traductions déjà validées de l'interface, à respecter).
2. Écris `glossary/glossary.tsv` : colonnes `english<TAB>french<TAB>categorie<TAB>note`.
   Ne garde que les vrais termes du jeu (noms de lieux, factions, peuples, titres, objets,
   mécaniques) ; ignore les mots courants (« After », « Take »...). Vise 300 à 800 lignes.
   Catégories : `personnage`, `lieu`, `faction`, `peuple`, `titre`, `objet`, `mecanique`, `autre`.
3. Commit `glossaire: premiere version` et push.

### Tâche « lots » (`cNNN`)

Pour chaque lot attribué, dans l'ordre :

1. Lis `source/chunks/cNNN.json` : un objet `{ "ID": "texte anglais" }`, dans l'ordre de l'histoire.
2. Écris `translations/cNNN.fr.json` : **exactement les mêmes clés**, valeurs en français.
   JSON UTF-8, `ensure_ascii` désactivé (accents en clair), indentation 1.
   Pour un gros lot, tu peux écrire le fichier en plusieurs fois, mais le résultat final doit
   être un seul objet JSON valide.
3. Lance `python tools/validate.py cNNN` et corrige **toutes** les erreurs. Les avertissements
   « looks untranslated » doivent être vérifiés (souvent un oubli).
4. `git add translations/cNNN.fr.json` puis commit `trad: cNNN` et `git push` (en cas de rejet :
   `git pull --rebase` puis push). Passe au lot suivant.

Ne relis pas inutilement des fichiers déjà lus, ne lance pas de sous-agents : le budget est limité.

## Règles de traduction

- **Qualité littéraire** : un français naturel et fluide, pas mot à mot. Narration au passé
  ou au présent comme l'original, dialogues vivants et adaptés au personnage.
- **Univers médiéval-fantastique** : registre soutenu pour nobles, prêtres, chroniques ;
  familier pour mercenaires, bandits, soldats. Pas d'anachronismes.
- **Tu / vous** : *vous* par défaut (inconnus, supérieurs, nobles, marchands) ; *tu* entre
  compagnons proches, envers un subordonné méprisé, dans les insultes et les menaces.
  Reste cohérent au sein d'une même scène (lots voisins = scènes voisines).
- **Noms propres** : les noms de personnes romanisés (Chen-Yuan, Honglu, Lucius...) restent
  tels quels. Les noms descriptifs (lieux, factions, titres) se traduisent selon
  `glossary/glossary.tsv`. Un nouveau terme absent du glossaire : choisis une traduction et
  ajoute-la à `glossary/new_terms/cNNN.tsv` (même format), jamais au glossaire principal.
- **Interface** : respecte `glossary/ui_terms.json` (Clan, Royaume, Légion, Gouverneur,
  Puissance, Ducats...). Textes courts (boutons, titres) : reste concis.
- **Typographie** : espace avant `? ! : ;`, guillemets « », points de suspension `...`,
  apostrophe droite `'`. Majuscules accentuées (À, É).

## Codes à conserver À L'IDENTIQUE (le validateur les vérifie)

| Code | Rôle | Exemple |
|---|---|---|
| `#C(FFxxxxxx)` … `#n` / `#N` | couleur | `#C(FF5AACDB)Lancelot#n` |
| `#r` / `#R` | retour à la ligne | `Ligne 1#rLigne 2` |
| `#Q` `#Y` `#G` `#S` `#A` | codes d'affichage | garder collé au mot qui suit |
| `#p{{...}}` | icône | ne jamais modifier |
| `{nom}` | variable remplacée par le jeu | `{ware}`, `{target_count}` — ne pas traduire le nom |
| `[player]`, `[Player]`, `[Area]`, `[Goods]` | variables | ne pas traduire |
| `<strong>` `</strong>` | balises | conserver |
| saut de ligne réel `\n` | | même nombre |

Tu peux déplacer un code dans la phrase si la grammaire française l'exige, mais jamais
en changer le nombre ni le contenu. Les autres crochets (`[Cloud Sea Library]`) sont du
texte normal : traduis-les.

Quelques textes anglais contiennent encore du chinois ou des notes internes (ex.
« 解析异常，请人工校对 ») : traduis la partie anglaise et laisse le reste tel quel.
