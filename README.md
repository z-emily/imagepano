ImagePano Project
This project provides a complete image stitching pipeline using custom-built modules for Harris corner detection, adaptive non-maximal suppression (ANMS), feature descriptors, feature matching, RANSAC, and homography transformation. The goal is to align and blend two input images based on their common features.

Features
Harris Corner Detection: Detects key points in the images.
Adaptive Non-Maximal Suppression (ANMS): Refines key points to enhance the quality of the features.
Feature Descriptors and Matching: Extracts and matches features between images.
RANSAC: Robustly estimates the transformation matrix by fitting the model to the data.
Homography Transformation: Aligns images based on the estimated transformation matrix.
Custom Modules
This project utilizes several custom modules that you can also use in your own projects:

harris: Implements Harris corner detection.
homography: Contains functions for computing homography matrices.
warp: Provides image warping functionality based on homography.
anms: Implements adaptive non-maximal suppression to refine key points.
feature: Includes functions for finding and describing image features.
ransac: Implements the RANSAC algorithm for robust model fitting.
utils: Provides utility functions for plotting and saving images.
Installation
Clone the repository:

bash
Copy code
git clone git@github.com:z-emily/imagepano.git
cd imagepano
Install the required dependencies:

The project includes a requirements.txt file that lists all necessary Python packages. Install them using:

bash
Copy code
pip install -r requirements.txt
Ensure that all custom modules are accessible:

Make sure the custom modules (harris, homography, warp, anms, feature, ransac, utils) are correctly implemented and located in the same directory or installed in your Python environment.

Usage
Prepare your images:

Place the two images you want to process in a directory.

Run the script:

Use the following command to process the two images:

bash
Copy code
python main.py path/to/first_image.jpg path/to/second_image.jpg
Replace path/to/first_image.jpg and path/to/second_image.jpg with the actual file paths of your images.

Results:

The processed images will be saved in the results/ directory. The results include:

harris1.jpg: Harris corners on the first image.
harris2.jpg: Harris corners on the second image.
anms1.jpg: ANMS points on the first image.
anms2.jpg: ANMS points on the second image.
matched1.jpg: Matched features on the first image.
matched2.jpg: Matched features on the second image.
The final warped image will be saved as warped_image.jpg in the current directory.

Custom Modules Usage
You can integrate and utilize the custom modules in your own projects. Each module is designed to be standalone and can be imported and used as follows:

python
Copy code
from harris import get_harris_corners
from homography import computeH
from warp import warpImage
from anms import adaptive_nonmaximal_suppression
from feature import find_descriptors, match_features
from ransac import ransac
from utils import plotAndSave, saveImage
Refer to the module files for detailed usage and examples.

Contributing
Feel free to fork the repository and submit pull requests. For any issues or feature requests, please open an issue in the GitHub repository.

License
This project is licensed under the MIT License. See the LICENSE file for details.