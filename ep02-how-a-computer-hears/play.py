"""Play the same numbers at three speeds: real, half (a monster) and double (a chipmunk)."""
import wave

import numpy as np
import sounddevice as sd

with wave.open("priya.wav", "rb") as f:     # the label tells us the rate
    RATE = f.getframerate()
    sound = np.frombuffer(f.readframes(f.getnframes()), dtype=np.int16)

for name, rate in [("real voice", RATE), ("half speed: a monster", RATE // 2),
                   ("double speed: a chipmunk", RATE * 2)]:
    print(name)
    sd.play(sound, rate); sd.wait()
