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
from services.CalculService import CalculService

main = Blueprint('calcul_blueprint', __name__)


@main.route('/')
def get_calculs():
    try:
        calculs = CalculService.get_calculs()
        return jsonify(calculs)
    except Exception as ex:
        return jsonify({'messagess': str(ex)}), 500


# do the register of the calcul, return the guid to the client and after executes the function to realize the calcul
@main.route('/startCalcul', methods=['POST'])
def startCalcul():
    try:
        guid = uuid.uuid4()
        print(guid)
        status = 'en_cours'
        date_debut = datetime.now()
        date_fin = None
        #Modify montant
        
        montant = request.json['montant']
        res = None
        calcul = Calcul(str(guid), status, DateFormat.convert_date(date_debut),
                        date_fin, montant, res)

        affected_rows = CalculService.saveCalcul(calcul.to_JSON())
        print("affected ",affected_rows)
        response = Response(str(guid))

        @response.call_on_close
        def on_close():
            print(str(guid))
            resultat.resultat(str(guid))

        if (affected_rows != None):
            return response

        else:
            return jsonify({'messages': "Error on insert"}), 500
            
    except Exception as ex:
        return jsonify({'messages': str(ex)}), 500




@main.route('/consultStatus/<guid>', methods=['GET'])
def consulterStatus(guid):

    guid=request.view_args['guid']
    calc=CalculService.getCalculByGuid(guid)

    if(calc== None):
        return jsonify({'message': 'Guid Not found'}), 404
    
    date_debut=calc['date_debut']
    date_fin= calc['date_fin']
    print(date_fin ," fin")
    status= calc['status']
    actual_date=str(DateFormat.convert_date(datetime.now())).replace(" ","")
    actual_date=actual_date.replace('"','')  


    print(actual_date)
    delta=DateFormat.deltaTime(date_debut,actual_date)


    if(date_fin == None):
        
        if(delta >15):  # update status to timeout
                calc['status']='timeout'
                res=CalculService.updateCalcul(calc)
                status='timeout'
        # en cours || timeout
    return jsonify({'message': str(status)}), 200





@main.route('/consultResult/<guid>', methods=['GET'])
def consultResult(guid):

    guid=request.view_args['guid']
    calc=CalculService.getCalculByGuid(guid)

    if(calc== None):
        return jsonify({'message': 'Result Not found'}), 404
    
    date_debut=calc['date_debut']
    date_fin= calc['date_fin']
    status= calc['status']
    if(status=='termine'):
        return jsonify({'Result': calc['resultat']}), 200



    actual_date=str(DateFormat.convert_date(datetime.now())).replace(" ","")
    actual_date=actual_date.replace('"','')  
    delta=DateFormat.deltaTime(date_debut,actual_date)


    if(date_fin == None):
        
        if(delta >15):  # update status to timeout
                calc['status']='timeout'
                res=CalculService.saveCalcul(calc)
                status='timeout'

        # en cours || timeout
    return jsonify({'message': "Resultat  "+str(status)}), 200




        
