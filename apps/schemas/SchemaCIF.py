from datetime import date
from pydantic import BaseModel
from typing import Optional, List


class RequestCIF(BaseModel):
    cif: str = None
    idno: str = None

class CIF(BaseModel):
    loanid: str = None
    loan_type: int = None
    loan_status: int = None
    loan_amount: int = None
    loan_tenure: int = None
    interest: int = None
    cif: str  = None
    idno: str = None
    fname: str = None
    lname: str = None
    dob: date = None
    gender: str = None
    marital_status: str = None
    income: int = None
    phone: str = None
    email: str = None
    isphoneverified: int = None
    isemailverified: int = None
    createdate: date = None
    updatedate: date = None
    source: str = None

class CustomerData_by_Idno(BaseModel):
    idno: str = None
    fname: str = None
    lname: str = None
    gender: str = None
    marital_status: str = None
    income: int = None
    loan_status: int = None
    loan_amount: int = None
    phone: str = None
    email: str = None
    source: str = None

class ResponseCIF(BaseModel):
    cif_list: List[CIF]

class ResponseIDNO(BaseModel):
    idno_list: List[CustomerData_by_Idno]

class Customer(BaseModel):
    idno : str = None
    fname : str = None
    lname : str = None
    dob : date = None
    # age : int = None  #database ga ada column age
    gender : str = None
    marital_status : str = None
    income : int = None
    phone : str = None
    email : str = None


class ResponseCustomer(BaseModel):
    customer : List[Customer]

class Request_data(BaseModel):
    fname : str = None
    lname : str = None
    dob : date = None

class loan_data(BaseModel):
    loanid: str = None
    loan_type: int = None
    loan_status: int = None
    loan_amount: int = None
    loan_tenure: int = None
    interest: int = None

class Response_name(BaseModel):
    data_loan: List[loan_data]