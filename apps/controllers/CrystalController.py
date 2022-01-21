from apps.helper import Log
from apps.schemas import BaseResponse
from apps.schemas.SchemaCIF import RequestCIF, ResponseCIF, ResponseCustomer, ResponseIDNO,Response_name,Request_data
from apps.helper.ConfigHelper import encoder_app
from main import PARAMS
from apps.models.LoanModel import Loan
from datetime import *
from apps.models import db as conn
import datetime
# from apps.models.BorrowerModel import Borrower
SALT = PARAMS.SALT.salt
class ControllerCrystal(object):
    @classmethod
    def get_loan_by_loan_id(cls,loanid,dob):
        result = BaseResponse()
        result.status = 400
        try:
            if loanid is not None and dob is not None:
                    data = Loan.where('loanid', '=', loanid).where('dob','=',dob).get().serialize()
                    result.status = 200
                    result.message = "Success"
                    result.data = {"CIF": data}
                    Log.info(result.message)
            else:
                    e = "data is empty"
                    Log.error(e)
                    result.status = 404
                    result.message = str(e)
        except Exception as e:
                Log.error(e)
                result.status = 400
                result.message = str(e)
        return result
    @classmethod
    def update_cif(cls,cif,updated_at):
        result = BaseResponse()
        result.status = 400
        try:
            data = conn.table('digital_lending_dataset').where('cif', '=', cif).update({'deleted':2,"updatedate":datetime.datetime.now()})
            if cif is not None and data == 1:
                    result.status = 200
                    result.message = "Success"
                    result.data = {"entry cif: " + cif + " deleted has been updated": data}
                    Log.info(result.message)
            else:
                    e = "data is empty or cif doesn't exist"
                    Log.error(e)
                    result.status = 404
                    result.message = str(e)
        except Exception as e:
                Log.error(e)
                result.status = 400
                result.message = str(e)
        return result

    @classmethod
    def delete_cif(cls,cif,updated_at):
        result = BaseResponse()
        result.status = 400
        try:
            data = conn.table('digital_lending_dataset').where('cif', '=', cif).where('deleted', '=', 0).update({'deleted':1})
            if cif is not None and data == 1:
                    result.status = 200
                    result.message = "Success"
                    result.data = "entry cif: " + cif + " has been deleted"
                    Log.info(result.message)
            else:
                    e = "data is empty or cif doesn't exist"
                    Log.error(e)
                    result.status = 404
                    result.message = str(e)
        except Exception as e:
                Log.error(e)
                result.status = 400
                result.message = str(e)
        return result

    @classmethod
    def get_biggest_loan(cls):
        result = BaseResponse()
        result.status = 400
        try:
            data = conn.table('digital_lending_dataset').max('loan_amount')
            result.status = 200
            result.message = "Success"
            result.data = {"Macimum loan amount": data}
            Log.info(result.message)
        except Exception as e:
            Log.error(e)
            result.status = 404
            result.message = str(e)
        return result
