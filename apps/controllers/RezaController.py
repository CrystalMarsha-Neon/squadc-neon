from main import PARAMS
from apps.models import db
from apps.helper import Log
from datetime import datetime
from apps.schemas import BaseResponse
from apps.models.LoanModel import Loan
from apps.schemas.SchemaCIF import ResponseCIF
from apps.utils.randomizer import random_N_digit
from apps.models.BorrowerDataModel import Borrower

SALT = PARAMS.SALT.salt

class ControllerReza(object):
    @classmethod
    def get_total_by_feature(cls, gender, marital_status):
        result = BaseResponse()
        result.status = 400
        
        data = db.table('digital_lending_dataset').sum('loan_amount')
        
        if gender:
            loan = Loan.where('gender', '=', gender.title()) 
            data = str(loan.sum('loan_amount'))
       
        if marital_status:
            loan = loan.where('marital_status', '=', marital_status.title())
            data = str(loan.sum('loan_amount'))
        
        result.status = 200
        result.message = "Success"
        result.data = { "total_loan": data }
        Log.info(result.message)

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
            db.table('digital_lending_dataset').where('loanid', loanid).update(input_data)
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
            db.table('digital_lending_dataset').where('loanid', loanid).update({'deleted': 1})

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

        loanid = db.table('digital_lending_dataset').max('loanid') + 1
    
        input_data["loanid"] = loanid
        input_data["cif"] = random_N_digit(4, "cif")
        input_data["idno"] = random_N_digit(16, "idno")
        input_data["dob"] = datetime.strptime(input_data["dob"], "%m/%d/%Y").date()

        input_data["isphoneverified"] = 0
        input_data["isemailverified"] = 0     
        input_data["createdate"] = datetime.strptime(datetime.today().strftime('%m/%d/%Y'), "%m/%d/%Y").date()
        input_data["updatedate"] = input_data["createdate"]

        input_data["source"] = "Web On Boarding"

        db.table('digital_lending_dataset').insert(input_data)
        result.status = 200
        result.message = "Success"
        result.data = ResponseCIF(**{"cif_list": [input_data]})

        return result    
    
    @classmethod
    def get_loan_by_borrowercif(cls, cif: int):
        result = BaseResponse()
        result.status = 400

        if cif is not None:
            data =  Borrower.find(cif).loans.serialize()
            result.status = 200
            result.message = "Success"
            result.data = data

        else:
            e = "cif not found!"
            Log.error(e)
            result.status = 404
            result.message = str(e)

        return result
