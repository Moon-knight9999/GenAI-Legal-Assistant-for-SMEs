from langdetect import detect
from transformers import MarianTokenizer, MarianMTModel

MODEL_NAME = "Helsinki-NLP/opus-mt-hi-en"

tokenizer = MarianTokenizer.from_pretrained(MODEL_NAME)
model = MarianMTModel.from_pretrained(MODEL_NAME)

def translate_hi_to_en(text: str) -> str:
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    translated = model.generate(**inputs, max_length=512)
    return tokenizer.decode(translated[0], skip_special_tokens=True)

def normalize(text: str) -> str:
    try:
        if detect(text) == "hi":
            return translate_hi_to_en(text)
        return text
    except Exception:
        # Fail-safe: never crash Streamlit
        return text
