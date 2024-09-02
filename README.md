# ImagePano Project

This project provides a complete image stitching pipeline using custom-built modules for Harris corner detection, adaptive non-maximal suppression (ANMS), feature descriptors, feature matching, RANSAC, and homography transformation. The goal is to align and blend two input images based on their common features.

## Features

- **Harris Corner Detection**: Detects key points in the images.
- **Adaptive Non-Maximal Suppression (ANMS)**: Refines key points to enhance the quality of the features.
- **Feature Descriptors and Matching**: Extracts and matches features between images.
- **RANSAC**: Robustly estimates the transformation matrix by fitting the model to the data.
- **Homography Transformation**: Aligns images based on the estimated transformation matrix.

## Custom Modules

This project utilizes several custom modules:

- **`harris`**: Implements Harris corner detection.
- **`homography`**: Contains functions for computing homography matrices.
- **`warp`**: Provides image warping functionality based on homography.
- **`anms`**: Implements adaptive non-maximal suppression to refine key points.
- **`feature`**: Includes functions for finding and describing image features.
- **`ransac`**: Implements the RANSAC algorithm for robust model fitting.
- **`utils`**: Provides utility functions for plotting and saving images.

## Installation

1. **Clone the repository:**

   ```bash
   git clone git@github.com:z-emily/imagepano.git
   cd imagepano
2. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
## Usage
1. **Run the script:**

   ```bash
   python main.py path/to/first_image.jpg path/to/second_image.jpg
>Replace path/to/first_image.jpg and path/to/second_image.jpg with the actual file paths of your images.

2. **Results:**

The processed images will be saved in the `results/` directory. The results include:

- `harris1.jpg`: Harris corners on the first image.
- `harris2.jpg`: Harris corners on the second image.
- `anms1.jpg`: ANMS points on the first image.
- `anms2.jpg`: ANMS points on the second image.
- `matched1.jpg`: Matched features on the first image.
- `matched2.jpg`: Matched features on the second image.
- `canvas.jpg`: The final panoramic image.