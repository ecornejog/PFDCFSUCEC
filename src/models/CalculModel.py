from database.db import get_connection
from .entities.Calcul import Calcul


class CalculModel():

    @classmethod
    def get_calculs(self):
        try:
            connection = get_connection()
            calculs = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM test_projet")
                resultset = cursor.fetchall()

                for row in resultset:
                    calcul = Calcul(row[0], row[1], row[2],
                                    row[3], row[4], row[5])
                    calculs.append(calcul.to_JSON())

            connection.close()
            return calculs
        except Exception as ex:
            raise Exception(ex)
            
    @classmethod
    def get_calcul_by_guid(self, guid):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT guid, status, date_debut, date_fin, montant, resultat FROM test_projet WHERE guid = %s", (guid,))
                row = cursor.fetchone()

                calcul= None
                if row != None:
                    calcul = Calcul(row[0], row[1], row[2],
                                    row[3], row[4], row[5])
                    calcul = calcul.to_JSON()

            connection.close()
            return calcul
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def lancer_Calcul(self, montant):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO test_projet (guid, status, date_debut, date_fin, montant, resultat) 
                                VALUES (%s, %s, %s, %s, %s, %s)""",
                               (montant.guid, montant.status, montant.date_debut,
                                montant.date_fin, montant.montant, montant.resultat))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def calcul(self,calcul):

        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE test_projet SET status = %s, 
                date_fin = %s, 
                resultat = %s
                WHERE test_projet.guid = %s""",
                               (calcul.status,calcul.date_fin, 
                               calcul.resultat,calcul.guid))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
