# GaussianProjects-
Gaussian Blur Projects Collection
# Gaussian Blur Projects Collection

This repository contains **six Python scripts**, each demonstrating different applications of Gaussian blur using OpenCV and Matplotlib. From basic image blurring to interactive, region-of-interest, real-time webcam processing, and iterative effects, these tools showcase how Gaussian filtering can be applied in various contexts.

---

## Project List

1. **Basic Blur Demo** (`Practice.py`) Apply Gaussian blur to an image with a kernel size of (5,5). Show the original and blurred image side by side.
   - **Description:** Applies a 5×5 Gaussian blur to a static image and displays the original and blurred versions side by side.
   - **Usage:**
     ```bash
     python Practice.py test.png
     ```
   - **Key Parameters:**
     - Kernel size (5,5)
     - Auto-calculated sigma

2. **Interactive Blur Prompt** (`Practice2.py`) Create a function that applies Gaussian blur with a user-defined kernel size and sigma.
   - **Description:** Prompts the user at runtime to enter a custom kernel size and sigma, then applies the blur and shows the results.
   - **Usage:**
     ```bash
     python Practice2.py test.png
     # Follow console prompts:
     #   Enter kernel size (e.g. 7 7)
     #   Enter sigma (e.g. 2.5)
     ```

3. **Sigma Comparison** (`Practice3.py`) Compare the effect of Gaussian blur with different sigma values on the same image.
   - **Description:** Blurs a static image with a fixed kernel (5×5) using multiple sigma values `[0, 1, 2, 5]`, plots all results in a single figure, and saves the output.
   - **Usage:**
     ```bash
     python Practice3.py
     ```
   - **Output:** Figure showing original plus each blurred variant; saved as `test2.jpg`.

4. **Interactive ROI Blur** (`Practice4.py`) Blur only a region of interest (ROI) in the image using Gaussian blur.
   - **Description:** Asks the user to define a rectangular “Region of Interest” (ROI) by typing `x y width height`, applies a Gaussian blur only to that region, and displays both original and ROI-blurred images.
   - **Usage:**
     ```bash
     python Practice4.py test.png
     # Follow console prompts to specify ROI coordinates and size.
     ```

5. **Real-Time Webcam Blur** (`Practice5.py`) Apply Gaussian blur in real-time to a webcam stream.
   - **Description:** Captures live video from a webcam, applies Gaussian blur to each frame in real time, and shows the original and blurred streams side by side. Press **q** to quit.
   - **Usage:**
     ```bash
     python Practice5.py --kernel 15 15 --sigma 100
     ```

6. **Iterative Blur Effect** (`Practice6.py`) Apply Gaussian blur iteratively and plot the result after each step.
   - **Description:** Applies Gaussian blur iteratively to an image for a specified number of iterations (`default=5`), then plots the original and each successive blur stage in one figure.
   - **Usage:**
     ```bash
     python Practice6.py --kernel 5 5 --sigma 1.0 --iters 5
     ```

---

## Prerequisites

- Python 3.7+
- OpenCV: `pip install opencv-python`
- NumPy: `pip install numpy`
- Matplotlib: `pip install matplotlib`

## Installation

```bash
git clone <repository_url>
cd <repository_folder>
python -m venv venv
# Activate the virtual environment:
# Windows PowerShell: .\venv\Scripts\activate
# Linux/macOS: source venv/bin/activate
pip install opencv-python numpy matplotlib
```

## Usage Tips

- **Kernel Size:** Always use odd integers (e.g., 3,5,7). Larger kernels produce stronger blur.
- **Sigma:** Controls spread of the Gaussian. `0` lets OpenCV auto-calculate based on kernel.
- **Real-Time Performance:** For webcam blur, high sigma values can slow down frame rate. Balance kernel & sigma for efficiency.

## License

This collection is licensed under the MIT License. Feel free to use and adapt for your own image-processing tasks.

