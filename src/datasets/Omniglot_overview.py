import os
import random
import matplotlib.pyplot as plt
from PIL import Image

plt.rcParams["font.family"] = "Times New Roman"

# Replace with the path to your Omniglot dataset directory
omniglot_dir = './data/omniglot-py/images_background/'

# List of alphabet names in the Omniglot dataset
alphabet_names = os.listdir(omniglot_dir)

# Number of examples to show for each alphabet
num_examples = 5
max_alphabets = 8

alphabet_names = ["Armenian", "Hebrew", "Cyrillic", "Korean", "Japanese_(katakana)", "Braille", "Gujarati", "Arcadian", "Sanskrit", "Futurama"]

# Create a figure and axis
fig, axes = plt.subplots(num_examples, len(alphabet_names), figsize=(10, 3))

# Iterate over each alphabet
for i, alphabet in enumerate(alphabet_names):
    alphabet_dir = os.path.join(omniglot_dir, alphabet)
    characters = os.listdir(alphabet_dir)
    characters = random.sample(characters, num_examples)  # Randomly select characters

    # Iterate over selected characters for the alphabet
    for j, character in enumerate(characters):
        character_dir = os.path.join(alphabet_dir, character)
        example_image_path = os.path.join(character_dir, random.choice(os.listdir(character_dir)))

        # Load and display the example image
        image = Image.open(example_image_path)
        axes[j, i].imshow(image, cmap='gray')
        axes[j, i].axis('off')

# Set alphabet names at the bottom of the plot
for i, alphabet in enumerate(alphabet_names):
    alphabet = alphabet.replace('_', ' ').replace(' (katakana)', '')
    axes[num_examples - 1, i].text(0.5, -1, alphabet, fontsize=12, ha='center', transform=axes[num_examples - 1, i].transAxes)

# Adjust layout and save the plot
plt.tight_layout()
plt.savefig('../../figures/Omniglot_overview.pdf')
plt.show()
