"""Extract blocks (polygons) from input linear features (e.g. a
road network.
"""

import geojson
from shapely.geometry import shape, mapping
from shapely.ops import polygonize


def two_points_line(feature):
    """Convert a Polyline to a Line composed of only two points."""
    features = []
    coords = feature['geometry']['coordinates']
    for i in range(0, len(coords) - 1):
        segment_coords = [coords[i], coords[i+1]]
        geom = geojson.LineString(segment_coords)
        features.append(geojson.Feature(geometry=geom))
    return features


def blocks(features):
    """Generate urban blocks from a set of roads.

    Parameters
    ----------
    features : iterable of dict
        Roads as an iterable of GeoJSON-like dict.

    Returns
    -------
    blocks : iterable of dict
        Urban blocks as an iterable of GeoJSON-like dict.
    """
    segments = []
    for feature in features:
        for linestring in two_points_line(feature):
            segments.append(shape(linestring['geometry']))
    return [
        geojson.Feature(geometry=mapping(block))
        for block in polygonize(segments)
    ]
