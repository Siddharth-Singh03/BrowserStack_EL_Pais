
from googletrans import Translator

translator = Translator()

def translate_text(text, target_lang="en"):
    try:
        translated = translator.translate(text, dest=target_lang)
        return translated.text
    except Exception as e:
        print(f"❌ Translation failed: {e}")
        return "[Translation Error]"
