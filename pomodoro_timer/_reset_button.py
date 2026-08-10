"""TODO"""

import tkinter as tk
import _settings

_NON_HOVER_TEXT = 'Reset'


class ResetButton(tk.Button):

    def __init__(self, parent):
        super().__init__(parent)

        # set text to dynamic variable
        self.hover_text = tk.StringVar(value='hover_text')
        self._non_hover_text = tk.StringVar(value=_NON_HOVER_TEXT)
        self.configure(textvariable=self._non_hover_text, font=_settings.FONT)

        self.bind('<Enter>', self._mouse_enters)
        self.bind('<Leave>', self._mouse_leaves)

    def _mouse_enters(self, _):
        """TODO"""
        self.configure(textvariable=self.hover_text)

    def _mouse_leaves(self, _):
        """TODO"""
        self.configure(textvariable=self._non_hover_text)
