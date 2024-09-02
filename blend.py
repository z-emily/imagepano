import numpy as np
import matplotlib.pyplot as plt 

def linearBlending(left, right):
        h, w = left.shape[:2]
        
        # overlap mask
        overlap_mask = np.zeros((h, w), dtype="int")
        for i in range(h):
            for j in range(w):
                if (np.count_nonzero(right[i, j]) > 0 and np.count_nonzero(left[i, j]) > 0):
                    overlap_mask[i, j] = 1
        
        # Plot overlap mask
        plt.imshow(overlap_mask.astype(int), cmap="gray")
        plt.show()
        
        # compute alpha mask on overlap region
        alpha_mask = np.zeros((h, w))
        for i in range(h): 
            minIdx = maxIdx = -1
            for j in range(w):
                if (overlap_mask[i, j] == 1 and minIdx == -1):
                    minIdx = j
                if (overlap_mask[i, j] == 1):
                    maxIdx = j
            
            if (minIdx == maxIdx):
                continue
                
            decrease_step = 1 / (maxIdx - minIdx)
            for j in range(minIdx, maxIdx + 1):
                alpha_mask[i, j] = 1 - (decrease_step * (j - minIdx))
        
        
        
        linearBlending_img = np.copy(right)
        linearBlending_img[:h, :w] = np.copy(left)
        # linear blending
        for i in range(h):
            for j in range(w):
                if ( np.count_nonzero(overlap_mask[i, j]) > 0):
                    linearBlending_img[i, j] = alpha_mask[i, j] * left[i, j] + (1 - alpha_mask[i, j]) * right[i, j]
        
        return linearBlending_img