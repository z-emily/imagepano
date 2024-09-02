import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def plotAndSave(image, points, path, size = 1, color = "blue"):
    plt.imshow(image)
    plt.scatter(points[1], points[0],s=size,color=color)
    plt.savefig(path)
    plt.show()

def isInlier(source_pt, dest_pt, H, threshold):
    src_homogeneous = np.array([source_pt[0], source_pt[1], 1])
    dest_homogeneous = np.array([dest_pt[0], dest_pt[1], 1])

    # Calculate resulting point using homography
    transformed_pt = np.asarray(H.dot(src_homogeneous))
    transformed_pt /= transformed_pt[0,2]

    # Calculate Euclidean distance between transformed point and second point
    distance = np.linalg.norm(transformed_pt[0,:2] - dest_homogeneous[:2])

    # Check if the distance is below the threshold
    return distance < threshold

def saveImage(image):
    img = Image.fromarray(image.astype('uint8'))
    img.save("results/canvas.png", dpi=(500, 500))

def homogeneous_coordinate(coordinate):
    x = coordinate[0]/coordinate[2]
    y = coordinate[1]/coordinate[2]
    return x[0], y[0]