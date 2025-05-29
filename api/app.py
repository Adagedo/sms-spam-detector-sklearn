from fastapi import Request, Response, APIRouter
from model.predictions import model



router = APIRouter()

router.post("/sms")
async def sendMessage(messages):
    
    return ""