import cv2
import matplotlib.pyplot as plt

# 1. Path to your input image
img_path = 'test.png'

# 2. Load image and convert to RGB
image_bgr = cv2.imread(img_path)
if image_bgr is None:
    raise FileNotFoundError(f"Could not load image at {img_path}")
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

# 3. Define Gaussian blur parameters
kernel_size = (5, 5)
sigma_values = [0, 1, 2, 5]

# 4. Create subplots for original + blurred versions
fig, axes = plt.subplots(1, len(sigma_values) + 1, figsize=(16, 5))
axes[0].imshow(image_rgb)
axes[0].set_title("Original")
axes[0].axis("off")

for ax, sigma in zip(axes[1:], sigma_values):
    blurred = cv2.GaussianBlur(image_rgb, kernel_size, sigma)
    ax.imshow(blurred)
    ax.set_title(f"σ = {sigma}")
    ax.axis("off")

plt.tight_layout()

# 5. Save the figure as a PNG
output_path = 'test2.jpg'
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.show()
