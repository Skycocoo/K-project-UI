import pygame
from main.klib import msgbox
from main.klib import welcome

import wx, pdb
# from .klib import trainingmode
# from .klib import bodygame3

def main():
    info = None
    app = wx.App()
    # while not (hasattr(info, 'name') and hasattr(info, 'age') and hasattr(info, 'gender')):
    info = msgbox.Msgbox(None, title="Welcome")
    app.MainLoop()

    main_win = welcome.Welcome_win(info, parent=None, title='Menu')
    app.MainLoop()
    return main_win.game

if __name__ == '__main__':
    result = main()
