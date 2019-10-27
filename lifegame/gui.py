from .frame import LGFrame
import wx


class GUILifeGame:
    """
    Simulate LifeGame as a GUI application.
    """
    def __init__(self, f_shape: tuple = (50, 50), time_step: int = 1000) -> None:
        """
        Initialize GUI LifeGame
        :param f_shape tuple(int, int):
        :param time_step [ms]:
        """
        self.f_shape = f_shape
        self.dt = time_step

    def run(self, init_rand: bool = False, rate: float = 0.2) -> None:
        """
        Run GUI LifeGame
        :param init_rand:
        :param rate:
        :return:
        """
        app = wx.App()
        frame = LGFrame(f_shape=self.f_shape,
                        time_step=self.dt)

        if init_rand:
            frame.init_rand(None, rate)

        frame.Show()
        app.MainLoop()

