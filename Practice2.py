#!/usr/bin/env python3
"""
gaussian_blur_prompt.py

Loads an image (default: test.png or one you specify), then asks you
to enter a Gaussian kernel size and sigma. Applies the blur and shows
original vs. blurred images side by side.
"""

import sys
from typing import Tuple

import cv2
import numpy as np
import matplotlib.pyplot as plt


def apply_gaussian_blur(
    image: np.ndarray,
    kernel_size: Tuple[int, int],
    sigma: float
) -> np.ndarray:
    kx, ky = kernel_size
    if kx % 2 == 0 or ky % 2 == 0 or kx < 1 or ky < 1:
        raise ValueError("kernel_size must be two odd integers > 1 (e.g. 5 5)")
    return cv2.GaussianBlur(image, (kx, ky), sigma)


def prompt_kernel() -> Tuple[int, int]:
    while True:
        raw = input("Enter kernel size (two odd integers, e.g. 5 5): ").strip().split()
        if len(raw) != 2:
            print("  ✗ Please enter exactly two numbers.")
            continue
        try:
            kx, ky = map(int, raw)
        except ValueError:
            print("  ✗ Both must be integers.")
            continue
        if kx < 1 or ky < 1 or kx % 2 == 0 or ky % 2 == 0:
            print("  ✗ Both must be odd and > 1.")
            continue
        return kx, ky


def prompt_sigma() -> float:
    while True:
        raw = input("Enter sigma (float, 0 for auto): ").strip()
        try:
            s = float(raw)
        except ValueError:
            print("  ✗ Please enter a valid number.")
            continue
        if s < 0:
            print("  ✗ Sigma cannot be negative.")
            continue
        return s


def main(img_path: str):
    # 1. Load image
    img_bgr = cv2.imread(img_path)
    if img_bgr is None:
        print(f"Error: could not load image at '{img_path}'", file=sys.stderr)
        sys.exit(1)

    # 2. Prompt for blur parameters
    print(f"Image loaded: '{img_path}'")
    kernel_size = prompt_kernel()
    sigma = prompt_sigma()

    # 3. Apply Gaussian blur
    blurred_bgr = apply_gaussian_blur(img_bgr, kernel_size, sigma)

    # 4. Convert to RGB for display
    img_rgb     = cv2.cvtColor(img_bgr,     cv2.COLOR_BGR2RGB)
    blurred_rgb = cv2.cvtColor(blurred_bgr, cv2.COLOR_BGR2RGB)

    # 5. Show side by side
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    axes[0].imshow(img_rgb)
    axes[0].set_title("Original")
    axes[0].axis("off")

    axes[1].imshow(blurred_rgb)
    axes[1].set_title(f"Blurred (kernel={kernel_size}, σ={sigma})")
    axes[1].axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Load an image and interactively apply Gaussian blur."
    )
    parser.add_argument(
        "image_path",
        nargs="?",
        default="test.png",
        help="Image filename in this folder (default: test.png)"
    )
    args = parser.parse_args()
    main(args.image_path)
