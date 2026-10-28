"""Live ears with Deepgram: send 20 ms slices while you talk; pencil guesses come back, then ink.
Needs DEEPGRAM_API_KEY. Press Ctrl+C to stop."""
import queue
import threading

import sounddevice as sd
from deepgram import DeepgramClient
from deepgram.core.events import EventType
from deepgram.listen.v1.types import ListenV1Results

RATE, FRAME = 16_000, 320          # 320 samples = 20 ms
LANGUAGE = "en-IN"                 # "multi" for Hindi + English in one sentence
frames = queue.Queue()             # a waiting line for frames
notepad = []                       # ink pieces of this turn

def on_mic(indata, n, time, status):
    frames.put(bytes(indata))      # 640 bytes per frame

def on_message(msg):
    if not isinstance(msg, ListenV1Results) or not msg.channel.alternatives:
        return
    text = msg.channel.alternatives[0].transcript
    if msg.is_final and text:                     # ink: never changes
        notepad.append(text)
        print("[ink]   ", " ".join(notepad))
    elif text:                                    # pencil: a live guess
        print("[pencil]", " ".join(notepad + [text]))
    if msg.speech_final and notepad:              # she paused: turn over
        print("[turn over] ->", " ".join(notepad))
        notepad.clear()

client = DeepgramClient()          # reads DEEPGRAM_API_KEY
with client.listen.v1.connect(model="nova-3", language=LANGUAGE,
        encoding="linear16", sample_rate=RATE, channels=1,
        interim_results=True, endpointing=300,
        smart_format=True,
        keyterm=["paneer roll", "cold coffee", "Sharma's Kitchen", "Pomato"]) as line:
    line.on(EventType.MESSAGE, on_message)
    threading.Thread(target=line.start_listening, daemon=True).start()
    print("Talk! (Ctrl+C to stop)")
    with sd.RawInputStream(samplerate=RATE, blocksize=FRAME,
            channels=1, dtype="int16", callback=on_mic):
        try:
            while True:
                line.send_media(frames.get())   # one 20 ms frame
        except KeyboardInterrupt:
            pass
