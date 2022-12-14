from time import sleep
from flask import Flask, Response, request, jsonify
from flask_cors import CORS
from utils.resultat import resultat

#from config import config

# Routes
from routes import Calcul

app = Flask(__name__)

CORS(app, resources={"*": {"origins": "http://localhost:9300"}})

@app.route('/')
def hello_world():
    return 'Flask Dockerized'

def page_not_found(error):
    return "<h1>Not found page</h1>", 404


if __name__ == '__main__':
    #app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(Calcul.main, url_prefix='/api/v1')
    app.register_blueprint(Calcul.main, url_prefix='/',name="def")



    # Error handlers
    app.register_error_handler(404, page_not_found)
    app.run(host='0.0.0.0',port=5000,threaded=True)
