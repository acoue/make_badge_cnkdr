import csv
from models import Participant

def read_csv(filepath):
    with open(filepath, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, delimiter=";")
        participants = []

        for row in reader:
            participants.append(Participant(
                nom=row.get("nom", ""),
                prenom=row.get("prenom", ""),
                fonction=row.get("fonction", ""),
                pays=row.get("pays", ""),
                photo=row.get("photo", ""),
                drapeau=row.get("drapeau", ""),
                genre=row.get("genre", ""),
                ligne_libre=row.get("ligne_libre", ""),
                options=row.get("options", "")
            ))

        return participants