from flask import Flask, request, jsonify, send_from_directory
from core.transcriber import transcribe_audio
from core.translator import translate_text
from core.synthesizer import synthesize_speech

app = Flask(__name__)

SUPPORTED_PAIRS = {
    "en-de": ("English", "German"),
    "de-en": ("German", "English"),
}


@app.route("/")
def index():
    return send_from_directory('.', 'index.html')


@app.route("/api/translate", methods=["POST"])
def translate():
    audio_file = request.files.get("audio")
    source_lang = request.form.get("source", "en")
    target_lang = request.form.get("target", "de")

    if not audio_file:
        return jsonify({"error": "No audio file provided"}), 400

    try:
        transcript = transcribe_audio(audio_file, language=source_lang)
        translation = translate_text(transcript, source=source_lang, target=target_lang)
        audio_url = synthesize_speech(translation, language=target_lang)

        return jsonify({
            "transcript": transcript,
            "translation": translation,
            "audio_url": audio_url,
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/languages", methods=["GET"])
def languages():
    return jsonify({"pairs": SUPPORTED_PAIRS})


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "version": "0.1.0-poc"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
