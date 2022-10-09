from time import sleep
from flask import Flask, Response, request
from flask_cors import CORS
from utils.resultat import resultat

from config import config

# Routes
from routes import Calcul

app = Flask(__name__)

CORS(app, resources={"*": {"origins": "http://localhost:9300"}})


def page_not_found(error):
    return "<h1>Not found page</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(Calcul.main, url_prefix='/api/calcul')

    # Error handlers
    app.register_error_handler(404, page_not_found)
    app.run(threaded=True)
