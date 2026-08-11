"""
A timer that utilizes color rather than sound to indicate completion. Used to not disturb coworkers

This timer is set for pomodoro work; 25 min on, 5 min off

Changelog:
2026-02-14 - transferred from other repository to this one

TODO
* make a mouseover show how much time is remaining on the clock
"""

import tkinter as tk

import _settings
from _reset_button import ResetButton
from _time_button import TimeButton


class GUI(tk.Frame):
    """TODO"""

    TITLE_PREFIX = 'Visual Timer'
    TITLE_SUFFIX = ' - {time} minutes'

    WINDOW_DIMENSIONS = '650x400'

    def __init__(self, master):
        super().__init__(master)
        self.pack(expand=True, fill='both')

        # set appearance
        self.master.title(self.TITLE_PREFIX)
        self.master.geometry(self.WINDOW_DIMENSIONS)

        # create buttons
        self.reset_button = ResetButton(self)
        self.time_buttons = []
        for time_option in _settings.TIME_OPTIONS:
            self.time_buttons.append(TimeButton(self, time_option))

        # pack reset button into frame
        self.reset_button.pack(expand=True, fill='both')

    def show_time_buttons(self):
        self.reset_button.pack_forget()
        for time_button in self.time_buttons:
            time_button.pack(side='left', expand=True, fill='both')

    def show_reset_button(self):
        for time_button in self.time_buttons:
            time_button.pack_forget()
        self.reset_button.pack(expand=True, fill='both')

    def flash_on(self):
        self.reset_button.configure(highlightbackground='green')
        self.reset_button.configure(bg='green')

    def flash_off(self):
        self.reset_button.configure(highlightbackground='light gray')
        self.reset_button.configure(bg='light gray')
