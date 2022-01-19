from apps.helper import Log
from apps.schemas import BaseResponse
from main import PARAMS
from apps.models.LoanModel import Loan
from apps.models import db

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
    