from dataclasses import dataclass

@dataclass
class Participant:
    nom: str
    prenom: str
    fonction: str
    pays: str
    photo: str
    drapeau: str
    genre: str = ""
    ligne_libre: str = ""
    options: str = ""