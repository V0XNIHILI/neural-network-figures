import matplotlib.pyplot as plt
import numpy as np

STEPS_LEFT = 4
STEPS_RIGHT = 16

num_steps_left = STEPS_LEFT - 1
num_steps_right = STEPS_RIGHT - 1

# Generate data for the staircase plot
x_staircase = np.linspace(0, 1, num=num_steps_left)
y_staircase = np.linspace(0, 1, num=num_steps_left)

# Generate data for the logarithmic staircase plot
x_log_staircase = np.linspace(0, 1, num=num_steps_right)
y_log_staircase = np.linspace(0, 1, num=num_steps_right)

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(6, 3), sharey=True)

# Left subplot (staircase plot)
axs[0].step(x_staircase, STEPS_RIGHT*y_staircase, where='post', color='b')
axs[0].plot([0, 1], [0, STEPS_RIGHT], 'k--', color='gray')
axs[0].set_title(f'$s=\\frac{{1}}{{{STEPS_LEFT}}}$')
axs[0].set_xlabel('$x$')
axs[0].set_ylabel('$x_{int}$')
axs[0].set_xlim(0, 1)
axs[0].set_ylim(0, STEPS_RIGHT)

# Make y-labels ints
from matplotlib.ticker import MaxNLocator
axs[0].yaxis.set_major_locator(MaxNLocator(integer=True))

# Right subplot (logarithmic staircase plot)
axs[1].step(x_log_staircase, STEPS_RIGHT*y_log_staircase, where='post', color='r')
axs[1].plot([0, 1], [0, STEPS_RIGHT], 'k--', color='gray')
axs[1].set_title(f'$s=\\frac{{1}}{{{STEPS_RIGHT}}}$')
axs[1].set_xlabel('$x$')
axs[1].set_xlim(0, 1)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()

# Save the plot
fig.savefig('../../figures/quantization_step_size.pdf')