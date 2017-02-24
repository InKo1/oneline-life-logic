import unittest
import life


class TestLife(unittest.TestCase):
    def test_get_neighbours_coords(self):

        point = (1, 2)
        neighbours = {(0, 1), (0, 2), (0, 3), (1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3)}
        self.assertSetEqual(set(life._get_neighbours_coords(point)), neighbours)

    def test_get_dead_neighbours_coords(self):

        point = (1, 2)
        field = {(0, 1): 1, (2, 2): 1, (1, 3): 1, (1, 2): 1}
        dead_neighbours = {(0, 2), (0, 3), (1, 1), (2, 1), (2, 3)}
        self.assertSetEqual(set(life._get_dead_neighbours_coords(point, field)), dead_neighbours)

    def test_get_neighbours_size(self):

        point = (1, 2)
        field = {(1, 1): 1, (1, 2): 1, (2, 2): 1}
        self.assertEqual(life._get_neigbours_size(point, field), 2)

    def test_get_dead_cells_with_alive_neighbours_coords(self):

        field = {(1, 2): 1, (2, 1): 1}
        cells = {
            (0, 1), (0, 2), (0, 3), (1, 1), (1, 3), (2, 2),
            (2, 3), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2)
        }
        self.assertSetEqual(set(life._get_dead_cells_with_alive_neighbours_coords(field)), cells)

    def test_get_cells_who_must_live(self):

        field = {(1, 2): 1, (2, 1): 1, (0, 1): 1}
        cells = {(1, 2)}
        self.assertSetEqual(set(life._get_cells_who_must_live(field)), cells)

        field = {(1, 2): 1, (2, 1): 1, (0, 1): 1, (0, 2): 1}
        cells = {(1, 2), (0, 1), (0, 2)}
        self.assertSetEqual(set(life._get_cells_who_must_live(field)), cells)

        field = {(1, 2): 1, (2, 1): 1, (0, 1): 1, (0, 2): 1, (2, 3): 1}
        cells = {(0, 1), (0, 2)}
        self.assertSetEqual(set(life._get_cells_who_must_live(field)), cells)

    def test_get_cells_who_must_born(self):

        field = {(1, 2): 1, (2, 1): 1, (0, 1): 1}
        cells = {(1, 1)}
        self.assertSetEqual(set(life._get_cells_who_must_born(field)), cells)


if __name__ == '__main__':
    unittest.main()
