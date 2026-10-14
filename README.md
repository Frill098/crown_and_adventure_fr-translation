# Crown and Adventure — traduction française

Dépôt de travail pour traduire en français les 62 738 textes uniques du jeu
(`ResourcesGame/data_language/en.marshal`), à l'aide de sessions Claude Code sur le web.

- `source/chunks/cNNN.json` — textes anglais, 180 lots d'environ 25 000 caractères, dans l'ordre des ID.
- `source/duplicates.json` — ID en double → ID de référence (reconstitués à l'assemblage).
- `glossary/` — glossaire commun (`glossary.tsv`), termes d'interface validés, propositions par lot.
- `translations/cNNN.fr.json` — traductions produites.
- `tools/validate.py` — vérifie clés et codes de mise en forme ; `tools/status.py` — avancement.

Consignes des sessions : voir [CLAUDE.md](CLAUDE.md).

**Dépôt privé** : il contient le texte du jeu, qui n'est pas à redistribuer.
