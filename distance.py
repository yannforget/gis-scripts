"""Generate distance raster (in source CRS units) from input features
provided as binary rasters.
"""

import numpy as np
from scipy.ndimage.morphology import distance_transform_edt


def distance_to(raster, affine, dtype='uint16'):
    """Calculate distances (in original CRS units) from features provided
    as a binary raster.

    Parameters
    ----------
    raster : numpy 2d array
        Input raster as a 2d numpy array -- distance will be computed
        against any non-zero pixel value.
    affine : Affine
        Affine of the source raster, used to convert distance to CRS
        units.
    dtype : str or dtype
        Dtype of the output distance raster. Defaults to `uint16`.

    Returns
    -------
    distance : numpy 2d array
        Output distance raster.
    """
    distance = distance_transform_edt(np.logical_not(raster))
    distance *= affine.a
    return distance.astype(dtype)
