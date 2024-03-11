from fastapi import FastAPI
from translate import translate_en2mn, translate_mn2en
from pydantic import BaseModel

app = FastAPI()

class Input(BaseModel):
    text: str

@app.post("/translate/english-to-mongolian")
def get_translation_en2mn(
    input: Input
):
    result = translate_en2mn(input.text)
    return {'result': result}

@app.post("/translate/mongolian-to-english")
def get_translation(
    input: Input
):
    result = translate_mn2en(input.text)
    return {'result': result}