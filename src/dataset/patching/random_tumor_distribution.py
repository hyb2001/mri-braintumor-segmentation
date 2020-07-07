import numpy as np
from src.dataset.patching.commons import array3d_center_crop


def _select_random_start_in_tumor(segmentation_mask, patch_size):
    # filter region where we can compute tumor
    crop_shape = (segmentation_mask.shape[0]-patch_size[0],
                  segmentation_mask.shape[1]-patch_size[1],
                  segmentation_mask.shape[2]-patch_size[2])

    cropped_mask = array3d_center_crop(segmentation_mask, crop_shape)

    # select tumor region and random choose center
    tumor_region_indices = np.nonzero(cropped_mask)
    axis_center = np.random.randint(0, len(tumor_region_indices[0]))

    return tumor_region_indices[0][axis_center], tumor_region_indices[1][axis_center], tumor_region_indices[2][axis_center]


def patching(volume: np.ndarray, labels: np.ndarray, patch_size: tuple):
    """
    Randomly chosen inside the tumor region
    """
    start_x, start_y, start_z = _select_random_start_in_tumor(labels, patch_size)
    volume_patch = volume[:, start_x:start_x+patch_size[0], start_y:start_y+patch_size[1], start_z:start_z+patch_size[2]]
    seg_patch = labels[start_x:start_x + patch_size[0], start_y:start_y + patch_size[1], start_z:start_z + patch_size[2]]

    return volume_patch, seg_patch
