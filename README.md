Here's the rewritten README:

---

**Velo**
Realtime voice translation for getting through daily life without a language barrier slowing you down.

---

**What is this?**

I moved to Germany and found that not speaking fluent German creates constant friction. Calling the doctor, dealing with landlords, sitting through university events that switch language mid sentence. It adds up fast.

Velo is my attempt to reduce that friction. You speak in English, the person on the other end hears German and vice versa, as close to real time as possible.

This repo is a proof of concept built for my Technical Documentation module. The architecture is defined and the core pipeline is mapped out, but it is not production ready. Think of it as a working blueprint.

---

**How it works**

Speech → Whisper (speech to text) → DeepL (translation) → gTTS (text to speech) → audio output.

The pipeline runs in both directions. The other person speaks German, you hear English. It is three APIs composed into a single low latency flow.

---

**Tech stack**

| Layer | Tool | Reason |
|---|---|---|
| Backend | Python + Flask | Lightweight, minimal setup |
| Speech to text | OpenAI Whisper | Best accuracy I tested, handles background noise well |
| Translation | DeepL | More natural output than Google Translate for German and English |
| Text to speech | gTTS | Free and functional for a demo. Robotic but adequate |
| Frontend | HTML, CSS, JS | No build step needed for a concept demo |

---

**Project structure**

```
├── app.py              # Flask app and API routes
├── core/
│   ├── transcriber.py  # Speech to text (Whisper)
│   ├── translator.py   # Translation (DeepL)
│   └── synthesizer.py  # Text to speech (gTTS)
├── index.html          # Landing page
└── requirements.txt    # Dependencies
```

Each core module has documented TODOs marking exactly what needs to be wired up.

---

**Getting started**

```bash
git clone && cd velo
python -m venv venv && source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # Add your OpenAI and DeepL API keys (free tiers work)
python app.py
```

Open http://localhost:5000. You need an OpenAI key for Whisper and a DeepL key for translation.

---

**Current status**

Done:
- API architecture and endpoint design
- Scaffolded core modules with clear TODOs
- Landing page

Not yet implemented:
- Whisper, DeepL, and gTTS wiring
- Microphone capture via Web Audio API
- WebSocket support for real time streaming

---

**What comes next**

WebSockets — the current HTTP request/response cycle adds latency that would feel noticeable in a real conversation.

Whisper streaming — avoid waiting for a full sentence before translating.

Better TTS — ElevenLabs sounds significantly more natural than gTTS.

Twilio integration — extend to actual phone calls, not just in browser.

More language pairs — the architecture already supports it, just a matter of adding codes.

---

**Why "Velo"?**

Velo means fast. That is the point.

---

**License**

MIT
