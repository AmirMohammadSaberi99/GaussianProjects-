#!/usr/bin/env python3
"""
realtime_gaussian_blur.py

Capture webcam video, apply Gaussian blur to each frame, and display
original vs. blurred in real time.
"""

import cv2
import argparse

def main(
    kernel_size: tuple[int, int] = (15, 15),
    sigma: float = 100,
    camera_index: int = 0
):
    # Open webcam
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print(f"Error: Unable to open camera #{camera_index}")
        return

    print("Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to read frame from webcam")
            break

        # Apply Gaussian blur
        blurred = cv2.GaussianBlur(frame, kernel_size, sigma)

        # Stack original and blurred side by side
        combined = cv2.hconcat([frame, blurred])

        # Show the result
        cv2.imshow('Original (left) | Blurred (right)', combined)

        # Exit on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Real-time Gaussian blur on webcam stream"
    )
    parser.add_argument(
        "--kernel", "-k",
        type=int,
        nargs=2,
        default=(5, 5),
        metavar=("KX", "KY"),
        help="Gaussian kernel size (odd integers), e.g. --kernel 5 5"
    )
    parser.add_argument(
        "--sigma", "-s",
        type=float,
        default=0,
        help="Sigma (standard deviation). 0 = auto-calc from kernel size"
    )
    parser.add_argument(
        "--camera", "-c",
        type=int,
        default=0,
        help="Camera index (default: 0)"
    )

    args = parser.parse_args()
    main(tuple(args.kernel), args.sigma, args.camera)
