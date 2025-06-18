from googletrans import Translator

# Create a Translator instance that we'll reuse
translator = Translator()

def translate_text(text, target_lang="en"):
    try:
        # Attempt to translate the given text to the target language
        translated = translator.translate(text, dest=target_lang)
        return translated.text
    except Exception as e:
        # In case something goes wrong with the translation API
        print(f" Translation failed: {e}")
        return "[Translation Error]"
