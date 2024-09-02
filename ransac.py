import numpy as np
from homography import computeH
from utils import isInlier

def ransac(matched, threshold = 5, num = 1000, num_samples = 4):
    best_points = {}
    matched_one = list(matched.keys())
    matched_two = list(matched.values())

    for _ in range(num):
        res = {}

        # sample 4 matched points
        sample_indices = np.random.choice(len(matched_one), num_samples, replace=False)
        sample_one =[]
        sample_two = []
        for i in range(num_samples):
            sample_one.append(matched_one[sample_indices[i]])
            sample_two.append(matched_two[sample_indices[i]])

        # calculate homography
        H = computeH(np.asarray(sample_one),np.asarray(sample_two))
        
        #count inliers for the fit
        for i in range(len(matched_two)):
            if isInlier(matched_two[i], matched_one[i], H, threshold):
                res[matched_one[i]] = matched_two[i]

        # update best points if greatest number of inliers
        if len(res) > len(best_points):
            best_points = res.copy()

    return best_points