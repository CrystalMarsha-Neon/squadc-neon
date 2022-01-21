from datetime import date
import json
from sqlite3 import Date
from fastapi import APIRouter, Query, Response
from apps.controllers.LoanController import ControllerLoan as loan
from apps.controllers.CrystalController import ControllerCrystal as crystalm

from typing import Optional
import datetime

router = APIRouter()
@router.post("/get_loan_by_loan_id")
async def get_loan_by_loan_id(response: Response,
        loanid: Optional[str]=Query(None),
        dob: Optional[date]=Query(None)):
    result = crystalm.get_loan_by_loan_id(loanid=loanid,dob=dob)
    response.status_code = result.status
    return result

# @router.delete("/delete_web_on_boarding")
# async def remove_web_on_boarding_data(response: Response,
#         loanid: Optional[str] = Query(None)):
#     result.status_code = result.status
#     return restult

@router.get("/get_biggest_loan")
async def get_biggest_loan(response: Response):
    result = crystalm.get_biggest_loan()
    response.status_code = result.status
    return result

@router.put("/update_cif")
async def update_cif(response: Response,
        cif: Optional[str]=Query(None)):
    result = crystalm.update_cif(cif=cif,updated_at=datetime.datetime.now)
    response.status_code = result.status
    return result

@router.delete("/delete_cif")
async def delete_cif(response: Response,
        cif: Optional[str]=Query(None)):
    result = crystalm.delete_cif(cif=cif,updated_at=datetime.datetime.now)
    response.status_code = result.status
    return result