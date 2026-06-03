# 🎫 Badge Generator CNKDR

Générateur de badges PDF (format A5) pour événements type compétition.

Ce projet permet de créer automatiquement des badges personnalisés à partir d’un fichier CSV avec :

- 📸 photo du participant
- 🏳️ drapeau et pays
- 👤 nom + texte libre
- 🎯 pictogrammes (bus, lunch, sayonara, etc.)
- 🟥 bandeau rôle (compétiteur, coach, arbitre, bénévole, etc.)
- 🧩 plusieurs layouts (`vertical` / `editorial`)
- 🐞 mode debug visuel pour vérifier les blocs et alignements

---

# 🚀 Installation

## 1. Cloner le projet
```
git clone <repo>
cd make_badge_cnkdr
```

## 2. Créer un environnement virtuel
```
python -m venv venv
source venv/Scripts/activate   # Windows
```

## 3. Installer les dépendances
```
pip install -r requirements.txt
```

## 4. Utilisation
### Layout editorial (par défaut)
```
python main.py --csv participants.csv 
```

### Layout vertical
```
python main.py --csv participants.csv --format vertical
```

### Mode debug (affichage des blocs)
```
python main.py --csv participants.csv --debug
```

# 📄 Format du CSV
```
nom;prenom;fonction;pays;photo;drapeau;ligne_libre;options
DUPONT;Jean;competiteur;France;jean.jpg;fr.png;Test ligne libre;bus,lunch
MARTIN;Paul;coach;Germany;paul.jpg;de.png;Coach équipe;
```

# 🎨 Layouts disponibles

## 🧾 Editorial
PHOTO | NOM
      | TEXTE

FLAG  | COUNTRY

PICTOS (plein largeur)

ROLE

## 📋 Vertical

PHOTO
NAME
TEXT
FLAG + COUNTRY
PICTOS
ROLE

# 🔳 Verso (QR Code)

Le projet permet de générer un **verso de badge avec QR codes**.

Contrairement au recto, les QR codes ne sont pas liés aux participants mais à des **informations générales de l’événement** :

- accès badge
- programme
- transport
- restauration
- contacts
- etc.

---
Chaque QR contient :
- une donnée (URL, code, etc.)
- un label affiché sous le QR
- un logo centré dans le QR

---

## Activation

Le verso est activé via :

```python
DOCUMENT_RECTO_VERSO = True
```
# ✅ 2. Ajouter la config `QR_BACK`
```md
## Configuration QR (`QR_BACK`)

```python
QR_BACK = {
    "TITLE": "Informations & accès",

    # Marges page
    "TOP_MARGIN": 45,     # Marge haute du verso
    "BOTTOM_MARGIN": 45,  # Marge basse
    "LEFT_MARGIN": 25,     # Marges latérales
    "RIGHT_MARGIN": 25,

    # Espacement entre lignes et colonnes
    "ROW_GAP": 22,     # Espace vertical entre lignes
    "COL_GAP": 18,     # Espace horizontal entre QR

    # Taille du QR
    "QR_SIZE": 90,     # taille du QR

    # Paramètres QR
    "QR_BORDER": 2,     # bordure du QR
    "QR_BOX_SIZE": 10,     # granularité du QR
    "QR_ERROR_CORRECTION": "H",     # niveau de correction (L/M/Q/H)

    # Logo au centre du QR
    "QR_LOGO_PATH": "assets/logos/qr_center_logo.png",
    "QR_LOGO_RATIO": 0.22,     # taille relative du logo
    "QR_LOGO_PADDING": 4,     # padding blanc autour

    # Texte sous le QR
    "LABEL_FONT_NAME": "Helvetica",
    "LABEL_FONT_SIZE": 9,     # taille du texte
    "LABEL_LINE_HEIGHT": 11,     # espacement lignes
    "LABEL_MAX_CHARS": 22,     # longueur max par ligne
}
```
# ✅ 3. Ajouter la config `BACK_QR_ROWS`

👉 Très important ⭐

```md
## Définition des QR (`BACK_QR_ROWS`)

Les QR sont définis par lignes dans la config :

```python
BACK_QR_ROWS = [
    [
        {
            "label": "Accès badge",
            "data": "EJC2026|badge_access"
        },
        {
            "label": "Programme",
            "data": "https://ejc2026.fr/programme"
        },
        {
            "label": "Règlement",
            "data": "https://ejc2026.fr/reglement"
        },
    ],
    [
        {
            "label": "Transport",
            "data": "https://ejc2026.fr/transport"
        },
        {
            "label": "Restauration",
            "data": "https://ejc2026.fr/restauration"
        },
        {
            "label": "Contacts",
            "data": "EJC2026|contact"
        },
    ],
]
```




# ⚙️ Configuration

Le fichier `config.py` centralise tous les paramètres du moteur :

- tailles des blocs (photo, texte, pictos…)
- espacements verticaux
- marges globales
- couleurs des rôles
- mapping des pictogrammes

## Bonnes pratiques

✅ Utiliser les variables pour ajuster le layout
✅ Ne jamais modifier directement le code des layouts
✅ Toujours tester avec `--debug`

## Exemples

Augmenter l’espace entre pictos et rôle :

```python
"SPACE_PICTOS_TO_ROLE": 20
```
Ajouter du padding sous le header :
```python
"TOP_CONTENT_MARGIN": 30
```
Agrandir les pictos :
```python
"PICTO_SIZE": 50
```

# 📌 Licence

Ce projet est distribué sous licence MIT.

Voir le fichier LICENSE pour plus de détails.
