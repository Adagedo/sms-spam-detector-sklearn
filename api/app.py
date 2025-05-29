from fastapi import Request, Response, APIRouter,HTTPException, status
from model.predictions import model
from api.schema import UserRequest, ResponseBody
from typing import List



router = APIRouter()

@router.post("/sms", status_code=status.HTTP_201_CREATED, response_model=ResponseBody)
async def sendMessage(userRequest:UserRequest):
    
    try:
        message:str = userRequest.message
        if message == None or message == "":
            raise HTTPException(status_code=status.HTTP_411_LENGTH_REQUIRED, detail="message can not be None or of length zero")
        models_prediction, score= model(message=message)
        print(models_prediction)
        response = {
            "msgtype":models_prediction, 
            "sender":userRequest.user,
            "models_score":score
        }
        
        return response
    
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"{e}")
    
        