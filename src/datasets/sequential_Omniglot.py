import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
from torchvision.datasets import Omniglot

# Create the Omniglot dataset
omniglot_dataset = Omniglot(root='./data', background=True, download=True)

image = Image.open('data/omniglot-py/images_background/Armenian/character38/0064_08.png')
# Resize image to 28x28
image = image.resize((28, 28), Image.ANTIALIAS)
image = np.array(image)
# Flatten the image by concatenating rows (reshape to a 784-pixel sequence)
flattened_image = image.flatten()

offset = 5

# Create subplots to display the original image and the flattened sequence
fig, axes = plt.subplots(2, 1, figsize=(10, 5), gridspec_kw={'height_ratios': [4, 1]})

# Plot the original image
axes[0].imshow(image, cmap='gray')
axes[0].set_title("Original 28 $\\times$ 28 image", fontdict={"family": "Times New Roman", "size": 15})

# Highlight the second row of pixels in the original image
rect = patches.Rectangle((-0.5, -0.5 + offset), 28, 1, linewidth=1, edgecolor='r', facecolor='#ff000080')
axes[0].add_patch(rect)

# Plot the flattened sequence
axes[1].imshow(flattened_image.reshape(1, -1), cmap='gray', aspect='auto')
axes[1].set_title("Flattened 784-pixel sequence", fontdict={"family": "Times New Roman", "size": 15})

# Highlight the corresponding pixels in the 1D image
rect = patches.Rectangle((-0.5 + offset * 28, -0.5), 28, 10, linewidth=1, edgecolor='r', facecolor='#ff000080')
axes[1].add_patch(rect)

# Show 0 7 14 21 and 28 ticks
axes[0].set_xticks([0, 14, 27])
axes[0].set_yticks([0, 14, 27])

axes[1].get_yaxis().set_visible(False)

# Adjust spacing between subplots
plt.tight_layout()

# Save plot as pdf
plt.savefig('../../figures/sequential_Omniglot.pdf')

# Show the plot
plt.show()
