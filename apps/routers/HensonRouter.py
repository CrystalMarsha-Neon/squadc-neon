from dis import Bytecode
import json
from fastapi import APIRouter, Body, Response
from apps.controllers.LoanController import ControllerLoan as loan
from apps.controllers.HensonController import ControllerHenson as henson

router = APIRouter()

example_input_idno_income = json.dumps({
    "idno": "1",
    "income": "1"
}, indent=2)

example_input_cif = json.dumps({
    "cif": "1",
}, indent=2)

example_input_idno = json.dumps({
    "idno": "1",
}, indent=2)

example_input_loanid = json.dumps({
    "loanid": "1",
}, indent=2)

@router.post("/get_customer_by_idno")
async def get_customer_by_idno(response: Response, input_data=Body(..., example=example_input_idno)):
    result = henson.get_customer(input_data=input_data)
    response.status_code = result.status
    return result

@router.get("/total_entry")
async def total_entry(response: Response):
    result = henson.total_entry()
    response.status_code = result.status
    return result

@router.delete("/delete_entry")
async def delete_entry(response: Response, input_data=Body(..., example=example_input_loanid)):
    result = henson.delete_entry(input_data=input_data)
    response.status_code = result.status
    return result

@router.put("/update_income")
async def update_income(response: Response, input_data=Body(..., example=example_input_idno_income)):
    result = henson.update_income(input_data=input_data)
    response.status_code = result.status
    return result    
    # pass