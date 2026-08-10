"""TODO"""

import tkinter as tk

from pomodoro_timer import _settings

_NON_HOVER_TEXT = 'Reset'

_FLASH_ON_COLOR = 'green'
_FLASH_OFF_COLOR = 'light gray'


class ResetButton(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent,
                         highlightbackground='light gray',
                         highlightthickness=10)
        # dynamic
        self.hover_text = None
        self._non_hover_text = 'Reset'

        # widgets
        self._button = tk.Button()

        self.bind('<Enter>', self._mouse_enters)
        self.bind('<Leave>', self._mouse_leaves)

        # store after_ids for cancelling
        self._blink_id = None
        self._text_update_id = None

    def set_command(self, command):
        self._button.configure(command=command)

    def start_blinking(self):
        self._blink_id = self.blink(True)

    def blink(self, on: bool):
        self.after(_settings.BLINK_PERIOD_MILLIS, lambda: self.blink(not on))
        if on:
            self._set_color(_FLASH_ON_COLOR)
        else:
            self._set_color(_FLASH_OFF_COLOR)

    def stop_blinking(self):
        self.after_cancel(self._blink_id)
        self._set_color(_FLASH_OFF_COLOR)

    def _set_color(self, color: str):
        self.configure(highlightbackground=color)
        self._button.configure(bg=color)

    def _mouse_enters(self, _):
        """TODO"""
        self._button.configure(text=self.hover_text)

    def _mouse_leaves(self, _):
        """TODO"""
        self._button.configure(text=self._non_hover_text)
