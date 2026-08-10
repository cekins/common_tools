"""TODO"""

import tkinter as tk

import _settings


class TimeButton(tk.Button):

    def __init__(self, parent, time_minutes):
        super().__init__(parent)

        self.configure(text=str(time_minutes),
                       font=_settings.FONT)

        self.time_minutes = time_minutes
