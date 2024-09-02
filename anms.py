import harris
import numpy as np

def adaptive_nonmaximal_suppression(points, H, threshold, goal_num=250):
    radiuses = {}

    for center_point in points:
        interest_points = []
        #Strength of current center point
        H_center = H[center_point[0],center_point[1]]
        # Find interest points with comparably large strengths
        for p in points:
            H_point = H[p[0],p[1]]
            interest_points.append(p) if H_center/H_point < threshold else None

        # If interest points found, record suppression radius for center point (minimum distance to strong point)
        if interest_points:
            interest_points = np.array(interest_points)
            harris_dists = harris.dist2(np.array([center_point]),interest_points)
            radiuses[center_point] = min(harris_dists[0])

    # Return 500 interest points with greatest suppression radius (strongest out of a large region)
    # ensures good spread of matching points
    selected_pts = []
    # point: radius to radius: point descending
    radiuses = sorted([(v, k) for (k, v) in radiuses.items()],reverse=True)
    for i in range(goal_num):
        selected_pts.append((radiuses[i][1][1],radiuses[i][1][0]))
    return selected_pts