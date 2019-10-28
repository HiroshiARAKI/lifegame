from lifegame import GUILifeGame


if __name__ == '__main__':

    # Create Conway's Game of Life GUI Frame
    game = GUILifeGame(f_shape=(50, 50), time_step=100)

    # Put Galaxy on center
    game.set_object('galaxy')

    # Start!!
    game.run()


