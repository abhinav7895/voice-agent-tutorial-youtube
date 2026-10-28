"""A cheat card for the ears: tell Whisper which words to expect, so paneer stays paneer."""
import whisper

ears = whisper.load_model("turbo")
HINT = "Pomato support. Sharma's Kitchen, paneer roll, cold coffee."

plain = ears.transcribe("priya.wav", language="en")["text"].strip()
hinted = ears.transcribe("priya.wav", language="en", initial_prompt=HINT)["text"].strip()
print("without a hint:", plain)
print("with a hint:   ", hinted)
