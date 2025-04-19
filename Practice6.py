#!/usr/bin/env python3
"""
iterative_gaussian_blur.py

Loads an image, applies Gaussian blur iteratively, and shows
the original plus each blurred iteration side by side.
"""

import cv2
import matplotlib.pyplot as plt

def main(
    img_path: str = 'test.png',
    kernel_size: tuple[int, int] = (5, 5),
    sigma: float = 1.0,
    num_iterations: int = 5
):
    # 1. Load image
    img_bgr = cv2.imread(img_path)
    if img_bgr is None:
        raise FileNotFoundError(f"Could not load image at '{img_path}'")
    # 2. Convert to RGB
    img = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    # 3. Iteratively blur
    images = [img]
    for i in range(num_iterations):
        images.append(
            cv2.GaussianBlur(images[-1], kernel_size, sigma)
        )

    # 4. Plot original + each iteration
    fig, axes = plt.subplots(1, num_iterations + 1, figsize=(4*(num_iterations+1), 5))
    for idx, ax in enumerate(axes):
        ax.imshow(images[idx])
        ax.set_title("Original" if idx == 0 else f"Iter {idx}")
        ax.axis("off")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Apply Gaussian blur iteratively and plot each step."
    )
    parser.add_argument(
        "image_path",
        nargs="?",
        default="test.png",
        help="Path to image file (default: test.png)"
    )
    parser.add_argument(
        "--kernel", "-k",
        type=int,
        nargs=2,
        default=(5, 5),
        metavar=("KX","KY"),
        help="Gaussian kernel size (odd ints), e.g. --kernel 5 5"
    )
    parser.add_argument(
        "--sigma", "-s",
        type=float,
        default=1.0,
        help="Sigma (standard deviation) for blur (default: 1.0)"
    )
    parser.add_argument(
        "--iters", "-n",
        type=int,
        default=5,
        help="Number of blur iterations (default: 5)"
    )
    args = parser.parse_args()

    main(
        img_path       = args.image_path,
        kernel_size    = tuple(args.kernel),
        sigma          = args.sigma,
        num_iterations = args.iters
    )
