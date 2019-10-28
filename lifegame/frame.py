import wx
import numpy as np
import os
from datetime import datetime
from .lifegame import LifeGame


class LGFrame(wx.Frame):
    """
    LifeGame GUI Frame on wxPython
    """
    RUN = 0
    STEP = 1
    STOP = 2
    CLEAR = 3

    def __init__(self, f_shape, w_size: int = 600, time_step: int = 1000) -> None:
        # initialize Conway's Game of Life Frame
        self.game = LifeGame(f_shape=f_shape)

        self.cell_size = float(w_size) / float(f_shape[0])
        self.x_max = float(f_shape[0]) * self.cell_size
        self.y_max = 25 + float(f_shape[1]) * self.cell_size
        self.f_shape = f_shape
        self.dt = time_step

        wx.Frame.__init__(self, None, -1,
                          title='LifeGame', size=(w_size, self.y_max*1.1))

        # Setup Panel
        self.panel = wx.Panel(self)
        self.SetBackgroundColour('white')

        # Setup Click event
        self.panel.Bind(wx.EVT_LEFT_DOWN, self.click)

        # Setup Timer
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.run)
        self.state = self.STOP

        # Setup Buttons
        self.btn1 = wx.Button(self.panel, wx.ID_ANY, label='Run')
        self.btn2 = wx.Button(self.panel, wx.ID_ANY, label='Step')
        self.btn3 = wx.Button(self.panel, wx.ID_ANY, label='Stop')
        self.btn4 = wx.Button(self.panel, wx.ID_ANY, label='Clear')
        self.btn5 = wx.Button(self.panel, wx.ID_ANY, label='Random')
        self.btn6 = wx.Button(self.panel, wx.ID_ANY, label='Save')

        self.btn1.SetBackgroundColour('blue')
        self.btn2.SetBackgroundColour('blue')
        self.btn3.SetBackgroundColour('blue')
        self.btn4.SetBackgroundColour('blue')
        self.btn5.SetBackgroundColour('blue')
        self.btn6.SetBackgroundColour('blue')

        self.btn1.Bind(wx.EVT_BUTTON, self.run)
        self.btn2.Bind(wx.EVT_BUTTON, self.step)
        self.btn3.Bind(wx.EVT_BUTTON, self.stop)
        self.btn4.Bind(wx.EVT_BUTTON, self.clear)
        self.btn5.Bind(wx.EVT_BUTTON, self.init_rand)
        self.btn6.Bind(wx.EVT_BUTTON, self.save)

        self.btn3.Disable()

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.btn1, 1)
        sizer.Add(self.btn2, 1)
        sizer.Add(self.btn3, 1)
        sizer.Add(self.btn4, 1)
        sizer.Add(self.btn5, 1)
        sizer.Add(self.btn6, 1)

        self.panel.Bind(wx.EVT_PAINT, self.draw)
        self.Center()
        self.panel.SetSizer(sizer)

        # Setup Statusbar
        self.CreateStatusBar()
        self.gen = 0
        self.SetStatusText('Size = (%d, %d): Generation = %d,   Alive cells = %d'
                           % (self.f_shape[0], self.f_shape[1], self.gen, np.count_nonzero(self.game.cells)))

    def draw(self, event):
        s = self.cell_size
        dc = wx.PaintDC(self.panel)
        dc.Clear()
        dc.SetPen(wx.Pen('gray'))
        for i, x in enumerate(np.arange(0, self.x_max, s)):
            for j, y in enumerate(np.arange(25, self.y_max, s)):
                color = 'white' if self.game.cells[i][j] == 0 else 'black'

                dc.SetBrush(wx.Brush(color))

                dc.DrawRectangle(x, y, s, s)

    def run(self, event):
        self.btn1.Disable()
        self.btn2.Disable()
        self.btn3.Enable()
        self.btn4.Disable()
        self.btn5.Disable()
        self.btn6.Disable()

        self.timer.Start(self.dt)
        self.game.update()
        self.gen += 1
        self.SetStatusText('Size = (%d, %d): Generation = %d,   Alive cells = %d'
                           % (self.f_shape[0], self.f_shape[1], self.gen, np.count_nonzero(self.game.cells)))
        self.panel.Refresh()

    def step(self, event):
        self.btn1.Enable()
        self.btn2.Enable()
        self.btn3.Disable()
        self.btn4.Enable()
        self.btn5.Enable()
        self.btn6.Enable()

        self.game.update()
        self.gen += 1
        self.SetStatusText('Size = (%d, %d): Generation = %d,   Alive cells = %d'
                           % (self.f_shape[0], self.f_shape[1], self.gen, np.count_nonzero(self.game.cells)))
        self.panel.Refresh()

    def stop(self, event):
        self.btn1.Enable()
        self.btn2.Enable()
        self.btn3.Disable()
        self.btn4.Enable()
        self.btn5.Enable()
        self.btn6.Enable()

        self.timer.Stop()

    def clear(self, event):
        self.btn1.Enable()
        self.btn2.Enable()
        self.btn3.Disable()
        self.btn4.Enable()
        self.btn5.Enable()
        self.btn6.Enable()

        self.game.clear()
        self.gen = 0
        self.SetStatusText('Size = (%d, %d): Generation = %d,   Alive cells = %d'
                           % (self.f_shape[0], self.f_shape[1], self.gen, np.count_nonzero(self.game.cells)))
        self.Refresh()

    def init_rand(self, event, rate: float = 0.2):
        self.btn1.Enable()
        self.btn2.Enable()
        self.btn3.Disable()
        self.btn4.Enable()
        self.btn5.Enable()

        self.game.init_rand(rate)
        self.gen = 0
        self.SetStatusText('Size = (%d, %d): Generation = %d,   Alive cells = %d'
                           % (self.f_shape[0], self.f_shape[1], self.gen, np.count_nonzero(self.game.cells)))
        self.Refresh()

    def save(self, event):
        self.btn1.Enable()
        self.btn2.Enable()
        self.btn3.Disable()
        self.btn4.Enable()
        self.btn5.Enable()
        self.btn6.Enable()

        os.makedirs('save/', exist_ok=True)
        file_name = 'save/data_%s.txt' % (datetime.now().strftime('%Y%m%d_%H-%M%-S'))
        np.savetxt(file_name, self.game.cells.T, fmt='%d',  delimiter=',')
        self.SetStatusText('Size = (%d, %d): Generation = %d,   Alive cells = %d,   Saved as "%s" !'
                           % (self.f_shape[0], self.f_shape[1], self.gen, np.count_nonzero(self.game.cells),
                              file_name))
        self.Refresh()

    def click(self, event):
        (x, y) = event.GetPosition()
        x = int(np.floor(x / self.cell_size))
        y = int(np.floor((y-25) / self.cell_size))

        self.game.cells[x][y] = 1 if self.game.cells[x][y] == 0 else 0

        self.SetStatusText('Size = (%d, %d): Generation = %d,   Alive cells = %d'
                           % (self.f_shape[0], self.f_shape[1], self.gen, np.count_nonzero(self.game.cells)))

        self.Refresh()

    def set_object(self, obj, x: int = 0, y: int = 0):
        self.game.cells[x:x+len(obj), y:y+len(obj[0])] = obj
