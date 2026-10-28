"""Record 3 seconds as priya.wav, at the 16,000 samples a second that Whisper wants."""
import sounddevice as sd
import soundfile as sf

RATE, SECONDS = 16_000, 3
print("Say: two paneer rolls and a cold coffee")
sound = sd.rec(SECONDS * RATE, samplerate=RATE, channels=1, dtype="float32")
sd.wait()
sf.write("priya.wav", sound, RATE)
print("saved priya.wav")
