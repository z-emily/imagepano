import numpy as np
from skimage import transform
import harris

def find_descriptors(im, pts,patch_size=40):
    point_desc_map = {}
    for pt in pts:
        offset_col = int(pt[0]-patch_size//2)
        offset_row = int(pt[1]-patch_size//2)

        sample = np.array(im[offset_row:offset_row+patch_size,offset_col:offset_col+patch_size])
        downsample = transform.resize(sample, (8, 8), anti_aliasing=False)

        normalized_sample = (downsample-np.mean(downsample))/np.std(downsample)
        flattened = normalized_sample.flatten().reshape(1,64)
        point_desc_map[pt] = flattened
    return point_desc_map

def match_features(descriptor_one, descriptor_two,threshold=0.5):
    matched_points = {}
    for pt_1, desc_1 in descriptor_one.items():
        distances = {}
        for pt_2, desc_2 in descriptor_two.items():
            dist = harris.dist2(desc_1, desc_2)
            distances[pt_2] = dist[0][0]

        distances_arr = sorted((v, k) for (k, v) in distances.items())
        ratio = distances_arr[0][0]/distances_arr[1][0]
        if ratio < threshold:
            matched_points[pt_1] = distances_arr[0][1]
    return matched_points