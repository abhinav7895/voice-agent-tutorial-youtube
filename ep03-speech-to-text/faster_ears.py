"""faster-whisper: the same model rebuilt for speed. Still waits for the end."""
import time

from faster_whisper import WhisperModel

ears = WhisperModel("turbo", device="cpu", compute_type="int8")
start = time.perf_counter()
segments, info = ears.transcribe("priya.wav", language="en")
text = " ".join(s.text.strip() for s in segments)   # the work happens here
took = time.perf_counter() - start

print(text)
print(f"{info.duration:.1f} s of speech, took {took:.1f} s")
