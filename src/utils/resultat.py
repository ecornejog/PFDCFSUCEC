from datetime import datetime
from time import sleep
from models.CalculModel import CalculModel
from models.entities.Calcul import Calcul
from utils.DateFormat import DateFormat


class resultat():

    @classmethod
    async def resultat(self, guid):
        print("entra a resultat")
        calcul_by_guid = CalculModel.get_calcul_by_guid(guid)
        calcul = Calcul(str(calcul_by_guid['guid']), calcul_by_guid['status'], calcul_by_guid['date_debut'],
                        calcul_by_guid['date_fin'], calcul_by_guid['montant'], calcul_by_guid['resultat'])
        if (calcul.montant):
            calcul.resultat = calcul.montant*1.05
            print(calcul.resultat)
        print("comienza el sleep")
        sleep(15)
        calcul.status = bool(1)
        calcul.date_fin = DateFormat.convert_date(datetime.now())
        print("antes de hacer el put")
        affected_rows = CalculModel.calcul(calcul)
        print("luego del put")
        return affected_rows
