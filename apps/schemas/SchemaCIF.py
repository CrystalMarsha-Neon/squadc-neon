from datetime import date
from pydantic import BaseModel
from typing import Optional, List


class RequestCIF(BaseModel):
    loan_type: int = None
    loan_status: int = None
    loan_amount: str = None
    loan_tenure: int = None
    interest: int = None
    cif: int = None
    idno: str = None
    fname: str = None
    lname: str = None
    dob: date = None
    gender: str = None
    marital_status: str = None
    income: str = None
    phone: str = None
    email: str = None
    isphoneverified: int = None
    isemailverified: int = None
    createdate: date = None
    updatedate: date = None
    source: str = None

class CIF(BaseModel):
    loanid: int = None
    loan_type: int = None
    loan_status: int = None
    loan_amount: str = None
    loan_tenure: int = None
    interest: int = None
    cif: int = None
    idno: str = None
    fname: str = None
    lname: str = None
    dob: date = None
    gender: str = None
    marital_status: str = None
    income: str = None
    phone: str = None
    email: str = None
    isphoneverified: int = None
    isemailverified: int = None
    createdate: date = None
    updatedate: date = None
    source: str = None

class ResponseCIF(BaseModel):
    cif_list: List[CIF]