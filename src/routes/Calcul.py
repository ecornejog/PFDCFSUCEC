from time import sleep
from urllib import response
from flask import Blueprint, jsonify, request
from flask import Response
import uuid
from datetime import datetime
from utils.DateFormat import DateFormat
from utils.resultat import resultat
import threading
from contextlib import contextmanager

# Entities
from models.entities.Calcul import Calcul
# Models
from models.CalculModel import CalculModel

main = Blueprint('calcul_blueprint', __name__)


@main.route('/')
def get_calculs():
    try:
        calculs = CalculModel.get_calculs()
        return jsonify(calculs)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


# do the register of the calcul, return the guid to the client and after executes the function to realize the calcul
@main.route('/lancerCalcul', methods=['POST'])
def lancer_Calcul():
    try:
        guid = uuid.uuid4()
        status = bool(0)
        date_debut = datetime.now()
        date_fin = None
        montant = request.json['montant']
        res = None
        calcul = Calcul(str(guid), status, DateFormat.convert_date(date_debut),
                        date_fin, montant, res)

        affected_rows = CalculModel.lancer_Calcul(calcul)
        response = Response(str(guid))

        @response.call_on_close
        def on_close():
            print(str(guid))
            resultat.resultat(str(guid))

        if affected_rows == 1:
            return response

        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
