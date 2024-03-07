from fastapi import FastAPI
from translate import translate_en2mn, translate_mn2en

app = FastAPI()

@app.get("/translate")
def get_translation(
    text: str,
    direction: str = 'en2mn'
):
    if direction == 'en2mn':
        result = translate_en2mn(text)
    elif direction == 'mn2en':
        result = translate_mn2en(text)
    else:
        Exception('The options are: mn2en, en2mn ')
    return {'result': result}