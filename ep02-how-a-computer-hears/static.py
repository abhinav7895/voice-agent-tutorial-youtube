"""Why static: read Priya's 2-byte samples one byte at a time. Turn your volume down first!"""
import numpy as np
import sounddevice as sd

raw_bytes = open("priya.raw", "rb").read()

wrong = np.frombuffer(raw_bytes, dtype=np.int8)    # 1 byte each: the mistake
right = np.frombuffer(raw_bytes, dtype=np.int16)   # 2 bytes each: the truth
print(len(wrong), "samples (wrong) vs", len(right), "(right)")

print("turn your volume down! static first...")
sd.play(wrong, 16_000); sd.wait()
print("...then Priya")
sd.play(right, 16_000); sd.wait()
