import argparse
import random
import sys

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def visualize_voxel(res: np.ndarray, color: str = "blue") -> None:
    """Visualize voxel data in the specified color.
    This function visualize voxel data. We can specify the voxel color. 
    It's default is blue.
    Args:
        res(np.ndarray) : Boolean matrix of voxel data.
        color(str) : Surface color of visualised voxel data.
    Return:
        None 
    """

    # create colot map
    colors = np.full((res.shape[0], res.shape[1],
                      res.shape[2]), "blue", dtype=str)

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.voxels(res, facecolors=colors, edgecolor='k')
    plt.show()


def load_npy(npy_file_path: str) -> np.ndarray:
    """Load npy file includes voxel model"""
    return np.load(npy_file_path)

def quarry(voxel_map: np.ndarray, side_length:int) -> np.ndarray:
    x_len, y_len, z_len = voxel_map.shape
    if side_length > min(x_len, y_len, z_len):
        print(
            f"Minium length of one side is {min(x_len, y_len, z_len)}. You should input large integer than it.")
        sys.exit()

    # Decide on a range to leave values.
    x_start = random.randint(0, x_len - side_length)
    x_end = x_start + side_length
    y_start = random.randint(0, y_len - side_length)
    y_end = y_start + side_length
    z_start = random.randint(0, z_len - side_length)
    z_end = z_start + side_length

    # Masking
    voxel_map_masked = np.zeros((voxel_map.shape), dtype=int)
    voxel_map_masked[x_start:x_end, y_start:y_end,
                     z_start:z_end] = voxel_map[x_start:x_end, y_start:y_end, z_start:z_end]

    return voxel_map_masked


def main():
    # Argments
    parser = argparse.ArgumentParser(description='Voxel_model_augment.')
    parser.add_argument('npy_path', help='Voxel npy filepath.')
    parser.add_argument('side_lenght', help='Side lenght augmented voxel model.')
    args = parser.parse_args()

    # Get argments
    npy_path = args.npy_path
    side_length = int(args.side_lenght)

    # load voxel model
    voxel_map = load_npy(npy_path)

    #Augment
    voxel_map_masked = quarry(voxel_map, side_length)

    visualize_voxel(voxel_map_masked)
    ###If you want to save,
    #np.save("./voxcelized", visualize_voxel)


if __name__ == "__main__":
    main()
