import unittest
from lifegame.cells import Cells


class TestCells(unittest.TestCase):
    """
    TestCase of lifegame/Cells class
    """
    def setUp(self) -> None:
        self.cells = Cells(f_shape=(10, 10))

    def test_count_alive_cells(self):
        n_cells = self.cells.count_alive_cells(5, 5)
        self.assertEqual(0, n_cells)

        self.cells.cells[5][5] = 1
        n_cells = self.cells.count_alive_cells(5, 5)
        self.assertEqual(0, n_cells)  # Expected the center of cell is not counted

        self.cells.cells[5][6] = 1
        n_cells = self.cells.count_alive_cells(5, 5)
        self.assertEqual(1, n_cells)


if __name__ == '__main__':
    unittest.main()
