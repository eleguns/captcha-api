from fastapi import FastAPI
from fastapi.responses import PlainTextResponse


app = FastAPI()

@app.get('/')
async def root():
    return PlainTextResponse('welcome !')