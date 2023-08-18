from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from src.routers import captcha_router

app = FastAPI()
app.include_router(captcha_router)

@app.get('/')
def root():
    return PlainTextResponse('welcome !')