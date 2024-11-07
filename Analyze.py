import numpy as np
import matplotlib.pyplot as plt

# Function to load image files (.idx3-ubyte format)
def load_images(filename):
    with open(filename, 'rb') as f:
        f.read(4)  # skip the magic number
        num_images = int.from_bytes(f.read(4), 'big')
        num_rows = int.from_bytes(f.read(4), 'big')
        num_cols = int.from_bytes(f.read(4), 'big')
        images = np.frombuffer(f.read(), dtype=np.uint8).reshape(num_images, num_rows, num_cols)
    return images

# Function to load label files (.idx1-ubyte format)
def load_labels(filename):
    with open(filename, 'rb') as f:
        f.read(4)  # skip the magic number
        num_labels = int.from_bytes(f.read(4), 'big')
        labels = np.frombuffer(f.read(), dtype=np.uint8)
    return labels

# Load the training and test sets
train_images = load_images('/Users/ronitghai/train-images-idx3-ubyte')
train_labels = load_labels('/Users/ronitghai/train-labels-idx1-ubyte')
test_images = load_images('/Users/ronitghai/t10k-images-idx3-ubyte')
test_labels = load_labels('/Users/ronitghai/t10k-labels-idx1-ubyte')

# Display a few images from the training set
num_display = 10
fig, axes = plt.subplots(1, num_display, figsize=(15, 5))
for i in range(num_display):
    axes[i].imshow(train_images[i], cmap='gray')
    axes[i].set_title(f"Label: {train_labels[i]}")
    axes[i].axis('off')
plt.suptitle("Sample Images from Dataset with Labels")
plt.show()
