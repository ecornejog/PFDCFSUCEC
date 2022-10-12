from datetime import datetime
from time import sleep
from services.CalculService import CalculService
from models.entities.Calcul import Calcul
from utils.DateFormat import DateFormat


class resultat():  # function to do the calcul in 15 seconds

    @classmethod
    def resultat(self, guid):
        calcul_by_guid = CalculService.getCalculByGuid(guid)
        print(calcul_by_guid)
        calcul = Calcul(str(calcul_by_guid['guid']), calcul_by_guid['status'], calcul_by_guid['date_debut'],
                        calcul_by_guid['date_fin'], calcul_by_guid['montant'], calcul_by_guid['resultat'])
        print(" calcul = ",calcul)
        if (calcul.montant):
            calcul.resultat = calcul.montant*1.05
        sleep(15)
        calcul.status = 'termine'
        calcul.date_fin = DateFormat.convert_date(datetime.now())
        #update the calcul in the database after the excecution of resultat.resultat(guid)
        affected_rows = CalculService.calcul(calcul)
        return affected_rows
