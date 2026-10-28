"""Chotu, the voice agent from Episode 1: ears (Whisper) -> brain (Claude) -> mouth (ElevenLabs)."""
import anthropic
import sounddevice as sd
import whisper
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play

RULES = """You are Chotu, the voice assistant on Pomato's support line.
Today's test order: #4821, two paneer rolls and a cold coffee from
Sharma's Kitchen, 340 rupees, rider Raju, arriving around 8:40 pm.
Help the caller with their order. You are on a phone call:
answer in one or two short sentences, no lists, no symbols."""

# --- the ears -------------------------------------------------------------
ears = whisper.load_model("turbo")       # downloads once (~1.5 GB)

def listen(seconds=5):
    print("Speak now...")
    sound = sd.rec(int(seconds * 16_000), samplerate=16_000,
                   channels=1, dtype="float32")
    sd.wait()                             # wait for the 5 seconds
    return ears.transcribe(sound.flatten())["text"].strip()

# --- the brain ------------------------------------------------------------
brain = anthropic.Anthropic()            # uses ANTHROPIC_API_KEY
history = []                             # everything said so far

def think(words):
    history.append({"role": "user", "content": words})
    answer = brain.messages.create(model="claude-haiku-5-5",
        max_tokens=1000, system=RULES, messages=history)
    reply = next(b.text for b in answer.content if b.type == "text")
    history.append({"role": "assistant", "content": reply})
    return reply

# --- the mouth ------------------------------------------------------------
mouth = ElevenLabs()                     # uses ELEVENLABS_API_KEY

def speak(reply):
    audio = mouth.text_to_speech.convert(text=reply,
        voice_id="JBFqnCBsd6RMkjVDRZzb", model_id="eleven_v4")
    play(audio)

# --- the loop -------------------------------------------------------------
if __name__ == "__main__":
    while True:
        input("Press Enter, then speak...")
        words = listen()
        print("Priya:", words)
        reply = think(words)
        print("Chotu:", reply)
        speak(reply)
