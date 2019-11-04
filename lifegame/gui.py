from .frame import LGFrame
import wx
import numpy as np
from glob import glob
import os


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
        self.app = wx.App()
        self.frame = LGFrame(f_shape=self.f_shape,
                             time_step=self.dt)

    def run(self, init_rand: bool = False, rate: float = 0.2) -> None:
        """
        Run GUI LifeGame
        :param init_rand:
        :param rate:
        :return:
        """

        if init_rand:
            self.frame.init_rand(None, rate)

        self.frame.Show()
        self.app.MainLoop()

    def set_object(self, obj: str = 'glider', center: bool = True, x: int = 0, y: int = 0):
        """
        Set an object to the Game Field
        :param obj:
        :param center:
        :param x:
        :param y:
        :return:
        """
        obj_path = os.getcwd()+'/lifegame/objects/'
        objects = glob(obj_path + '*.txt')
        objects = [os.path.basename(o)[:-4] for o in objects]
        print(objects)

        if obj not in objects:
            raise Exception('The object "{}" is not supported now.'.format(obj))

        obj = np.loadtxt(obj_path + '{}.txt'.format(obj), delimiter=',').T
        if center:
            x = int(self.f_shape[0] / 2 - len(obj) / 2)
            y = int(self.f_shape[1] / 2 - len(obj[0]) / 2)

        self.frame.set_object(obj, x, y)



