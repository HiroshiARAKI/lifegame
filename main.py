from lifegame import GUILifeGame


if __name__ == '__main__':

    # Create Conway's Game of Life GUI Frame
    game = GUILifeGame(f_shape=(10, 10), time_step=100)

    # Start!!
    game.run(init_rand=True, rate=0.2)


