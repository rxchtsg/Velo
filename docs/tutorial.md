# Getting Started with Velo

This is a step by step tutorial for getting Velo running locally. It assumes you have Python 3.9 or later installed and are comfortable using a terminal, but no prior knowledge of Flask, Whisper, DeepL, or gTTS.

By the end of this tutorial, you will have Velo running locally, understand what happens when you call its one real endpoint, and know why the translation call itself will not produce real output yet.

## Step 1: Clone the repository

```bash
git clone https://github.com/rxchtsg/Velo.git
cd Velo
```

You should now have a folder containing `app.py`, a `core/` folder, and this `docs/` folder among other files.

## Step 2: Create a virtual environment

A virtual environment keeps Velo's dependencies separate from other Python projects on your machine.

```bash
python -m venv venv
source venv/bin/activate
```

On Windows, activate it with:

```bash
venv\Scripts\activate
```

You will know it worked if your terminal prompt now starts with `(venv)`.

## Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

This installs Flask and the other packages Velo's backend needs.

## Step 4: Set up environment variables

Velo expects two API keys, one for Whisper (speech to text) and one for DeepL (translation), even though the calls to these services are currently stubbed out. Step 6 explains why.

```bash
cp .env.example .env
```

Open `.env` in a text editor and fill in:

```
OPENAI_API_KEY=your_openai_key_here
DEEPL_API_KEY=your_deepl_key_here
```

If you do not have keys yet, you can leave these blank. The app will still start, since these values are not read until the real API calls are uncommented in `core/transcriber.py` and `core/translator.py`.

## Step 5: Run the app

```bash
python app.py
```

You should see Flask start up and confirm it is running on port 5000. Open this in your browser:

```
http://localhost:5000
```

You should see the Velo landing page.

## Step 6: Try the API and understand what happens

Send a request to the health check endpoint to confirm the server is alive:

```bash
curl http://localhost:5000/api/health
```

Expected response:

```json
{"status": "ok", "version": "0.1.0-poc"}
```

Now try the translation endpoint itself:

```bash
curl -X POST http://localhost:5000/api/translate \
  -F "audio=@path/to/any/audio/file.wav" \
  -F "source=en" \
  -F "target=de"
```

This will return a 500 error with a message like "Whisper integration pending." That is expected, not a bug. Open `core/transcriber.py` and you will see the real Whisper call written out but commented out, with `raise NotImplementedError(...)` left in its place. The same is true for `core/translator.py` and `core/synthesizer.py`. This lets you run and inspect the full request path without needing live API keys, while making it clear exactly what is left to connect.

## Step 7: Where to go next

- To understand why the code is structured this way, read [`docs/architecture.md`](./architecture.md).
- To pick up one of the open TODOs, such as wiring up Whisper, DeepL, or gTTS, see [`CONTRIBUTING.md`](../CONTRIBUTING.md).

## Troubleshooting

**ModuleNotFoundError on startup.** Your virtual environment likely is not activated. Re-run the `source venv/bin/activate` command from Step 2.

**Port 5000 already in use.** Another process is using that port, which is common on macOS, where AirPlay Receiver uses 5000 by default. Either stop that process or change the port in the last line of `app.py`.

**.env values not taking effect.** Make sure you copied `.env.example` to a file literally named `.env`, not `.env.example`, and restart the server after editing it.
