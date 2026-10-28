"""Record 3 seconds of your voice and look at it as numbers. Saves priya.wav (with a label) and priya.raw (without)."""
import wave

import sounddevice as sd

RATE = 16_000            # samples every second
SECONDS = 3

print("Say: where's my order?")
sound = sd.rec(SECONDS * RATE, samplerate=RATE,
               channels=1, dtype="int16")   # 2-byte whole numbers
sd.wait()
sound = sound.flatten()

print(sound[:10])                # the first 10 samples
print(len(sound), "samples")     # 16,000 a second x 3 seconds

raw_bytes = sound.tobytes()
with open("priya.raw", "wb") as f:          # just the numbers, no label
    f.write(raw_bytes)
with wave.open("priya.wav", "wb") as f:     # the same numbers + a label
    f.setnchannels(1)                       # one voice
    f.setsampwidth(2)                       # 2 bytes per sample
    f.setframerate(RATE)                    # 16,000 a second
    f.writeframes(raw_bytes)
print("saved priya.wav and priya.raw")
