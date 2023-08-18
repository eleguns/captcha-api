from captcha.image import ImageCaptcha
from io import BytesIO

def captcha_generator(text: str):
    img = ImageCaptcha(width = 280, height = 90)
    data = img.generate(text)
    s = BytesIO()
    img.write(text, s)
    return s