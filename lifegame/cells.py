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

    def is_alive(self, x, y):
        """
        The cell is alive?
        :param x:
        :param y:
        :return:
        """
        return True if self.cells[x][y] != 0 else False

    def count_alive_cells(self, x, y):
        """
        Count alive cells surrounding a cell.
        :param x:
        :param y:
        :return:
        """

        # indices of surrounding cells.
        ul = y - 1 if (y-1) >= 0 else 0  # upper left
        ur = y + 2 if (y+2) <= (self.f_shape[1]) else self.f_shape[1]  # upper right
        bl = x - 1 if (x-1) >= 0 else 0  # bottom left
        br = x + 2 if (x+2) <= (self.f_shape[0]) else self.f_shape[0]  # bottom right

        # slice
        cells = self.cells[bl:br, ul:ur]
        n_cells = np.count_nonzero(cells)

        return n_cells if not self.is_alive(x, y) else n_cells - 1

    def make_cell_change(self, x, y):
        """
        change the state (dead or live) of a cell
        :param x:
        :param y:
        :return:
        """
        self.cells[x][y] = 1 if not self.cells[x][y] else 0

