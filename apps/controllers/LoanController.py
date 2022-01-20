from apps.helper import Log
from apps.schemas import BaseResponse
from apps.schemas.SchemaCIF import RequestCIF, ResponseCIF, ResponseCustomer, ResponseIDNO,Response_name,Request_data
from apps.helper.ConfigHelper import encoder_app
from main import PARAMS
from apps.models.LoanModel import Loan
# from apps.models.BorrowerModel import Borrower
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
    
    # @classmethod
    # def delete_cif(cls,loanid):
    #     result = BaseResponse()
    #     result.status = 400
    #     try:
    #         if loanid is not None:
    #                 data = Loan.where('loanid', '=', loanid).update({'deleted':1})
    #                 result.status = 200
    #                 result.message = "Success"
    #                 result.data = {"CIF": data}
    #                 Log.info(result.message)
    #         else:
    #                 e = "idno not found!"
    #                 Log.error(e)
    #                 result.status = 404
    #                 result.message = str(e)
    #     except Exception as e:
    #             Log.error(e)
    #             result.status = 400
    #             result.message = str(e)
    #     return result
    @classmethod
    def update_cif(cls,cif):
        result = BaseResponse()
        result.status = 400
        if cif is not None:
                data = Loan.where('cif', '=', cif).update({'deleted':2})
                result.status = 200
                result.message = "Success"
                result.data = {"CIF": data}
                Log.info(result.message)
        return result
            

                 
