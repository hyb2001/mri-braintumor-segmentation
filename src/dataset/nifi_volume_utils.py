import numpy as np
import nibabel as nib


def get_one_label_volume(mask: np.ndarray, label: int) -> np.ndarray:
    selector = lambda x: x if x == label else 0
    vfunc = np.vectorize(selector)
    return vfunc(mask)


def save_nifi_volume(volume:np.ndarray, path:str):
    img = nib.Nifti1Image(volume, np.eye(4))
    img.header.get_xyzt_units()
    img.to_filename(path)


def load_nifi_volume(filepath: str) -> np.ndarray:
    proxy = nib.load(filepath)
    img = proxy.get_fdata()
    proxy.uncache()
    return img

