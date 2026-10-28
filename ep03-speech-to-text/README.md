# Episode 3: Speech-to-text

Chotu's ears. Whisper reads a 30-second page after you finish; live ears write words while you talk.

```bash
pip install -r requirements.txt
python record.py            # records priya.wav (3 seconds)
python whisper_ears.py      # Whisper on your laptop, timed
python faster_ears.py       # faster-whisper: the same model, quicker
python see_your_voice.py    # the sound picture Whisper reads
python whisper_hint.py      # a cheat card for tricky words like paneer
export DEEPGRAM_API_KEY=...
python live_ears.py         # live: pencil guesses, then ink, while you talk (Ctrl+C to stop)
```

Live ears use [Deepgram](https://deepgram.com) (paid per minute, with free credit to start). Set
`LANGUAGE = "multi"` in `live_ears.py` for callers who mix Hindi and English.
