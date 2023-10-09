import numpy as np
import matplotlib.pyplot as plt

plt.style.use('tableau-colorblind10')

# Define the range of x values
x_values = np.linspace(-2, 5, 400)

# Define the clamp bounds
a = 1
c = 3

def clamp(x, a, c):
    if x < a:
        return a
    elif x > c:
        return c
    else:
        return x

# Calculate the clamp values for each x
clamp_values = [clamp(x, a, c) for x in x_values]

# Create the plot
plt.figure(figsize=(5, 3))
plt.plot(x_values, clamp_values, label=f'clamp(x; {a}, {c})')
plt.axvline(x=a, color='r', linestyle='--', label=f'a = {a}')
plt.axvline(x=c, color='g', linestyle='--', label=f'c = {c}')
plt.xlabel('$x$')
plt.ylabel('$x_{int}$')
plt.legend()
plt.grid(True)
plt.tight_layout()

# let y-axis start at 0
plt.ylim(0, 4)

# Save the plot
plt.savefig('../../figures/clamp.pdf')

plt.show()
