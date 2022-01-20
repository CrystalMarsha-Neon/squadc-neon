from ast import Try
from apps.helper import Log
from apps.schemas import BaseResponse
from apps.schemas.SchemaCIF import RequestCIF, ResponseCIF, ResponseCustomer, ResponseIDNO,Response_name,Request_data, RequestHenson
from apps.helper.ConfigHelper import encoder_app
from main import PARAMS
from apps.models.LoanModel import Loan
from apps.models import db as conn
import json
import datetime

SALT = PARAMS.SALT.salt


class ControllerHenson(object):
    
    @classmethod
    def get_customer(cls, input_data=None):
        input_data = RequestCIF(**input_data)
        result = BaseResponse()
        result.status = 400

        try:
            if input_data.idno is not None:
                data = Loan.where('idno', '=', input_data.idno).where('deleted', '=', 0).get().serialize()
                result.status = 200
                result.message = "Success"
                result.data = ResponseCustomer(**{"customer": data})
                Log.info(result.message)
            else:
                e = "idno not found!"
                Log.error(e)
                result.status = 404
                result.message = str(e)
        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result

    @classmethod
    def total_entry(cls):
        result = BaseResponse()
        result.status = 400

        try:
            data = Loan.where('deleted', '=', 0).count()
            result.status = 200
            result.message = "Success"
            result.data = {"total_entry": data}
            Log.info(result.message)
        except Exception as e:
            Log.error(e)
            result.status = 404
            result.message = str(e)

        return result

    @classmethod
    def delete_entry(cls, input_data=None):
        result = BaseResponse()
        result.status = 400
        input_data = RequestCIF(**input_data)

        try:
            if input_data.loanid is not None:
                hasil = conn.table('digital_lending_dataset').where('loanid', input_data.loanid).where('deleted', '=', 0).update({'deleted':1})
                if hasil != 0:                                
                    result.status = 200
                    result.message = "Success"
                    result.data = "entry loanid: " + input_data.loanid + " has been deleted"   
                else:
                    result.status = 200
                    result.message = "No such entry"  
            else:
                e = "loanid not found"
                Log.error(e)
                result.message = str(e)
                result.status = 404
        except Exception as e:
            Log.error(e)
            result.message = str(e)
            result.status = 404
        
        return result

    @classmethod
    def update_income(cls, input_data=None):
        result = BaseResponse()
        result.status = 400
        input_data = RequestHenson(**input_data)

        try:
            if input_data.idno is not None:
                hasil = conn.table('digital_lending_dataset').where('idno', input_data.idno).where('deleted', '=', 0)\
                    .update({"income": input_data.income,"updatedate":datetime.datetime.now()})
                # data = Loan.where("loanid", "=", input_data.loanid).update(**{"deleted": 1})                
                if hasil != 0:
                    result.status = 200
                    result.message = "Success"
                    result.data = "entry loanid: " + input_data.idno + " successfully updated with income: " + input_data.income                
                else:
                    result.status = 200
                    result.message = "No such entry"   
            else:
                e = "idno not found"
                Log.error(e)
                result.message = str(e)
                result.status = 404
        except Exception as e:
            Log.error(e)
            result.message = str(e)
            result.status = 404

        return result