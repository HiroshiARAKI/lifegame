import numpy as np


class Cells(object):
    """
    Manege cells
    """
    def __init__(self, f_shape):
        self.f_shape = f_shape
        self.cells = np.zeros(shape=f_shape, dtype=int)

    def get_cells(self):
        return self.cells

    def count_alive_cells(self, x, y):
        """
        Count alive cells surrounding a cell.
        :param x:
        :param y:
        :return:
        """

        # indices of surrounding cells.
        ul = max(y - 1, 0)  # upper left
        ur = min(y + 2, self.f_shape[1])  # upper right
        bl = max(x - 1, 0)  # bottom left
        br = min(x + 2, self.f_shape[0])  # bottom right

        # slice
        cells = self.cells[bl:br, ul:ur]
        n_cells = np.count_nonzero(cells)

        return n_cells - self.cells[x][y]

    def make_cell_change(self, x, y):
        """
        change the state (dead or live) of a cell
        :param x:
        :param y:
        :return:
        """
        self.cells[x][y] = 1 if not self.cells[x][y] else 0

