# Episode 1: Build your first AI voice agent

Chotu listens with Whisper, thinks with Claude, and talks with ElevenLabs.

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=...  ELEVENLABS_API_KEY=...
python chotu.py           # press Enter, speak for 5 seconds, hear Chotu answer
python chotu_timed.py     # the same, printing how long each step takes
```

- The first run downloads the Whisper model (about 1.5 GB).
- ElevenLabs' `play()` needs `mpv` or `ffmpeg` installed to play the audio.
- Try it yourself: change the test order in `RULES` and see if Chotu keeps up.
