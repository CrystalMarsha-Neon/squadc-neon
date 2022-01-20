from apps.helper import Log
from apps.schemas import BaseResponse
from apps.schemas.SchemaCIF import RequestCIF, ResponseCIF, ResponseCustomer, ResponseIDNO,Response_name,Request_data
from apps.helper.ConfigHelper import encoder_app
from main import PARAMS
from apps.models.LoanModel import Loan

SALT = PARAMS.SALT.salt


class ControllerHenson(object):
    
    @classmethod
    def get_customer(cls, input_data=None):
        input_data = RequestCIF(**input_data)
        result = BaseResponse()
        result.status = 400

        try:
            if input_data.idno is not None:
                data = Loan.where('idno', '=', input_data.idno).get().serialize()
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
            data = Loan.count()
            result.status = 200
            result.message = "Success"
            result.data = {"total_entry": data}
            Log.info(result.message)
        except Exception as e:
            Log.error(e)
            result.status = 404
            result.message = str(e)

        return result