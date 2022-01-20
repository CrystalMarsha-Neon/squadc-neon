from apps.helper import Log
from apps.schemas import BaseResponse
from apps.schemas.SchemaCIF import RequestCIF, ResponseIDNO
from apps.helper.ConfigHelper import encoder_app
from main import PARAMS
from apps.models.LoanModel import Loan
# from apps.models.BorrowerModel import Borrower
SALT = PARAMS.SALT.salt

class ControllerRifki(object):
    @classmethod
    def get_loan_by_idno(cls, input_data=None):
        input_data = RequestCIF(**input_data)
        result = BaseResponse()
        result.status = 400

        try:
            if input_data.idno is not None:
                data = Loan.where('idno', '=', input_data.idno).get().serialize()
                result.status = 200
                result.message = "Success"
                result.data = ResponseIDNO(**{"idno_list": data})
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
    def get_loan_type_activate(cls, input_data):
        input_data = input_data
        result = BaseResponse()
        result.status = 400
        typestat = int(input_data)    

        try:
            if typestat > 0 and typestat < 4:
                data = Loan.where('loan_status', '=', input_data).count()
                result.status = 200
                result.message = "Success"
                result.data = {"count_loan_active": data}
                Log.info(result.message)
            else:
                e = "loan_type not found! Please check the example input!"
                Log.error(e)
                result.status = 404
                result.message = str(e)
                
        except Exception as e:
            Log.error(e)
            result.status = 404
            result.message = str(e)

        return result