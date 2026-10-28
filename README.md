# Voice AI for absolute beginners: the code

Code for the YouTube series **Voice AI for absolute beginners** by [Abhinav Yadav](https://abhinavyadav.in).
Every episode improves **Chotu**, the voice agent for Pomato, a made-up food delivery app.

| Episode | Folder | What you build |
|---|---|---|
| 1 · Build your first AI voice agent | [`ep01-first-voice-agent`](ep01-first-voice-agent) | Chotu: ears (Whisper) → brain (Claude) → mouth (ElevenLabs), and a timer for each step |
| 2 · How a computer hears | [`ep02-how-a-computer-hears`](ep02-how-a-computer-hears) | Record your voice as numbers, play it at the wrong speed, make static on purpose |
| 3 · Speech-to-text | [`ep03-speech-to-text`](ep03-speech-to-text) | Whisper on your laptop, see your voice as a picture, live ears with pencil and ink |

More folders arrive with each new video.

## Setup

You need Python 3.10 or newer, and a microphone. Each folder has its own `requirements.txt`:

```bash
cd ep01-first-voice-agent
python -m venv .venv && source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Whisper also needs **ffmpeg** (`brew install ffmpeg` on a Mac, `sudo apt install ffmpeg` on Linux).

API keys go in environment variables (copy `.env.example`, fill it in, then `export` them or use your shell's
tool of choice): `ANTHROPIC_API_KEY` (Episode 1), `ELEVENLABS_API_KEY` (Episodes 1 and 2),
`DEEPGRAM_API_KEY` (Episode 3, live ears). Episodes 2 and 3 mostly run free, with no keys.

## A note on model names and libraries

AI libraries change quickly. If a model name or function stops working, check the library's own docs; the
idea in each video stays the same. Issues and fixes are welcome.

## License

MIT
