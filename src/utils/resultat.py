from datetime import datetime
from time import sleep
from models.CalculModel import CalculModel
from models.entities.Calcul import Calcul
from utils.DateFormat import DateFormat


class resultat():  # function to do the calcul in 15 seconds

    @classmethod
    def resultat(self, guid):
        calcul_by_guid = CalculModel.get_calcul_by_guid(guid)
        calcul = Calcul(str(calcul_by_guid['guid']), calcul_by_guid['status'], calcul_by_guid['date_debut'],
                        calcul_by_guid['date_fin'], calcul_by_guid['montant'], calcul_by_guid['resultat'])
        if (calcul.montant):
            calcul.resultat = calcul.montant*1.05
        sleep(15)
        calcul.status = bool(1)
        calcul.date_fin = DateFormat.convert_date(datetime.now())
        affected_rows = CalculModel.calcul(calcul)
        return affected_rows
