import json
from fastapi import APIRouter, Body, Response
from apps.controllers.LoanController import ControllerLoan as loan

router = APIRouter()
example_input_cifno = json.dumps({
    "cif": "1",
}, indent=2)

example_input_idno = json.dumps({
    "idno": "1",
}, indent=2)

@router.post("/get_customer")
async def get_customer(response: Response, input_data=Body(..., example=example_input_idno)):
    result = loan.get_customer(input_data=input_data)
    response.status_code = result.status
    return result

