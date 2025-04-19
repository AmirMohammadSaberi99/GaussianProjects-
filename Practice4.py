#!/usr/bin/env python3
"""
interactive_roi_blur.py

Loads `test.png` (or a file you specify), asks you for an ROI via console input,
applies a Gaussian blur to that ROI, and displays original vs. ROI‑blurred images.
"""

import sys
from typing import Tuple

import cv2
import numpy as np
import matplotlib.pyplot as plt


def apply_gaussian_blur(
    image: np.ndarray,
    kernel_size: Tuple[int, int] = (15, 15),
    sigma: float = 0
) -> np.ndarray:
    kx, ky = kernel_size
    if kx % 2 == 0 or ky % 2 == 0 or kx < 1 or ky < 1:
        raise ValueError("kernel_size must be odd integers > 1, e.g. (15,15)")
    return cv2.GaussianBlur(image, (kx, ky), sigma)


def prompt_roi(img_width: int, img_height: int) -> Tuple[int, int, int, int]:
    """
    Ask the user to type x, y, w, h and return them as integers.
    Performs a simple sanity check against image bounds.
    """
    while True:
        raw = input(
            f"Enter ROI as four integers x y w h (within 0≤x<{img_width}, 0≤y<{img_height}):\n> "
        )
        parts = raw.strip().split()
        if len(parts) != 4:
            print("  ✗ Please enter exactly four values.")
            continue

        try:
            x, y, w_roi, h_roi = map(int, parts)
        except ValueError:
            print("  ✗ All four must be integers.")
            continue

        if (
            x < 0 or y < 0 or
            w_roi <= 0 or h_roi <= 0 or
            x + w_roi > img_width or
            y + h_roi > img_height
        ):
            print("  ✗ ROI out of bounds or non‑positive. Try again.")
            continue

        return x, y, w_roi, h_roi


def main(
    img_path: str,
    kernel_size: Tuple[int, int],
    sigma: float
):
    # 1. Load image
    img_bgr = cv2.imread(img_path)
    if img_bgr is None:
        print(f"ERROR: Could not open '{img_path}'", file=sys.stderr)
        sys.exit(1)

    # 2. Convert for display
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    h, w = img_rgb.shape[:2]

    # 3. Prompt the user for ROI
    print(f"Image loaded: {img_path} (width={w}, height={h})")
    x, y, w_roi, h_roi = prompt_roi(w, h)

    # 4. Extract, blur, and re‑insert ROI
    region = img_rgb[y : y + h_roi, x : x + w_roi]
    blurred_region = apply_gaussian_blur(region, kernel_size, sigma)
    output = img_rgb.copy()
    output[y : y + h_roi, x : x + w_roi] = blurred_region

    # 5. Display
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    ax1.imshow(img_rgb)
    ax1.set_title("Original")
    ax1.axis("off")

    ax2.imshow(output)
    ax2.set_title(
        f"ROI Blurred\n(x={x},y={y},w={w_roi},h={h_roi})\n"
        f"kernel={kernel_size}, σ={sigma}"
    )
    ax2.axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Interactively blur an ROI in an image."
    )
    parser.add_argument(
        "image_path",
        nargs="?",
        default="test.png",
        help="Image filename in this folder (default: test.png)"
    )
    parser.add_argument(
        "--kernel", "-k",
        type=int, nargs=2, default=(15, 15),
        metavar=("KX","KY"),
        help="Gaussian kernel size (odd ints), default=15 15"
    )
    parser.add_argument(
        "--sigma", "-s",
        type=float, default=0,
        help="Sigma for blur; 0 = auto‑calc, default=0"
    )
    args = parser.parse_args()

    main(
        img_path    = args.image_path,
        kernel_size = tuple(args.kernel),
        sigma       = args.sigma
    )
