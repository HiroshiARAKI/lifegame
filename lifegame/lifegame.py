from .cells import Cells
import numpy as np

BORN = 0
SURVIVE = 1
DIE_SPARSE = 2
DIE_DENSE = 3


class LifeGame(Cells):
    """
    The LifeGame: Main class
    """
    def __init__(self, f_shape: tuple = (100, 100), time_step: int = 1000) -> None:
        if (f_shape[0] * f_shape[1]) > (100 * 100):
            raise Exception('Please set Cells to fewer than (100, 100)')

        super().__init__(f_shape)
        self.w_h = int(150 / f_shape[0])
        self.w_w = int(150 / f_shape[1])
        self.dt = time_step

    def update(self) -> None:
        """
        Update next generation
        :return:
        """
        next_states = np.zeros(shape=self.cells.shape, dtype=int)

        for y, line in enumerate(self.cells):
            for x, cell in enumerate(line):
                next_states[x][y] = self.get_next_state(self.count_alive_cells(x, y),
                                                        self.is_alive(x, y)
                                                        )
        self.step_next_generation(next_states)

    def step_next_generation(self, next_states) -> None:
        """
        Change all cells' states by the Life Rule
        :param next_states:
        :return:
        """
        for y, line in enumerate(self.cells):
            for x, cell in enumerate(line):
                if next_states[x][y] == BORN:
                    self.cells[x][y] = 1

                elif next_states[x][y] == DIE_DENSE or next_states[x][y] == DIE_SPARSE:
                    self.cells[x][y] = 0

                else:
                    self.cells[x][y] = 1

    @staticmethod
    def get_next_state(n_cells, my_state) -> int:
        """
        Get next state of a cell
        :param n_cells:
        :param my_state:
        :return:
        """
        if not my_state and n_cells == 3:
            return BORN
        elif my_state and (n_cells == 2 or n_cells == 3):
            return SURVIVE
        elif my_state and n_cells <= 1:
            return DIE_SPARSE
        else:
            return DIE_DENSE

    def init_rand(self, rate: float) -> None:
        """
        Initialize cells' states randomly.
        :param rate:
        :return:
        """
        if rate < 0 or rate > 1:
            raise Exception('Please set the range of rate to 0 < rate < 1 ')

        for x, line in enumerate(self.cells):
            for y, cell in enumerate(line):
                self.cells[x][y] = 1 if np.random.rand() <= rate else 0

    def clear(self) -> None:
        """
        Clear all cells to dead
        :return:
        """
        self.cells = np.zeros(shape=self.f_shape, dtype=int)

