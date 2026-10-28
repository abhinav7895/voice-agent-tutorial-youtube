"""Whisper on your laptop: accurate, but it waits for the whole recording."""
import time

import whisper

ears = whisper.load_model("turbo")       # downloads once
start = time.perf_counter()
result = ears.transcribe("priya.wav", language="en")
took = time.perf_counter() - start

print(result["text"].strip())
print(f"took {took:.1f} s, after she had already stopped")
