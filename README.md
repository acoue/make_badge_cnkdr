# Badges PDF A5 EJC 2026

Fichiers générés :


## Installer les dépendances
```bash
pip install -r requirements.txt
```

## Exécuter
```bash
python main.py --csv participants.csv
```

## Colonnes CSV attendues
- `nom`
- `prenom`
- `fonction`
- `photo`
- `pays`
- `drapeau`

Le script accepte aussi les variantes :
- `prénom`, `firstname`
- `role`
- `country`
- `flag`
- `photo_path`

Chaque ligne génère 1 page A5 dans le PDF.
