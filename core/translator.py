"""
Translation module.
Wraps the DeepL API. Can be swapped for Google Translate, LibreTranslate, etc.
"""

# import deepl
# import os

# deepl wants uppercase codes ("EN"/"DE"), rest of the app uses lowercase, hence this map
LANGUAGE_MAP = {
    "en": "EN",
    "de": "DE",
}


def translate_text(text: str, source: str = "en", target: str = "de") -> str:
    """
    Translate text from source to target language.

    Args:
        text   : input text
        source : ISO 639-1 source language code
        target : ISO 639-1 target language code

    Returns:
        str : translated text

    TODO: uncomment and configure below
        translator = deepl.Translator(os.environ["DEEPL_API_KEY"])
        result = translator.translate_text(
            text,
            source_lang=LANGUAGE_MAP[source],
            target_lang=LANGUAGE_MAP[target],
        )
        return result.text
    """
    raise NotImplementedError("DeepL integration pending.")
