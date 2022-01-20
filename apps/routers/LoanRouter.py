import json
from fastapi import APIRouter, Body, Response
from apps.controllers.LoanController import ControllerLoan as loan

router = APIRouter()

example_input_cifno = json.dumps({
    "cif": "1",
}, indent=2)

example_input_ = json.dumps({
    "loan_type": "1/2/3",
    "loan_status": "1/2",
    "loan_amount": "11,000,000",
    "loan_tenure": "24",
    "interest": "12",
    "fname": "reza",
    "lname": "habibi",
    "dob": "mm/dd/yyyy",
    "gender": "Female/Male",
    "marital_status": "Single/Married",
    "income": "22,000,000",
    "phone": "333-4444-22",
    "email": "r.habibi@ymail.com",
}, indent=2)

@router.post("/get_loan_by_cif")
async def get_loan_by_cif(response: Response, input_data=Body(..., example=example_input_cifno)):
    result = loan.get_loan_by_cif(input_data=input_data)
    response.status_code = result.status
    return result

@router.post("/get_loan_by_cif_debug")
async def get_loan_by_cif_debug(response: Response, input_data=Body(..., example=example_input_cifno)):
    result = loan.get_loan_by_cif_debug(input_data=input_data)
    response.status_code = result.status
    return result

@router.get("/loan/{loanid}")
async def get_loan(response: Response, loanid: int):
    result = loan.get_loan(loanid=loanid)
    response.status_code = result.status
    return result

@router.post("/loan")
async def create_loan(response: Response, input_data=Body(..., example=example_input_)):
    result = loan.create_loan(input_data=input_data)
    response.status_code = result.status
    return result

@router.put("/loan/{loanid}")
async def update_loan(response: Response, loanid: int, input_data=Body(..., example=example_input_)):
    result = loan.update_loan(loanid=loanid, input_data=input_data)
    response.status_code = result.status
    return result

@router.delete("/loan/{loanid}")
async def delete_loan(response: Response, loanid: int):
    result = loan.delete_loan(loanid=loanid)
    response.status_code = result.status
    return result