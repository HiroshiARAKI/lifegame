from lifegame import GUILifeGame, obj


if __name__ == '__main__':

    # Create Conway's Game of Life GUI Frame
    game = GUILifeGame(f_shape=(100, 100), time_step=10)

    # Put Galaxy on center
    game.set_object(obj.GALAXY)

    # Start!!
    game.run()
