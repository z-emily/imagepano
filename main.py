import harris
import matplotlib.pyplot as plt
from skimage import io
import numpy as np
from homography import computeH
from warp import warpImage
from anms import adaptive_nonmaximal_suppression
from feature import find_descriptors, match_features
from ransac import ransac
from utils import plotAndSave, saveImage
import argparse


def main():
    parser = argparse.ArgumentParser(description="Process two image file paths.")

    # Add arguments for the two image paths
    parser.add_argument(
        'imagepath1',
        type=str,
        help='Path to the first image file to be processed'
    )
    parser.add_argument(
        'imagepath2',
        type=str,
        help='Path to the second image file to be processed'
    )

    args = parser.parse_args()

    '''
    Sample Images
    IM_1_PATH = "images/left.jpg"
    IM_2_PATH = "images/right.jpg"
    '''

    #Loading Images
    IM_1_PATH = args.imagepath1
    IM_2_PATH = args.imagepath2

    one = io.imread(IM_1_PATH)
    two = io.imread(IM_2_PATH)

    one_bw = io.imread(IM_1_PATH, as_gray=True)
    two_bw = io.imread(IM_2_PATH, as_gray=True)

    H1, coords_1 = harris.get_harris_corners(one_bw)
    H2, coords_2 = harris.get_harris_corners(two_bw)

    plotAndSave(one, coords_1,"results/harris1.jpg")
    plotAndSave(two, coords_2,"results/harris2.jpg")

    points_1 = list(zip(coords_1[0],coords_1[1]))
    suppressed_points_1 = adaptive_nonmaximal_suppression(points_1,H1,0.9,goal_num=250)
    suppressed_points_1_list = [[p[1] for p in suppressed_points_1], [p[0] for p in suppressed_points_1]]
    plotAndSave(one, suppressed_points_1_list,"results/anms1.jpg")

    points_2 = list(zip(coords_2[0],coords_2[1]))
    suppressed_points_2 = adaptive_nonmaximal_suppression(points_2,H2,0.9,goal_num=250)
    suppressed_points_2_list = [[p[1] for p in suppressed_points_2], [p[0] for p in suppressed_points_2]]
    plotAndSave(two, suppressed_points_2_list,"results/anms2.jpg")


    #Find Descriptors
    descriptors_1 = find_descriptors(one_bw, suppressed_points_1)
    descriptors_2 = find_descriptors(two_bw, suppressed_points_2)

    #Match Feature Descriptors
    matched_features = match_features(descriptors_1, descriptors_2,threshold=0.5)

    matched_one = matched_features.keys()
    matched_one_list = [p[1] for p in matched_one], [p[0] for p in matched_one]
    plotAndSave(one, matched_one_list,"results/matched1.jpg")


    matched_two = matched_features.values()
    matched_two_list = [p[1] for p in matched_two], [p[0] for p in matched_two]
    plotAndSave(two, matched_two_list,"results/matched2.jpg")

    #RANSAC
    ransac_points = ransac(matched_features,threshold=0.5,num=1000)
    p_one = list(ransac_points.keys())
    p_two = list(ransac_points.values())

    #Compute Homography
    H = computeH(np.asarray(p_one),np.asarray(p_two))

    warped_img = warpImage(one,two,H)
    saveImage(warped_img)
    print("DONE")


if __name__ == "__main__":
    main()