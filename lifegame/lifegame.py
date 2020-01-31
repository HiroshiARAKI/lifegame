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
        if (f_shape[0] * f_shape[1]) > (300 * 300):
            raise Exception('Please set Cells to fewer than (300, 300)')

        super().__init__(f_shape)
        self.w_h = int(150 / f_shape[0])
        self.w_w = int(150 / f_shape[1])
        self.dt = time_step

    def update(self) -> None:
        """
        Update next generation
        :return:
        """
        alive_cells = [
            [self.count_alive_cells(x, y) for y in range(len(line))]
            for x, line in enumerate(self.cells)
        ]

        next_states = [
            [self.get_next_state(a, cell)
             for a, cell in zip(als, line)]
            for als, line in zip(alive_cells, self.cells)
        ]

        # step next generation
        self.cells = np.array([
            [self.get_next_generation(s) for s in ns]
            for ns in next_states
        ])

    @staticmethod
    def get_next_generation(state) -> int:
        """
        Get next generation status
        :param state:
        :return:
        """
        if state == BORN:
            return 1
        elif state == DIE_DENSE or state == DIE_SPARSE:
            return 0
        else:
            return 1

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

        self.cells = np.array([
            [1 if np.random.rand() <= rate else 0 for _ in c]
            for c in self.cells
            ]
        )

    def clear(self) -> None:
        """
        Clear all cells to dead
        :return:
        """
        self.cells = np.zeros(shape=self.f_shape, dtype=int)

