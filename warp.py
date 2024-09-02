import numpy as np
import matplotlib.pyplot as plt
import skimage.draw as draw
from utils import homogeneous_coordinate

def warpImage(dest_im,src_im, H):
    height,width,ch = src_im.shape

    #Find Bounds
    corners = [[0, height, 1],[width, height, 1],[0, 0, 1],[width, 0, 1]]
    transformed_corners = np.squeeze(np.asarray([H.dot(p) for p in corners]))
    transformed_corners = [p / p[2] for p in transformed_corners]

    max_x = int(max(transformed_corners,key= lambda p: p[0])[0])
    max_y = int(max(transformed_corners,key= lambda p: p[1])[1])
    min_x = int(min(transformed_corners, key= lambda p: p[0])[0])
    min_y = int(min(transformed_corners, key= lambda p: p[1])[1])

    max_x_all = max(max_x, dest_im.shape[1], src_im.shape[1])
    max_y_all = max(max_y, dest_im.shape[0], src_im.shape[0])

    move_x = abs(min(0,min_x))
    move_y = abs(min(0,min_y))

    canvas_height = max_y_all+abs(min_y)
    canvas_width = max_x_all+abs(min_x)

    canvas = np.zeros((canvas_height+1, canvas_width+1, 3))

    #New Image Polygon
    col_coor,row_coor = draw.polygon([0,canvas_width,canvas_width,0],[0,0,canvas_height,canvas_height])

    #Transform to Homogenous coordinates
    canvas_coords = np.vstack([col_coor,row_coor, np.ones(len(row_coor))])
    transformed = np.linalg.inv(H).dot(canvas_coords)
    new_col_coor,new_row_coor = homogeneous_coordinate(transformed)

    #Retain only valid indices
    valid_indices = np.where((new_row_coor >= 0) & (new_row_coor < src_im.shape[0]) & (new_col_coor >= 0) & (new_col_coor < src_im.shape[1]))

    new_col_coor = new_col_coor[valid_indices].astype(int)
    new_row_coor = new_row_coor[valid_indices].astype(int)
    col_coor = np.array([col_coor])[valid_indices].astype(int)+move_x
    row_coor = np.array([row_coor])[valid_indices].astype(int)+move_y

    #Add to Canvas
    canvas[row_coor, col_coor] = src_im[new_row_coor, new_col_coor]

    #Blend
    def generate_alpha_mask(width, height):
        # Create a linear gradient alpha mask
        half = width // 2
        no_change_half = np.ones(half)
        gradient = np.linspace(1, 0, half)
        alpha = np.append(no_change_half, gradient)

        # Repeat the alpha gradient for each row
        alpha_mask = np.tile(alpha, (height, 1))
        alpha_mask = alpha_mask.reshape((height, width, 1))  # Reshape to broadcasting

        return alpha_mask
        
    alpha = generate_alpha_mask(width, height)
    transparent_dest_im = dest_im*alpha

    canvas[move_y:dest_im.shape[0]+move_y,move_x:dest_im.shape[1]+move_x] = (alpha)*transparent_dest_im + (1-alpha)*canvas[move_y:dest_im.shape[0]+move_y, move_x:dest_im.shape[1]+move_x]

    return canvas
