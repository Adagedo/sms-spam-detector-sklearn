from fastapi import Request, Response, APIRouter,HTTPException, status
from model.predictions import model
from schema import UserRequest, ResponseBody
from typing import List



router = APIRouter()

router.post("/sms", status_code=status.HTTP_201_CREATED, response_model=List[ResponseBody])
async def sendMessage(userRequest:UserRequest):
    
    try:
        print(userRequest)
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"{e}")
    
    return 
        