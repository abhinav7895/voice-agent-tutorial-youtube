"""Chotu's mouth asking ElevenLabs for raw samples, and the one-number fix for the chipmunk voice."""
import numpy as np
import sounddevice as sd
from elevenlabs.client import ElevenLabs

mouth = ElevenLabs()                     # uses ELEVENLABS_API_KEY
reply = "Your two paneer rolls and cold coffee are on the way with Raju!"

audio = mouth.text_to_speech.convert(text=reply,
    voice_id="JBFqnCBsd6RMkjVDRZzb", model_id="eleven_v4",
    output_format="pcm_24000")       # raw samples, 24,000 a second
samples = np.frombuffer(b"".join(audio), dtype=np.int16)

print("before: the wrong speed (a chipmunk)")
sd.play(samples, 48_000); sd.wait()
print("after: the real speed")
sd.play(samples, 24_000); sd.wait()
