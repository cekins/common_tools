"""
A timer that utilizes color rather than sound to indicate completion. Used to not disturb coworkers

This timer is set for pomodoro work; 25 min on, 5 min off

Changelog:
2026-02-14 - transferred from other repository to this one

TODO
* make a mouseover show how much time is remaining on the clock
"""

import tkinter as tk
from tkinter import font


class App(tk.Frame):
    """TODO"""

    TITLE_PREFIX = 'Visual Timer'
    TITLE_SUFFIX = ' - {time} minutes'

    WINDOW_DIMENSIONS = '650x400'

    FONT = 'Helvetica 36 bold' 

    def __init__(self, master):
        super().__init__(master)
        self.pack(expand=True, fill='both')

        # set appearance
        self.master.title(self.TITLE_PREFIX)
        self.master.geometry(self.WINDOW_DIMENSIONS)

        # create buttons
        self.btn_25 = tk.Button(self, text='25', font=self.FONT)
        self.btn_25.configure(command=lambda: self._press_timer_button(25))

        self.btn_5 = tk.Button(self, text='5', font=self.FONT)
        self.btn_5.configure(command=lambda: self._press_timer_button(5))

        self.frame_reset = tk.Frame(self, 
                                    highlightbackground='light gray',
                                    highlightthickness=10)
        self.btn_reset = tk.Button(self.frame_reset, text='Reset', font=self.FONT)
        self.btn_reset.configure(command=self._reset)
        self.btn_reset.pack(expand=True, fill='both')

        self._pack_time_buttons()

    def _pack_time_buttons(self):
        self.frame_reset.pack_forget()
        self.btn_25.pack(side='left', expand=True, fill='both')
        self.btn_5.pack(side='left', expand=True, fill='both')

    def _pack_reset_button(self):
        self.btn_25.pack_forget()
        self.btn_5.pack_forget()
        self.frame_reset.pack(expand=True, fill='both')

    def _press_timer_button(self, time):
        self._pack_reset_button()
        self.master.title(self.TITLE_PREFIX + self.TITLE_SUFFIX.format(time=time))
        self._time = self.master.after(time * 60000, self._alarm)

    def _alarm(self):
        self.master.attributes('-topmost', True)
        self.master.attributes('-topmost', False)
        self._blink_on()

    def _blink_on(self):
        self.frame_reset.configure(highlightbackground='green')
        self.btn_reset.configure(bg='green')
        self._time = self.master.after(500, self._blink_off)

    def _blink_off(self):
        self.frame_reset.configure(highlightbackground='light gray')
        self.btn_reset.configure(bg='light gray')
        self._time = self.master.after(500, self._blink_on)

    def _reset(self):
        self.master.after_cancel(self._time)
        self.frame_reset.configure(highlightbackground='light gray')
        self.btn_reset.configure(bg='light gray')
        self._pack_time_buttons()
        self.master.title(self.TITLE_PREFIX)




