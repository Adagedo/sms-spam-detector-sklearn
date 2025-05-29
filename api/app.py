from fastapi import FastAPI, Request, Response

app = FastAPI()

@app.get("/")
async def root():
    return "server is running..."

#create the api here