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
python main.py --csv participants.csv python main.py --csv participants.csv --format vertical
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
DUPONT;Jean;competiteur;France;photos/jean.jpg;flags/fr.png;Test ligne libre;bus,lunch
MARTIN;Paul;coach;Germany;photos/paul.jpg;flags/de.png;Coach équipe;
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
