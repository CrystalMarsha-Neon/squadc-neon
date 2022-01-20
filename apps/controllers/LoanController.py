from apps.helper import Log
from apps.schemas import BaseResponse
from apps.schemas.SchemaCIF import RequestCIF, ResponseCIF, ResponseCustomer, ResponseIDNO,Response_name,Request_data
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
    def get_loan_by_name(cls,fname,lname,dob):
        result = BaseResponse()
        result.status = 400
        try:
            if fname is not None and lname is not None or dob is not None:
                    data = Loan.where(('fname', '=', fname)).get().serialize()
                    result.status = 200
                    result.message = "Success"
                    result.data = { "CIF": data}
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
