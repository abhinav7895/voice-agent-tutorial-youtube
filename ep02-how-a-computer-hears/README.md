# Episode 2: How a computer hears

Sound, inside a computer, is a long list of numbers. These scripts let you see that, and hear the two classic
mistakes: the wrong speed (a chipmunk or a monster) and the wrong number size (static).

```bash
pip install -r requirements.txt
python record.py        # say "where's my order?": prints the numbers, saves priya.wav
python play.py          # the same recording at the real speed, half speed, double speed
python static.py        # the same bytes read 1 byte at a time (static), then 2 (Priya)
```

`chotu_mouth_fix.py` is the one-number fix for Chotu's chipmunk voice (needs `ELEVENLABS_API_KEY`).

Tip: if every number is 0, your laptop hasn't allowed the microphone yet. Check its privacy settings.
