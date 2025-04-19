# Apply Gaussian blur to an image with a kernel size of (5,5). Show the original and blurred image side by side.
import cv2
import matplotlib.pyplot as plt

# Path to your image file
img_path = 'test.png'  # change this to your image

# 1. Read the image (in BGR color space)
image_bgr = cv2.imread(img_path)
if image_bgr is None:
    raise FileNotFoundError(f"Could not load image at {img_path}")

# 2. Convert to RGB for correct plotting
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

# 3. Apply Gaussian blur with a 5×5 kernel
kernel_size = (5, 5)
sigma = 0  # 0 means sigma is calculated from kernel size
blurred_rgb = cv2.GaussianBlur(image_rgb, kernel_size, sigma)

# 4. Display side by side using Matplotlib
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].imshow(image_rgb)
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(blurred_rgb)
axes[1].set_title(f'Gaussian Blurred ({kernel_size[0]}×{kernel_size[1]})')
axes[1].axis('off')

plt.tight_layout()
plt.show()
