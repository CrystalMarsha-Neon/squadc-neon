import json
from fastapi import APIRouter, Query, Response
from apps.controllers.RezaController import ControllerReza as reza
from typing import Optional

router = APIRouter()

@router.get("/get_total_by_feature") 
async def get_total_by_feature(response: Response, 
            gender: Optional[str]=Query(None, example="Male/Female"),
            marital_status: Optional[str]=Query(None, example="Single/Married")):
    result = reza.get_total_by_feature(gender=gender, marital_status=marital_status)
    response.status_code = result.status
    return result