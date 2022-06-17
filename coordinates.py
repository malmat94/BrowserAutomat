from pynput import *
#it's from https://www.youtube.com/watch?v=-7cFtMnseLI&ab_channel=WebDevPro

def coordinator (x, y):
    """Function that gives me coordinates of my mouse"""
    print("Now at: {}".format((x, y)))

with mouse.Listener(on_move = coordinator) as listener:
    listener.join()

