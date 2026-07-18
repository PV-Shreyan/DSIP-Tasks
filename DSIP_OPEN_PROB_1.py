import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# Define the discrete-time functions
# ---------------------------------------------------------

def u(n):
    """Discrete-time unit step function"""
    return np.where (n >= 0, 1.0, 0.0)

def delta(n):
    """Discrete-time unit impulse function"""
    return np.where (n == 0, 1.0, 0.0)

# ---------------------------------------------------------
# Define the discrete-time signals
# ---------------------------------------------------------

# Signal 1: Alternating sequence of 2 and 3
n1 = np.arange (-3, 7)
# For odd 'n' the value is 2. For even 'n' the value is 3.
x1 = np.where (n1 % 2 != 0, 2.0, 3.0)

# Signal 2: Trapezoidal step sequence
n2 = np.arange (0, 8)
x2 = np.array ([0, 1, 2, 3, 3, 2, 1, 0])

# Signal 3: Bounded ramp sequence
n3 = np.arange (-3, 4)
# Values grow linearly as 2n between -1 and 1, bounded at -2 and 2
x3 = np.clip (2 * n3, -2.0, 2.0)

# Signal 4: x[n] = u(n) - u(n-3) - 5u(n-7)
n4 = np.arange (-2, 10)
x4 = u(n4) - u(n4 - 3) - 5 * u(n4 - 7)

# Signal 5: x[n] = delta(n) + 3*delta(n-1) + 5*delta(n+1)
n5 = np.arange (-3, 4)
x5 = delta(n5) + 3 * delta(n5 - 1) + 5 * delta(n5 + 1)

# ---------------------------------------------------------
# Plot the signals
# ---------------------------------------------------------
plt.figure (figsize = (12, 10))

# Plot Signal 1
plt.subplot (3, 2, 1)
plt.stem (n1, x1)
plt.title ('Signal 1: Alternating Sequence')
plt.xlabel ('n')
plt.ylabel ('x[n]')
plt.grid (True, linestyle = '--', alpha = 0.6)

# Plot Signal 2 
# (Using step plot to match the zero-order hold drawing style from the image)
plt.subplot (3, 2, 2)
plt.step (n2, x2, where = 'post', color = 'b', linewidth = 2)
plt.title ('Signal 2: Trapezoidal Sequence')
plt.xlabel ('n')
plt.ylabel ('x[n]')
plt.grid (True, linestyle = '--', alpha = 0.6)

# Plot Signal 3
# (Using standard plot to match the linear interpolation style from the image)
plt.subplot (3, 2, 3)
plt.plot (n3, x3, color='r', marker='o')
plt.title ('Signal 3: Bounded Ramp')
plt.xlabel ('n')
plt.ylabel ('x[n]')
plt.grid (True, linestyle = '--', alpha = 0.6)

# Plot Signal 4
plt.subplot (3, 2, 4)
plt.stem (n4, x4)
plt.title ('Signal 4: $x[n] = u(n) - u(n-3) - 5u(n-7)$')
plt.xlabel ('n')
plt.ylabel ('x[n]')
plt.grid (True, linestyle = '--', alpha = 0.6)

# Plot Signal 5
plt.subplot (3, 2, 5)
plt.stem (n5, x5)
plt.title ('Signal 5: $x[n] = \delta(n) + 3\delta(n-1) + 5\delta(n+1)$')
plt.xlabel ('n')
plt.ylabel ('x[n]')
plt.grid (True, linestyle = '--', alpha = 0.6)

plt.tight_layout()
plt.show()