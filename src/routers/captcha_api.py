from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from src.utils import captcha_generator
from io import BytesIO

router = APIRouter()

@router.get('/captcha', tags=['captcha'])
def captcha_api(text: str):
    data = captcha_generator(text)
    return StreamingResponse(BytesIO(data.getvalue()), media_type='image/png')