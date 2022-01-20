from datetime import date
from apps.helper import Log
from apps.schemas import BaseResponse
from apps.schemas.SchemaCIF import RequestCIF, ResponseCIF
from apps.helper.ConfigHelper import encoder_app
from main import PARAMS
from apps.models.LoanModel import Loan
from apps.models import db
from datetime import datetime
from apps.utils.helper import random_N_digit

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
    def get_loan(cls, loanid: int):
        result = BaseResponse()
        result.status = 400

        if loanid is not None:
            data = Loan.where('loanid', '=', loanid).get().serialize()
            result.status = 200
            result.message = "Success"
            result.data = ResponseCIF(**{"cif_list": data})

        else:
            e = "cif not found!"
            Log.error(e)
            result.status = 404
            result.message = str(e)

        return result        

    @classmethod
    def update_loan(cls, loanid: int, input_data=None):
        result = BaseResponse()
        result.status = 400

        if loanid is not None:
            #loan = Loan.find(loanid)
            db.table('lendings').where('loanid', loanid).update(input_data)
            data = Loan.where('loanid', '=', loanid).get().serialize()

            result.status = 200
            result.message = "Success"
            result.data = ResponseCIF(**{"cif_list": data})

        else:
            e = "cif not found!"
            Log.error(e)
            result.status = 404
            result.message = str(e)

        return result

    @classmethod
    def delete_loan(cls, loanid: int):
        result = BaseResponse()
        result.status = 400

        if loanid is not None:
            #loan = Loan.find(loanid)
            db.table('lendings').where('loanid', loanid).update({'deleted': 1})

            result.status = 200
            result.message = "Success"

        else:
            e = "cif not found!"
            Log.error(e)
            result.status = 404
            result.message = str(e)

        return result

    @classmethod
    def create_loan(cls, input_data=None):
        result = BaseResponse()
        result.status = 400

        loanid = db.table('lendings').max('loanid') + 1
    
        input_data["loanid"] = loanid
        input_data["cif"] = random_N_digit(4, "cif")
        input_data["idno"] = random_N_digit(16, "idno")
        input_data["dob"] = datetime.strptime(input_data["dob"], "%m/%d/%Y").date()

        input_data["isphoneverified"] = 0
        input_data["isemailverified"] = 0     
        input_data["createdate"] = datetime.strptime(datetime.today().strftime('%m/%d/%Y'), "%m/%d/%Y").date()
        input_data["updatedate"] = input_data["createdate"]

        input_data["source"] = "Web On Boarding"

        db.table('lendings').insert(input_data)
        result.status = 200
        result.message = "Success"
        result.data = ResponseCIF(**{"cif_list": [input_data]})

        return result                   