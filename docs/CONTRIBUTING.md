# Contributing to Velo

Velo is a proof of concept project, but it is structured so that a new contributor can pick up a piece of it without needing the full context in someone's head. This guide covers how to find something to work on, how the codebase is organized, and what is expected of a change before it is merged.

## Before you start

Read [`docs/architecture.md`](./docs/architecture.md) first. It explains why the pipeline is split into three modules and why each one currently raises `NotImplementedError`. Understanding that will save you from accidentally "fixing" something that is intentionally left incomplete.

## Where to find work

The project's current gaps are listed under "Not yet implemented" in the README, and each corresponding module has a TODO comment showing exactly what to uncomment and configure. Good first contributions:

- Connect the Whisper API in `core/transcriber.py`
- Connect the DeepL API in `core/translator.py`
- Connect gTTS audio generation in `core/synthesizer.py`
- Add microphone recording in the browser, in `index.html` and the frontend JS
- Improve error handling in `app.py`, particularly the broad `except Exception` in the `/api/translate` route

If you want to work on something not listed, open an issue first describing what you would like to change and why, so the scope is agreed on before you start.

## Project structure (quick reference)

```
├── app.py              # Flask app and API routes
├── core/
│   ├── transcriber.py  # Speech to text logic
│   ├── translator.py   # Translation logic
│   └── synthesizer.py  # Text to speech logic
├── docs/
│   ├── architecture.md # Why the system is structured this way
│   └── tutorial.md     # Step by step setup guide
├── index.html           # Landing page and prototype UI
├── requirements.txt
├── .env.example
└── CONTRIBUTING.md      # This file
```

## Coding conventions

- Keep functions small and single purpose. Each `core/` module should keep doing one job (transcribe, translate, or synthesize) and should not pick up cross cutting logic.
- Comment the non obvious, not the obvious. A one line comment explaining why a language code is mapped to an API specific format is useful. A comment restating what a line of code already says clearly is not.
- Keep the module boundary intact. `app.py` should only call the three public functions, `transcribe_audio`, `translate_text`, and `synthesize_speech`. It should never reach into a module's internals.
- Do not commit API keys. `.env` is gitignored for a reason. Only `.env.example`, with placeholder values, belongs in the repo.

## Making a change

1. Branch from `main`. Use a short, descriptive branch name, for example `feature/whisper-integration` or `fix/translate-error-handling`.
2. Write a clear commit message. Describe what changed and why, not just what file was touched, for example "Connect Whisper API in transcriber.py" rather than "update file."
3. Update the docs if behavior changes. If you wire up a new API or change an endpoint's expected input or output, update the relevant section of the README or `docs/` so the documentation does not drift from the code.
4. Open a pull request with a short description of what you implemented and any manual testing you did, since there is no automated test suite yet.

## Testing manually

There is no test suite yet, so changes should be manually verified against the API contract described in the README's "API overview" section. Specifically, confirm your change still returns the expected JSON shape (`transcript`, `translation`, `audio_url`) or a sensible error response.

## Adding a new language pair

If you are extending Velo beyond English and German, you will need to update the `LANGUAGE_MAP` in `core/translator.py` and `SUPPORTED_PAIRS` in `app.py`. Both are intentionally kept as simple dictionaries so this is a small, localized change rather than a structural one.

## Questions

Open an issue if anything here is unclear. As a small proof of concept project, the fastest way to improve this guide is for someone to hit a gap in it and flag it.
