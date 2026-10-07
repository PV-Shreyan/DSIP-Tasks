import numpy as np
import matplotlib.pyplot as plt

signal = ([1, 5, 2, 6, 3, 7, 4, 8])

# Compute the FFT of the signal
fft_result = np.fft.fft (signal)

# Compute the magnitude and phase spectrum of the FFT result
magnitude_spectrum = np.abs (fft_result) # np.absolute
phase_spectrum = np.angle (fft_result)

# Compute IFFT of the FFT result
ifft_result = np.real(np.fft.ifft (fft_result)) 

sample_index = np.arange(len(signal))

plt.figure (figsize = (12, 8))

plt.subplot (2, 2, 1)
plt.stem (sample_index, signal)
plt.title ("Original Signal")
plt.xlabel ("Sample Index")
plt.ylabel ("Amplitude")
plt.grid (True)

plt.subplot (2, 2, 2)
plt.stem (sample_index, magnitude_spectrum)
plt.title ("Magnitude Spectrum")
plt.xlabel ("Sample Index")
plt.ylabel ("Magnitude")
plt.grid (True)

plt.subplot (2, 2, 3)
plt.stem (sample_index, phase_spectrum)
plt.title ("Phase Spectrum")
plt.xlabel ("Sample Index")
plt.ylabel ("Phase")
plt.grid (True)

plt.subplot (2, 2, 4)
plt.stem (sample_index, ifft_result)
plt.title ("IFFT Signal")
plt.xlabel ("Sample Index")
plt.ylabel ("Amplitude")
plt.grid (True)

plt.tight_layout()
plt.show()