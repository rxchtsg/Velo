"""
Text-to-Speech module.
Uses gTTS (Google Text-to-Speech) -- free, no API key needed.
Can be upgraded to ElevenLabs for more natural voices.
"""

import os
import uuid

# from gtts import gTTS

OUTPUT_DIR = "static/audio"


def synthesize_speech(text: str, language: str = "de") -> str:
    """
    Convert text to speech and save as audio file.

    Args:
        text     : text to synthesize
        language : target language code

    Returns:
        str : URL path to the generated audio file

    TODO: uncomment and configure below
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        filename = f"{uuid.uuid4().hex}.mp3"
        filepath = os.path.join(OUTPUT_DIR, filename)
        tts = gTTS(text=text, lang=language)
        tts.save(filepath)
        return f"/static/audio/{filename}"
    """
    # uuid4 avoids filename clashes if two people translate at the same time
    raise NotImplementedError("gTTS integration pending.")
