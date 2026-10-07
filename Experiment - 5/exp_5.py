import numpy as np
import matplotlib.pyplot as plt

def compute_fft (signal):
    # Compute the FFT of the signal
    fft_result = np.fft.fft (signal)
    return fft_result

def compute_ifft (fft_result):
    # Compute the IFFT of the FFT result
    reconstructed_signal = np.fft.ifft (fft_result)
    return reconstructed_signal

# Define the discrete-time signal (8 points -> N = 2^3, fits radix-2 DIT-FFT)
signal = np.array ([1, 2, 3, 4, 5, 6, 7, 8])

# Compute the FFT
fft_result = compute_fft (signal)

# Compute the magnitude and phase spectrum of the FFT result
magnitude_spectrum = np.abs (fft_result)
phase_spectrum = np.angle (fft_result)

# Compute the IFFT of the FFT result (reconstruct original signal)
reconstructed_signal = compute_ifft (fft_result)

plt.figure (figsize = (10, 9))

plt.subplot (4, 1, 1)
plt.stem (signal)
plt.title ('Original Discrete-Time Signal x(n)')
plt.xlabel ('n')
plt.ylabel ('Amplitude')

plt.subplot (4, 1, 2)
plt.stem (magnitude_spectrum)
plt.title ('Magnitude Spectrum |X(k)| (FFT)')
plt.xlabel ('Frequency index k')
plt.ylabel ('Magnitude')

plt.subplot (4, 1, 3)
plt.stem (phase_spectrum)
plt.title ('Phase Spectrum (FFT)')
plt.xlabel ('Frequency index k')
plt.ylabel ('Phase (radians)')

plt.subplot (4, 1, 4)
plt.stem (reconstructed_signal.real)
plt.title ('Reconstructed Signal (IFFT)')
plt.xlabel ('n')
plt.ylabel ('Amplitude')

plt.tight_layout ()
plt.show ()

print ("Original signal:", signal)
print ("FFT result:", fft_result)
print ("Magnitude spectrum:", magnitude_spectrum)
print ("Phase spectrum:", phase_spectrum)
print ("Reconstructed signal:", reconstructed_signal.real)