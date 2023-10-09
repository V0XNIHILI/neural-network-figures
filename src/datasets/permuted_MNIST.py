import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

from torchvision.datasets import MNIST

mnist_dataset = MNIST(root="./data/", download=True)

image = mnist_dataset.data[0]

# Resize image to 28x28
# image = image.resize((28, 28), Image.ANTIALIAS)
image = np.array(image)
# Flatten the image by concatenating rows (reshape to a 784-pixel sequence)
flattened_image = image.flatten()

offset = 7

# Permute the pixels in the flattened image at random
np.random.seed(0)

perm = np.random.permutation(784)
flattened_image = flattened_image[np.random.permutation(784)]

plt.suptitle("Original 28 $\\times$ 28 images", fontdict={"family": "Times New Roman"}, size=15)

# Placing the plots in the plane
plot1 = plt.subplot2grid((4, 2), (0, 0), colspan=1, rowspan=2) #left top
plot2 = plt.subplot2grid((4, 2), (0, 1), rowspan=2, colspan=1) # right top
plot3 = plt.subplot2grid((4, 2), (2, 0), colspan=2) #up
plot4 = plt.subplot2grid((4, 2), (3, 0), colspan=2) # bottom

axes = [plot1, plot2, plot3, plot4]

# Create subplots to display the original image and the flattened sequence
# fig, axes = plt.subplots(2, 1, figsize=(10, 5), gridspec_kw={'height_ratios': [4, 1]})

# Plot the original image
axes[0].imshow(image, cmap='gray')
# axes[0].set_title("Original 28x28 image", fontdict={"family": "Times New Roman", "size": 15})

# Highlight the second row of pixels in the original image
rect = patches.Rectangle((-0.5, -0.5 + offset), 28, 1, linewidth=1, edgecolor='r', facecolor='#ff000080')
axes[0].add_patch(rect)

# Plot the flattened sequence
axes[2].imshow(flattened_image.reshape(1, -1), cmap='gray', aspect='auto')
axes[2].set_title("Flattened 784-pixel sequences", fontdict={"family": "Times New Roman", "size": 15})

for i, value in enumerate(perm):
    if value >= 28*offset and value < 28*(offset+1):
        # Highlight the corresponding pixels in the 1D image
        rect = patches.Rectangle((-0.5 + i, -0.5), 1, 10, linewidth=1, edgecolor='r', facecolor='#ff000080')
        axes[2].add_patch(rect)

axes[2].axis('off')

# Show 0 7 14 21 and 28 ticks
axes[0].set_xticks([0, 14, 27])
axes[0].set_yticks([0, 14, 27])

axes[2].get_yaxis().set_visible(False)

image = mnist_dataset.data[1]

# Resize image to 28x28
# image = image.resize((28, 28), Image.ANTIALIAS)
image = np.array(image)
# Flatten the image by concatenating rows (reshape to a 784-pixel sequence)
flattened_image = image.flatten()

# Plot the original image
axes[1].imshow(image, cmap='gray')
# axes[1].set_title("Original 28x28 image", fontdict={"family": "Times New Roman", "size": 15})

# Highlight the second row of pixels in the original image
rect = patches.Rectangle((-0.5, -0.5 + offset), 28, 1, linewidth=1, edgecolor='royalblue', facecolor='#0000ff80')
axes[1].add_patch(rect)

# Plot the flattened sequence
axes[3].imshow(flattened_image.reshape(1, -1), cmap='gray', aspect='auto')
# axes[3].set_title("Flattened 784-pixel sequence", fontdict={"family": "Times New Roman", "size": 15})

for i, value in enumerate(perm):
    if value >= 28*offset and value < 28*(offset+1):
        # Highlight the corresponding pixels in the 1D image
        rect = patches.Rectangle((-0.5 + i, -0.5), 1, 10, linewidth=1, edgecolor='royalblue', facecolor='#0000ff80')
        axes[3].add_patch(rect)

# Show 0 7 14 21 and 28 ticks
axes[1].set_xticks([0, 14, 27])
axes[1].set_yticks([0, 14, 27])

axes[3].get_yaxis().set_visible(False)
# Adjust spacing between subplots
plt.tight_layout()

# Save plot as pdf
plt.savefig('../../figures/sequential_MNIST.pdf', bbox_inches='tight', pad_inches=0)

# Show the plot
plt.show()
