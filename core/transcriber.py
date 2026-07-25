"""
Speech to Text module.
Wraps OpenAI Whisper. Swap the implementation here without touching the rest of the app.
"""

# import openai
# import os


def transcribe_audio(audio_file, language: str = "en") -> str:
    """
    Transcribe audio to text.

    Args:
        audio_file : file-like object (wav, mp3, webm)
        language   : ISO 639-1 language code hint

    Returns:
        str : transcribed text

    TODO: uncomment and configure below
        client = openai.OpenAI(api_key=os.environ["OPENAI_API_KEY"])
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            language=language,
        )
        return transcript.text
    """
    # passing the language hint so whisper skips auto-detection, faster on short clips
    raise NotImplementedError("Whisper integration pending.")
