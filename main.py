from fastapi import FastAPI, Response
from api.app import router

app = FastAPI()



app.include_router(router=router)


@app.get("/")
async def root():
    return "server is running"

    
