from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class UserRequest(BaseModel):
    
    user:str
    message:str 
    sent_at:Optional[datetime]=datetime.utcnow()
    

class ResponseBody(BaseModel):
    
    msgtype:str
    sender:str
    
    
    