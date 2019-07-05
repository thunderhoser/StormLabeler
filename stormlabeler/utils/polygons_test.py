"""Unit tests for polygons.py."""

import unittest
import numpy
import shapely.geometry
from stormlabeler.utils import polygons

TOLERANCE = 1e-6
TOLERANCE_NUM_DECIMAL_PLACES = 6

X_COORDS_COMPLEX = numpy.array([
    0, 0, 60, 60, 0, numpy.nan, 15, 15, 45, 45, 15
])
Y_COORDS_COMPLEX = numpy.array([
    0, 40, 40, 0, 0, numpy.nan, 10, 30, 30, 10, 10
])

X_COORDS_SIMPLE = X_COORDS_COMPLEX[:5]
Y_COORDS_SIMPLE = Y_COORDS_COMPLEX[:5]

# The following constants are used to test _vertex_arrays_to_list.
COORD_LIST_COMPLEX = [
    (0, 0), (0, 40), (60, 40), (60, 0), (0, 0), (numpy.nan, numpy.nan),
    (15, 10), (15, 30), (45, 30), (45, 10), (15, 10)
]

COORD_LIST_SIMPLE = COORD_LIST_COMPLEX[:5]

# The following constants are used to test vertex_arrays_to_polygon.
POLYGON_OBJECT_SIMPLE = shapely.geometry.Polygon(shell=COORD_LIST_SIMPLE)

COORD_LIST_HOLE = COORD_LIST_COMPLEX[6:]
POLYGON_OBJECT_COMPLEX = shapely.geometry.Polygon(
    shell=COORD_LIST_SIMPLE, holes=tuple([COORD_LIST_HOLE])
)

# The following constants are used to test point_in_or_on_polygon.
QUERY_X_COORDS = numpy.array(
    [0, 10, 20, 30, 40, 50, 60, 0, 10, 20, 40, 50, 60], dtype=float
)
QUERY_Y_COORDS = numpy.array(
    [0, 10, 20, 30, 40, 50, 60, 60, 50, 40, 20, 10, 0], dtype=float
)

IN_ON_POLYGON_FLAGS_SIMPLE = numpy.array(
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1], dtype=bool
)
IN_ON_POLYGON_FLAGS_COMPLEX = numpy.array(
    [1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1], dtype=bool
)


class PolygonsTests(unittest.TestCase):
    """Each method is a unit test for polygons.py."""

    def test_vertex_arrays_to_list_simple(self):
        """Ensures correct output from _vertex_arrays_to_list.

        In this case, using simple polygon.
        """

        this_coord_list = polygons._vertex_arrays_to_list(
            x_coordinates=X_COORDS_SIMPLE, y_coordinates=Y_COORDS_SIMPLE)

        self.assertTrue(len(this_coord_list), len(COORD_LIST_SIMPLE))

        for i in range(len(this_coord_list)):
            self.assertTrue(numpy.allclose(
                this_coord_list[i], COORD_LIST_SIMPLE[i], atol=TOLERANCE,
                equal_nan=True
            ))

    # def test_vertex_arrays_to_list_complex(self):
    #     """Ensures correct output from _vertex_arrays_to_list.
    #
    #     In this case, using complex polygon.
    #     """
    #
    #     this_coord_list = polygons._vertex_arrays_to_list(
    #         x_coordinates=X_COORDS_COMPLEX, y_coordinates=Y_COORDS_COMPLEX)
    #
    #     self.assertTrue(len(this_coord_list), len(COORD_LIST_COMPLEX))
    #
    #     for i in range(len(this_coord_list)):
    #         self.assertTrue(numpy.allclose(
    #             this_coord_list[i], COORD_LIST_COMPLEX[i], atol=TOLERANCE,
    #             equal_nan=True
    #         ))

    def test_vertex_arrays_to_polygon_simple(self):
        """Ensures correct output from vertex_arrays_to_polygon.

        In this case, using simple polygon.
        """

        this_polygon_object = polygons.vertex_arrays_to_polygon(
            x_coordinates=X_COORDS_SIMPLE, y_coordinates=Y_COORDS_SIMPLE)

        self.assertTrue(
            this_polygon_object.almost_equals(
                POLYGON_OBJECT_SIMPLE, decimal=TOLERANCE_NUM_DECIMAL_PLACES)
        )

    def test_vertex_arrays_to_polygon_complex(self):
        """Ensures correct output from vertex_arrays_to_polygon.

        In this case, using complex polygon.
        """

        this_polygon_object = polygons.vertex_arrays_to_polygon(
            x_coordinates=X_COORDS_COMPLEX, y_coordinates=Y_COORDS_COMPLEX)

        self.assertTrue(
            this_polygon_object.almost_equals(
                POLYGON_OBJECT_COMPLEX, decimal=TOLERANCE_NUM_DECIMAL_PLACES)
        )

    def test_point_in_or_on_polygon_simple(self):
        """Ensures correct output from point_in_or_on_polygon.

        In this case, using simple polygon.
        """

        num_query_points = len(QUERY_X_COORDS)
        these_flags = numpy.full(num_query_points, False, dtype=bool)

        for k in range(num_query_points):
            these_flags[k] = polygons.point_in_or_on_polygon(
                polygon_object=POLYGON_OBJECT_SIMPLE,
                query_x_coordinate=QUERY_X_COORDS[k],
                query_y_coordinate=QUERY_Y_COORDS[k]
            )

        self.assertTrue(numpy.array_equal(
            these_flags, IN_ON_POLYGON_FLAGS_SIMPLE
        ))

    def test_point_in_or_on_polygon_complex(self):
        """Ensures correct output from point_in_or_on_polygon.

        In this case, using complex polygon.
        """

        num_query_points = len(QUERY_X_COORDS)
        these_flags = numpy.full(num_query_points, False, dtype=bool)

        for k in range(num_query_points):
            these_flags[k] = polygons.point_in_or_on_polygon(
                polygon_object=POLYGON_OBJECT_COMPLEX,
                query_x_coordinate=QUERY_X_COORDS[k],
                query_y_coordinate=QUERY_Y_COORDS[k]
            )

        self.assertTrue(numpy.array_equal(
            these_flags, IN_ON_POLYGON_FLAGS_COMPLEX
        ))


if __name__ == '__main__':
    unittest.main()
