from google.cloud import translate_v2 as translate
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

def translate_text(text, target_language):
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language=target_language)
    return result['translatedText']

if __name__ == "__main__":
    text_to_translate = "Hello World!"
    target_language = "es"
    translated_text = translate_text(text_to_translate, target_language)
    print(f"Translated text: {translated_text}")