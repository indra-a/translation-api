from transformers import AutoModelForSeq2SeqLM, NllbTokenizer

tokenizer_en2mn = NllbTokenizer.from_pretrained("tokenizer_en2mn/")
tokenizer_mn2en = NllbTokenizer.from_pretrained("tokenizer_mn2en/")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-600M")

def translate_mn2en(text, tokenizer_mn2en=tokenizer_mn2en, model=model):
    inputs = tokenizer_mn2en(text, return_tensors="pt")
    translated_tokens = model.generate(**inputs, forced_bos_token_id = tokenizer_mn2en.lang_code_to_id['eng_Latn'])
    return tokenizer_mn2en.batch_decode(translated_tokens, skip_special_tokens = True)

def translate_en2mn(text, tokenizer_en2mn=tokenizer_en2mn, model=model):
    inputs = tokenizer_en2mn(text, return_tensors="pt")
    translated_tokens = model.generate(**inputs, forced_bos_token_id = tokenizer_en2mn.lang_code_to_id['khk_Cyrl'])
    return tokenizer_en2mn.batch_decode(translated_tokens, skip_special_tokens = True)