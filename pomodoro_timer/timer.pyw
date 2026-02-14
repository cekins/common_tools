#!/bin/python3


import sys
import tkinter as tk

import app


def main():
    root = tk.Tk()
    timer = app.App(root)

    # set ctrl-w to close timer
    root.bind('<Control-w>', lambda _: root.destroy())

    timer.mainloop()

    return 0


if __name__ == '__main__':
    sys.exit(main())
