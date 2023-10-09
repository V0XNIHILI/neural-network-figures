import matplotlib.pyplot as plt
import numpy as np

STEPS = 16

steps_plus_one = STEPS + 1

# Generate data for the staircase plot
x_staircase = np.linspace(0, 1, num=steps_plus_one)
y_staircase = np.linspace(0, 1, num=steps_plus_one)

# Generate data for the logarithmic staircase plot
x_log_staircase = 1/2**np.linspace(0, STEPS, num=steps_plus_one)[::-1]
y_log_staircase = 1/2**np.linspace(0, STEPS, num=steps_plus_one)[::-1]

print(np.linspace(0, STEPS, num=steps_plus_one))

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(6, 3), sharey=True)

# Left subplot (staircase plot)
axs[0].step(x_staircase, y_staircase, where='post', color='b')
axs[0].plot([0, 1], [0, 1], 'k--', color='gray')
axs[0].set_title('Uniform quantization')
axs[0].set_xlabel('x')
axs[0].set_ylabel('$\\hat{x}$')
axs[0].set_xlim(0, 1)
axs[0].set_ylim(0, 1)

# Right subplot (logarithmic staircase plot)
axs[1].step(x_log_staircase, y_log_staircase, where='post', color='r')
axs[1].plot([0, 1], [0, 1], 'k--', color='gray')
axs[1].set_title('Logarithmic quantization')
axs[1].set_xlabel('x')
axs[1].set_xlim(0, 1)
axs[1].set_ylim(0, 1)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()

# Save the plot
fig.savefig('../../figures/quantization_steps.pdf')