import json
from fastapi import APIRouter, Body, Response
from apps.controllers.LoanController import ControllerLoan as loan
from apps.controllers.HensonController import ControllerHenson as henson

router = APIRouter()

example_input_idno = json.dumps({
    "idno": "1",
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

@router.delete("/delete_something")
async def delete_something():
    pass

@router.put("/put_something")
async def put_something():
    pass