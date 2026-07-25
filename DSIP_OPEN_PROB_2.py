import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve
import soundfile as sf

audio_path = r"C:\Users\PV shreyan\Videos\Projects\MCI INTRO.mp3"

# Samples will be float32 array normalized between -1.0 and 1.0
samples, sample_rate = sf.read (audio_path, dtype = 'float32')

# If stereo (2 channels), convert to mono (1 cahnnel) by averaging channels
if samples.ndim > 1:
    samples = samples.mean(axis = 1)

# Define multiple convolution kernels (Impulse Responses)
kernels = {
    "Custom_Alternating": np.array ([1, 0, 1, 0, 1], dtype = np.float32),
    "Low_Pass_Smoothing": np.ones (15, dtype = np.float32) / 15,
    "High_Pass_Sharpening": np.array ([-1, -1, -1, 8, -1, -1, -1], dtype = np.float32)
}

# Normalize original samples for plotting
samples_norm = samples / np.max (np.abs (samples)) 

plt.figure (figsize = (12, 8))
plt.subplot (len (kernels) + 1, 1, 1)
plt.plot (samples_norm, color = 'blue')
plt.title ("Original Audio Signal")

plot_index = 2

for kernel_name, kernel in kernels.items():
    print (f"Processing with {kernel_name} kernel...")
    
    # Perform convolution
    convoluted = convolve (samples, kernel, mode='same')
    
    # Normalize output to [-1, 1] range
    convoluted_normalized = convoluted / np.max (np.abs (convoluted))
    
    # Export directly to WAV using soundfile
    output_filename = f"output_{kernel_name}.wav"
    sf.write (output_filename, convoluted_normalized, sample_rate)
    print (f"Convoluted audio saved as '{output_filename}'.")
    
    # Plot convoluted signals
    plt.subplot (len (kernels) + 1, 1, plot_index)
    plt.plot (convoluted_normalized, color = 'red')
    plt.title (f"Convoluted Audio Signal with {kernel_name} Kernel")
    plot_index += 1

plt.tight_layout()
plt.show()