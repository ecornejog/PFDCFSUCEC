from flask import Blueprint, jsonify, request, redirect, url_for
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

@main.route('/calcul/<guid>', methods=['PUT','GET'])
def calcul(guid):
    try:
        calcul_by_guid = CalculModel.get_calcul_by_guid(guid)
        calcul = Calcul(str(calcul_by_guid['guid']), calcul_by_guid['status'], calcul_by_guid['date_debut'],
                        calcul_by_guid['date_fin'], calcul_by_guid['montant'], calcul_by_guid['resultat'])
        #calcul.resultat = resultat.resultat(calcul.montant)
        #calcul.status = bool(1)
        #calcul.date_fin = DateFormat.convert_date(datetime.now())
        #affected_rows = CalculModel.calcul(calcul)
        thread = threading.Thread(target=resultat.resultat(calcul.guid))
        thread.daemon = True         # Daemonize 
        thread.start()
        #return jsonify(calcul.guid)
        #if affected_rows == 1:
        #    return jsonify(calcul.guid)
        #else:
        #    return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/lancerCalcul', methods=['POST'])
async def lancer_Calcul():
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
        if affected_rows == 1:
            await resultat.resultat(calcul.guid)
            #thread = threading.Thread(target=resultat.resultat(guid))
            #thread.daemon = True         # Daemonize 
            #thread.start()
            #redirect(url_for('calcul_blueprint.calcul', guid = calcul.guid))
            return jsonify(calcul.guid)
            #return 
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

