from database.db import get_connection
from models.entities.Calcul import Calcul



class CalculService():



    @classmethod
    def saveCalcul(self, calcul):

        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO calcul (guid, status, date_debut, date_fin, montant, resultat) 
                                VALUES (%s, %s, %s, %s, %s, %s)""",
                               (calcul['guid'], calcul['status'], calcul['date_debut'],
                                calcul['date_fin'], calcul['montant'], calcul['resultat']))
                affected_rows = 1
                connection.commit()

            connection.close()
            print(calcul)
            return calcul
        except Exception as ex:
            print(str(ex))
            return None


    @classmethod
    def updateCalcul(self, calcul):

        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE calcul set status=%s where guid=%s """,
                               (calcul['status'],calcul['guid'] ))
                affected_rows = 1
                connection.commit()

            connection.close()
            print(calcul)
            return calcul
        except Exception as ex:
            print(str(ex))
            return None



    @classmethod
    def get_calculs(self):  # get all the calculs
        try:
            connection = get_connection()
            calculs = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM calcul")
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
    def getCalculByGuid(self, guid):  # get the calcul from an GUID
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT guid, status, date_debut, date_fin, montant, resultat FROM calcul WHERE guid = %s", (guid,))
                row = cursor.fetchone()
                calcul = None
                if row != None:
                    calcul = Calcul(row[0], row[1], row[2],
                                    row[3], row[4], row[5])
                    calcul = calcul.to_JSON()


            connection.close()
            return calcul
        except Exception as ex:
            return None



  

    @classmethod
    def calcul(self, calcul):  # update the calcul in the database after the excecution of resultat.resultat(guid)

        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE calcul SET status = %s, 
                date_fin = %s, 
                resultat = %s
                WHERE calcul.guid = %s""",
                               (calcul.status, calcul.date_fin,
                                calcul.resultat, calcul.guid))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def resultat(self, guid):
        calcul_by_guid = CalculService.getCalculByGuid(guid)
        calcul = Calcul(str(calcul_by_guid['guid']), calcul_by_guid['status'], calcul_by_guid['date_debut'],
                        calcul_by_guid['date_fin'], calcul_by_guid['montant'], calcul_by_guid['resultat'])
        if (calcul.montant):
            calcul.resultat = calcul.montant*1.05
        sleep(15)
        calcul.status = 'termine'
        calcul.date_fin = DateFormat.convert_date(datetime.now())
        affected_rows = CalculService.saveCalcul(calcul)
        return affected_rows