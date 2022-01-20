import json
from typing import Optional
from fastapi import APIRouter, Body, Query, Response
from apps.controllers.RifkiController import ControllerRifki as Rifki

router = APIRouter()

example_input_idno = json.dumps({
    "idno": "681286",
}, indent=2)

@router.post("/get_loan_by_idno")
async def get_loan_by_idno(response: Response, input_data=Body(..., example=example_input_idno)):
    result = Rifki.get_loan_by_idno(input_data=input_data)
    response.status_code = result.status
    return result

@router.get("/get_loan_type_activate")
async def get_loan_type_activate(response: Response, 
            loan_type: Optional[str]=Query(None, example="1/2/3")):
    result = Rifki.get_loan_type_activate(loan_type)
    response.status_code = result.status
    return result