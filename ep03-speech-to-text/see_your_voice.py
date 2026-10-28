"""See your voice the way Whisper does: low pitches at the bottom, high at the top, bright = loud."""
import matplotlib.pyplot as plt
import whisper

audio = whisper.load_audio("priya.wav")             # 16,000 numbers a second
picture = whisper.log_mel_spectrogram(audio)        # the sound picture
plt.imshow(picture.numpy(), origin="lower", aspect="auto")
plt.xlabel("time"); plt.ylabel("pitch")
plt.show()
