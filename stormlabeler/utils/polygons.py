"""Utility methods for polygons."""

import numpy
import shapely.geometry
from stormlabeler.utils import general_utils
from stormlabeler.utils import error_checking


def _vertex_arrays_to_list(x_coordinates, y_coordinates):
    """Converts vertices of simple polygon from two arrays to one list.

    V = number of vertices

    :param x_coordinates: See doc for `check_vertex_arrays`.  NaN's are not
        allowed in this case.
    :param y_coordinates: Same.
    :return: vertex_coords_as_list: length-V list, where each element is a tuple
        with (x, y).
    """

    check_vertex_arrays(
        x_coordinates=x_coordinates, y_coordinates=y_coordinates,
        allow_nan=False)

    num_vertices = len(x_coordinates)
    vertex_coords_as_list = []

    for i in range(num_vertices):
        vertex_coords_as_list.append((x_coordinates[i], y_coordinates[i]))

    return vertex_coords_as_list


def check_vertex_arrays(x_coordinates, y_coordinates, allow_nan=True):
    """Error-checks vertex arrays.

    V = number of vertices

    :param x_coordinates: length-V numpy array of x-coordinates.  May contain
        NaN's, where the first NaN separates the exterior from the first hole
        and the [k]th NaN separates the [k - 1]th hole from the [k]th hole.
        This method assumes that the first unbroken string of real values (not
        NaN) represents the exterior of the polygon.
    :param y_coordinates: Same but for y-coordinates.
    :param allow_nan: Boolean flag.  If True, this method allows NaN's in the
        coordinate arrays.
    :return: ValueError: if NaN's occur at different positions in the two
        arrays.
    """

    error_checking.assert_is_boolean(allow_nan)

    if allow_nan:
        error_checking.assert_is_real_numpy_array(x_coordinates)
        error_checking.assert_is_real_numpy_array(y_coordinates)
    else:
        error_checking.assert_is_numpy_array_without_nan(x_coordinates)
        error_checking.assert_is_numpy_array_without_nan(y_coordinates)

    error_checking.assert_is_numpy_array(x_coordinates, num_dimensions=1)

    these_expected_dim = numpy.array([len(x_coordinates)], dtype=int)
    error_checking.assert_is_numpy_array(
        y_coordinates, exact_dimensions=these_expected_dim)

    x_nan_indices = numpy.where(numpy.isnan(x_coordinates))[0]
    y_nan_indices = numpy.where(numpy.isnan(y_coordinates))[0]

    if not numpy.array_equal(x_nan_indices, y_nan_indices):
        error_string = (
            'x-coord ({0:s}) and y-coord ({1:s}) lists have NaN''s at different'
            ' locations.'
        ).format(str(x_nan_indices), str(y_nan_indices))

        raise ValueError(error_string)


def vertex_arrays_to_polygon(x_coordinates, y_coordinates):
    """Converts vertex arrays to `shapely.geometry.Polygon` object.

    :param x_coordinates: See doc for `check_vertex_arrays`.  NaN's are allowed
        in this case.
    :param y_coordinates: Same.
    :return: polygon_object: Polygon object (instance of
        `shapely.geometry.Polygon`).
    """

    check_vertex_arrays(
        x_coordinates=x_coordinates, y_coordinates=y_coordinates, allow_nan=True
    )

    x_coords_2d_list = general_utils.split_array_by_nan(x_coordinates)
    y_coords_2d_list = general_utils.split_array_by_nan(y_coordinates)

    exterior_coords_as_list = _vertex_arrays_to_list(
        x_coordinates=x_coords_2d_list[0], y_coordinates=y_coords_2d_list[0]
    )

    num_holes = len(x_coords_2d_list) - 1
    if num_holes == 0:
        return shapely.geometry.Polygon(shell=exterior_coords_as_list)

    hole_coords_list_of_tuples = []

    for i in range(num_holes):
        hole_coords_list_of_tuples.append(
            _vertex_arrays_to_list(
                x_coordinates=x_coords_2d_list[i + 1],
                y_coordinates=y_coords_2d_list[i + 1]
            )
        )

    polygon_object = shapely.geometry.Polygon(
        shell=exterior_coords_as_list, holes=tuple(hole_coords_list_of_tuples)
    )

    assert polygon_object.is_valid
    return polygon_object


def point_in_or_on_polygon(
        polygon_object, query_x_coordinate, query_y_coordinate):
    """Returns True if point is inside/touching the polygon, False otherwise.

    :param polygon_object: `shapely.geometry.Polygon` object.
    :param query_x_coordinate: x-coordinate of query point.
    :param query_y_coordinate: y-coordinate of query point.
    :return: result: Boolean flag.  True if point is inside/touching the
        polygon, False otherwise.
    """

    error_checking.assert_is_not_nan(query_x_coordinate)
    error_checking.assert_is_not_nan(query_y_coordinate)

    point_object = shapely.geometry.Point(
        query_x_coordinate, query_y_coordinate)

    if polygon_object.contains(point_object):
        return True

    return polygon_object.touches(point_object)
