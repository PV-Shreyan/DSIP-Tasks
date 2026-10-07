import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from scipy.signal import correlate

original_path = r"C:\Users\PV shreyan\Videos\Projects\Young and Beautiful(MP3_160K).mp3"
karaoke_path  = r"C:\Users\PV shreyan\Videos\Projects\Lana Del Rey - Young And Beautiful (Karaoke Version)(MP3_160K).mp3"
different_path = r"C:\Users\PV shreyan\Videos\Projects\🍂 [Copyright Free Chill Background Music] - _Way Home_ by _tokyowalker4038   🇯🇵(MP3_160K).mp3"

frames_to_read = 44100 * 10 
original_audio, _ = sf.read (original_path, frames = frames_to_read, always_2d = True)
karaoke_audio, _ = sf.read (karaoke_path, frames = frames_to_read, always_2d = True)
different_audio, _ = sf.read (different_path, frames = frames_to_read, always_2d = True)

# Mix left and right channels together
original_mono = original_audio.mean (axis = 1)
karaoke_mono = karaoke_audio.mean (axis = 1)
different_mono = different_audio.mean (axis = 1)

# COMPARE THE SONGS (CROSS-CORRELATION)
print ("Comparing Original vs Karaoke")
correlation_karaoke = correlate (original_mono, karaoke_mono, mode = 'same', method = 'fft')

print ("Comparing Original vs Different Song")
correlation_different = correlate (original_mono, different_mono, mode = 'same', method = 'fft')

# DISPLAY RESULT
plt.figure (figsize = (10, 6))

plt.subplot (2, 1, 1)
plt.plot (correlation_karaoke, color = 'blue')
plt.title ("Similarity: Original vs Karaoke")

plt.subplot (2, 1, 2)
plt.plot (correlation_different, color = 'red')
plt.title ("Similarity: Original vs Different Song")

plt.tight_layout()
plt.show()