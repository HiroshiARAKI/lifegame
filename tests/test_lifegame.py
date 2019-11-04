import unittest
import numpy as np
from lifegame.lifegame import LifeGame, BORN, SURVIVE, DIE_SPARSE, DIE_DENSE


class TestLifeGame(unittest.TestCase):
    """
    TestCase of lifegame/LifeGame class
    """
    def setUp(self) -> None:
        self.game = LifeGame()

    def test_init_rand(self):
        self.game.init_rand(rate=0)
        self.assertEqual(0, np.count_nonzero(self.game.cells))

    def test_clear(self):
        self.game.clear()
        self.assertEqual(0, np.count_nonzero(self.game.cells))

    def test_get_next_state(self):
        self.assertEqual(BORN, self.game.get_next_state(3, 0))

        self.assertEqual(SURVIVE, self.game.get_next_state(2, 1))
        self.assertEqual(SURVIVE, self.game.get_next_state(3, 1))

        self.assertEqual(DIE_DENSE, self.game.get_next_state(4, 1))
        self.assertEqual(DIE_DENSE, self.game.get_next_state(5, 1))

        self.assertEqual(DIE_SPARSE, self.game.get_next_state(1, 1))
        self.assertEqual(DIE_SPARSE, self.game.get_next_state(0, 1))


if __name__ == '__main__':
    unittest.main()
