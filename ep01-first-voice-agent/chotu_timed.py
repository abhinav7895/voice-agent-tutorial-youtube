"""Episode 1's timer: the same Chotu, printing how long the ears, brain and mouth each take."""
import time

from elevenlabs.play import play

from chotu import listen, mouth, think

def make_voice(reply):
    # join the pieces so the timer measures the whole voice being made
    return b"".join(mouth.text_to_speech.convert(text=reply,
        voice_id="JBFqnCBsd6RMkjVDRZzb", model_id="eleven_v4"))

while True:
    input("Press Enter, then speak...")
    t0 = time.perf_counter()
    words = listen();          t1 = time.perf_counter()
    reply = think(words);      t2 = time.perf_counter()
    audio = make_voice(reply); t3 = time.perf_counter()
    print(f"ears {t1-t0:.1f}s  brain {t2-t1:.1f}s  mouth {t3-t2:.1f}s")
    print("Chotu:", reply)
    play(audio)
