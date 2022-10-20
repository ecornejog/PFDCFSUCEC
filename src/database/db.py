import psycopg2
from psycopg2 import DatabaseError
from decouple import config


def get_connection():
    try:
        return psycopg2.connect(
            host='localhost',
            user='postgres',
            password='azerty',
            database='Poc_Ec'
        )
    except DatabaseError as ex:
        raise ex


# password =  azerty
# port = 5432
