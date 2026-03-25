### Velo

Real time voice translation for people who just want to live their life without a language barrier getting in the way.


## What is this?

So I moved to Germany and quickly realised that not speaking German fluently creates a lot of friction in daily life. Calling the doctor, dealing with landlords, sitting in a university event thats half in German....it adds up.

Velo is my attempt to solve that, at least partially. The idea is simple: you speak in English, the person on the other end hears it in German, and vice versa. As close to real time as possible.

This repo is a proof of concept built for my Technical Documentation module. Its not production ready, but the architecture is there and the core pipeline is mapped out. Think of it as a blueprint.


## How it works

Your voice goes into Whisper (speech to text), the transcript gets sent to DeepL (translation), and the result gets converted back to audio via gTTS (text to speech). The other person hears the translated version. Then it works the same way in reverse.

Its not magic, its just three APIs duct taped together in a way that hopefully feels seamless.


## Tech stack

Backend is Python with Flask because its lightweight and I didnt want to overcomplicate it. Speech to text is handled by OpenAI Whisper which has by far the best accuracy Ive tested, especially with background noise. Translation goes through DeepL because it produces more natural output than Google Translate for German/English specifically. Text to speech is gTTS for now- its free and gets the job done for a demo, though it does sound a bit robotic.

The frontend is plain HTML, CSS and JS. No React, no build step, nothing fancy.


## Project structure

app.py is the Flask app and where all the API routes live. The core folder has three files: transcriber.py handles speech to text, translator.py handles translation, and synthesizer.py handles text to speech. Each one has a documented TODO showing exactly what needs to be wired up. index.html is the landing page. requirements.txt has everything you need to install.


## Getting started

Clone the repo and cd into it. Create a virtual environment with python -m venv venv and activate it. Install dependencies with pip install -r requirements.txt. Copy .env.example to .env and add your API keys -- you need an OpenAI key for Whisper and a DeepL key for translation (free tier works fine). Then run python app.py and open http://localhost:5000.


## Current status

The architecture is fully defined and the API endpoints are designed. The core modules are scaffolded with clear TODOs so its obvious what needs to be implemented next. The landing page is done. What isnt done yet: actually wiring up Whisper, DeepL and gTTS, the frontend microphone capture via Web Audio API, and WebSocket support for proper real-time streaming.


## What I would do next

Switch from HTTP to WebSockets -- the current request/response setup adds latency that would feel annoying in a real conversation. Get Whisper streaming working so it doesnt have to wait for a full sentence before translating. Upgrade the TTS voice -- gTTS is fine for a demo but ElevenLabs sounds much more natural. Add Twilio integration so it works on actual phone calls, not just in-browser. Support more language pairs -- the architecture already handles it, its just a matter of adding the codes.


## Why Velo?

Velo means fast. Thats the whole point.


## Notes

This was built for my Technical Documentation class as a semester project. I kept the code intentionally simple and readable, the goal was to show the concept and the architecture clearly, not to build something shippable.


License

MIT
