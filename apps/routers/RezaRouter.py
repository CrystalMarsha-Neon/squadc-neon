import json
from typing import Optional
from fastapi import APIRouter, Body, Query, Response
from apps.controllers.RezaController import ControllerReza as reza

router = APIRouter()

example_input_ = json.dumps({
    "loan_type": "1",
    "loan_status": "2",
    "loan_amount": "11000000",
    "loan_tenure": "24",
    "interest": "12",
    "fname": "reza",
    "lname": "habibi",
    "dob": "10/08/1996",
    "gender": "Male",
    "marital_status": "Married",
    "income": "22000000",
    "phone": "333-4444-22",
    "email": "r.habibi@ymail.com",
}, indent=2)

@router.get("/get_total_by_feature") 
async def get_total_by_feature(response: Response, 
            gender: Optional[str]=Query(None, example="Male/Female"),
            marital_status: Optional[str]=Query(None, example="Single/Married")):
    result = reza.get_total_by_feature(gender=gender, marital_status=marital_status)
    response.status_code = result.status
    return result

@router.get("/loan/{loanid}")
async def get_loan(response: Response, loanid: int):
    result = reza.get_loan(loanid=loanid)
    response.status_code = result.status
    return result

@router.post("/loan")
async def create_loan(response: Response, input_data=Body(..., example=example_input_)):
    result = reza.create_loan(input_data=input_data)
    response.status_code = result.status
    return result

@router.put("/loan/{loanid}")
async def update_loan(response: Response, loanid: int, input_data=Body(..., example=example_input_)):
    result = reza.update_loan(loanid=loanid, input_data=input_data)
    response.status_code = result.status
    return result

@router.delete("/loan/{loanid}")
async def delete_loan(response: Response, loanid: int):
    result = reza.delete_loan(loanid=loanid)
    response.status_code = result.status
    return result    