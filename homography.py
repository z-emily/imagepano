import numpy as np

def computeH(dest_pts,source_pts):
    A = []
    for i in range(len(dest_pts)):
        p1 = dest_pts[i]
        p2 = source_pts[i]
        im1x = p1[0]
        im1y = p1[1]
        im2x = p2[0]
        im2y = p2[1]

        A.append([im2x,im2y,1,0,0,0,-(im2x*im1x),-(im2y*im1x)])
        A.append([0,0,0,im2x,im2y,1,-(im2x*im1y),-(im2y*im1y)])

    A = np.array(A)

    b = []
    for p in dest_pts:
        b.extend(p[0:2])
    b = np.array([b]).T
    H = np.linalg.lstsq(A,b,rcond=-1)[0]

    return np.matrix([[H[0].item(), H[1].item(), H[2].item()],
                      [H[3].item(), H[4].item(), H[5].item()],
                       [H[6].item(), H[7].item(), 1.]])