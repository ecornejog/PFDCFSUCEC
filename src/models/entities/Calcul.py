from utils.DateFormat import DateFormat


class Calcul():

    def __init__(self, guid, status=None, date_debut=None, date_fin=None, montant=None, resultat=None) -> None:
        self.guid = guid
        self.status = status
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.montant = montant
        self.resultat = resultat

    def to_JSON(self):
        return {
            'guid': self.guid,
            'status': self.status,
            'date_debut': DateFormat.convert_date(self.date_debut),
            'date_fin': DateFormat.convert_date(self.date_fin),
            'montant': self.montant,
            'resultat': self.resultat
        }
