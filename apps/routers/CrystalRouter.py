from datetime import date
import json
from sqlite3 import Date
from fastapi import APIRouter, Query, Response
from apps.controllers.LoanController import ControllerLoan as loan
from typing import Optional

router = APIRouter()
@router.post("/get_loan_by_name")
async def get_loan_by_name(response: Response,
        fname: Optional[str]=Query(None),
        lname: Optional[str]=Query(None),
        dob: Optional[date]=Query(None)):
    result = loan.get_loan_by_name(fname=fname,lname=lname,dob=dob)
    response.status_code = result.status
    return result