import requests
import json
from utility.logger import log
from resources.atm_data_process import Atm_dml

class AtmflowMiddleware:

    def __init__(self):
        pass
    def run(self,payload=None,operation=None):
        """     
        This function process the request and returns response
        """
        return_status = None
        result = {}
        db_obj =Atm_dml()
        db_res=None
        try:
            
            if operation == "select":
               db_res=db_obj.fetch_atmdata()
               for i,dict_row in enumerate(db_res):
                   for k,v in dict_row.items():
                       if k == "atm_details":
                          db_res[i]["atm_details"]=json.loads(v)
                   
            elif operation == "insert":
               atm_details=payload.get("atm_details")
               
               if not atm_details:
                  db_res="please provid valid atm_details payload"
               else:
                  db_obj.create_atmdata(payload["atm_details"])
                  db_res=" atm_details inserted successfully"
            elif operation == "update":
              id=payload.get("id")
              atm_details=payload.get("atm_details")
              
              if not id or not atm_details:
                 db_res="please provid valid id and atm_details"
              else:
                  db_obj.update_atmdata(id,atm_details)
                  db_res=" atm_details updated successfully"                 
            elif operation == "delete":
              id=payload.get("id")
              
              if not id:
                 db_res="please provid valid id"
              else:
                  db_obj.delete_atmdata(id)
                  db_res=" atm_details deleted successfully"                     
            elif operation == "authenticate":
              username=payload.get('username')
              password=payload.get('password')
              
              if not username or not password:
                 db_res="please provid valid Login Details"             
              else:
                  res=db_obj.authenticate(username,password)  
                  if not res:
                     db_res="N"
                  else:
                     db_res="Y"
            return_status = 200
            result['status'] = 1
            result['data'] = db_res
        except Exception:
            result = {}
            log.exception("Exception while submitting feedback")
            return_status = 500
            result['status'] = 0
            result['message'] = (
                'Internal Error has occurred while processing the request')
        finally:
            del db_obj
        return return_status, result
