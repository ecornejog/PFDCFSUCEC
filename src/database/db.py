import psycopg2
from psycopg2 import DatabaseError
from decouple import config


def get_connection():
    try:
        return psycopg2.connect(
            host='postgres',
            user='docker',
            password='docker',
            database='docker'
        )
    except DatabaseError as ex:
        raise ex


# password =  azerty
# port = 5432
