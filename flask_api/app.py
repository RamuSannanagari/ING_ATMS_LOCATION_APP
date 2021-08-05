from flask import Flask, Response, request, render_template, redirect, session
from flask_restplus import reqparse, Api, Resource, fields
from flask_cors import CORS
import json,os
from collections import OrderedDict

#user modules
from utility.logger import init_logger, log, metrics_logging
from middleware.AtmFlow import AtmflowMiddleware



app = Flask(__name__, static_url_path='/static/')
app.secret_key = 'ItShouldBeAnythingButSecret05L21a0546' 
app.config['CORS_HEADERS'] = 'Content-Type'
Cors = CORS(app)

api = Api(app)
init_logger()

# Defining api models from documentation
model_400 = api.model('Errorresponse400', {'message': fields.String, 'errors': fields.Raw})
model_500 = api.model('Errorresponse400', {'message': fields.Integer, 'errors': fields.String})
model_health_200 = api.model('successResponse200', {'success': fields.Boolean, 'status': fields.Integer})

log.info("API started Successfully")

@api.route('/atms')
@api.response(200, 'Successful')
@api.response(400, 'validation Error', model_400)
@api.response(500, 'Internal processing Error', model_500)
class Atms(Resource):
    def get(self):
        return_status = None
        result = {}
        try:
            log.info("instance Request Initiated")
            fp = AtmflowMiddleware()
            return_status, result = fp.run(operation="select")
        except:
            result = {}
            log.exception('Exception while submitting  processing Request')
            return_status = 500
            result['status'] = 0
            result['message'] = 'Internal Error has Occurred while processing the  request'
        finally:
            resp = Response(json.dumps(result),status=return_status, mimetype="application/json")
        return resp

    def post(self):
        return_status = None
        result = {}
        try:
            log.info("instance Request Initiated")
            fp = AtmflowMiddleware()
            payload=request.json
            return_status, result = fp.run(payload, "insert")
        except Exception as e:
            result = {}
            log.exception('Exception while submitting  processing Request')
            return_status = 500
            result['message'] = 'Internal Error has Occurred while processing the  request'
            result['status'] = 0
        finally:
            resp = Response(json.dumps(result),
                            status=return_status, mimetype="application/json")
        return resp
        
    def put(self):
        return_status = None
        result = {}
        try:
            log.info("instance Request Initiated")
            fp = AtmflowMiddleware()
            payload=request.json
            return_status, result = fp.run(payload, "update")
        except Exception as e:
            result = {}
            log.exception('Exception while submitting  processing Request')
            return_status = 500
            result['message'] = 'Internal Error has Occurred while processing the  request'
            result['status'] = 0
        finally:
            resp = Response(json.dumps(result),
                            status=return_status, mimetype="application/json")
        return resp
        
    def delete(self):
        return_status = None
        result = {}
        try:
            log.info("instance Request Initiated")
            fp = AtmflowMiddleware()
            payload=request.json
            return_status, result = fp.run(payload, "delete")
        except Exception as e:
            result = {}
            log.exception('Exception while submitting  processing Request')
            return_status = 500
            result['message'] = 'Internal Error has Occurred while processing the request'
            result['status'] = 0
        finally:
            resp = Response(json.dumps(result),
                            status=return_status, mimetype="application/json")
        return resp     
api.add_resource(Atms, '/atms', methods=['GET'])
api.add_resource(Atms, '/atms', methods=['POST'])
api.add_resource(Atms, '/atms', methods=['PUT'])
api.add_resource(Atms, '/atms', methods=['DELETE'])


@app.route('/dashboard')
def dashboard():
    if('user' in session and session['user'] == 'test'):
        log.info("instance Request Initiated")
        fp = AtmflowMiddleware()
        return_status, result = fp.run(request, "select")
         
        rest_list=[]
        result_dict=OrderedDict({"housenumber":[],
                 "street":[],
                 "postalcode":[],
                 "city":[],
                 "distance":[],
                 "functionality":[],
                 "type":[]
                 })
        for dict_item in result["data"]:
            res_dict=result_dict.copy()
            res_dict["housenumber"]=dict_item["atm_details"]["address"]["housenumber"]
            res_dict["street"]=dict_item["atm_details"]["address"]["street"]
            res_dict["postalcode"]=dict_item["atm_details"]["address"]["postalcode"]
            res_dict["city"]=dict_item["atm_details"]["address"]["city"]
            res_dict["distance"]=dict_item["atm_details"]["distance"]
            res_dict["functionality"]=dict_item["atm_details"]["functionality"]
            res_dict["type"]=dict_item["atm_details"]["type"]
            rest_list.append(res_dict)
        return render_template("dashboard.html",rest_list = rest_list)


    return '<h1>You are not logged in.</h1>'  #if the user is not in the session

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if(request.method == 'POST'):
        username = request.form.get('username')

        log.info("instance Request Initiated")
        fp = AtmflowMiddleware()
        payload={}
        payload['username']=request.form.get('username')
        payload['password']=request.form.get('password')
        return_status, result = fp.run(payload,"authenticate")

        if result['data']=="Y":     
            print("#############")
            print(username)
            session['user'] = username
            return redirect('/dashboard')

        return "<h1>Wrong username or password</h1>"    #if the username or password does not matches 

    return render_template("login.html")


        
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 7197))
    log.info(port)
    log.info("runing ...")
    app.run(host='0.0.0.0', port=port)
