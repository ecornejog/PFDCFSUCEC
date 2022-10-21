# PFDCFSUCEC
 Plate-forme de calculs financiers sur un cloud à empreinte Carbone négative

## Steps
First create virtual env:
### `python -m virtualenv env`

Activate the virtual env:
### `.\env\Scripts\activate`

Install the required packages:
### `pip install flask flask-cors psycopg2 python-decouple python-dotenv autopep8 flask[async] `

Create a .env file (in the root of the project) for the environment variable:

### `SECRET_KEY=SECRET_KEY`
### `PGSQL_HOST=host`
### `PGSQL_USER=user`
### `PGSQL_PASSWORD=password`
### `PGSQL_DB=database`

## Docker Part

First build the docker:  
### `docker compose build`  
And then up the docker:  
### `docker compose up`  
