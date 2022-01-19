from apps.helper import Log
from apps.schemas import BaseResponse
<<<<<<< HEAD
from apps.schemas.SchemaCIF import RequestCIF, ResponseCIF, ResponseIDNO
=======
from apps.schemas.SchemaCIF import RequestCIF, ResponseCIF, ResponseCustomer
>>>>>>> 1913fc6499d5d5d349fe5f733b4e45524b0d6357
from apps.helper.ConfigHelper import encoder_app
from main import PARAMS
from apps.models.LoanModel import Loan

SALT = PARAMS.SALT.salt


class ControllerLoan(object):
    @classmethod
    def get_loan_by_cif(cls, input_data=None):
        input_data = RequestCIF(**input_data)
        result = BaseResponse()
        result.status = 400

        try:
            if input_data.cif is not None:
                data = Loan.where('cif', '=', input_data.cif).get().serialize()
                result.status = 200
                result.message = "Success"
                result.data = encoder_app(ResponseCIF(**{"cif_list": data}).json(), SALT)
                Log.info(result.message)
            else:
                e = "cif not found!"
                Log.error(e)
                result.status = 404
                result.message = str(e)
        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result

    @classmethod
    def get_loan_by_cif_debug(cls, input_data=None):
        input_data = RequestCIF(**input_data)
        result = BaseResponse()
        result.status = 400

        try:
            if input_data.cif is not None:
                data = Loan.where('cif', '=', input_data.cif).get().serialize()
                result.status = 200
                result.message = "Success"
                result.data = ResponseCIF(**{"cif_list": data})
                Log.info(result.message)
            else:
                e = "cif not found!"
                Log.error(e)
                result.status = 404
                result.message = str(e)
        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result
<<<<<<< HEAD
    
    @classmethod
    def rifki(cls, input_data=None):
=======

    @classmethod
    def get_customer(cls, input_data=None):
>>>>>>> 1913fc6499d5d5d349fe5f733b4e45524b0d6357
        input_data = RequestCIF(**input_data)
        result = BaseResponse()
        result.status = 400

        try:
            if input_data.idno is not None:
                data = Loan.where('idno', '=', input_data.idno).get().serialize()
                result.status = 200
                result.message = "Success"
<<<<<<< HEAD
                result.data = ResponseIDNO(**{"idno_list": data})
                Log.info(result.message)
            else:
                e = "idno not found!"
=======
                result.data = ResponseCustomer(**{"customer": data})
                Log.info(result.message)
            else:
                e = "cif not found!"
>>>>>>> 1913fc6499d5d5d349fe5f733b4e45524b0d6357
                Log.error(e)
                result.status = 404
                result.message = str(e)
        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result