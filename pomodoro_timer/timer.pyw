#!/bin/python3


import sys
import time
import tkinter as tk

from gui import GUI

_SEC_PER_MIN = 60
_MILLI_PER_SEC = 1000

_TIMER_TEXT_UPDATE_PERIOD = 1000

_BLINK_PERIOD = 1000


class Timer:

    def __init__(self, time_minutes):
        self._start_time = time.monotonic() + time_minutes * _SEC_PER_MIN

    def get_time_str(self):
        remaining_sec = self._start_time - time.monotonic()
        min, sec = divmod(int(remaining_sec), _SEC_PER_MIN)
        return f'{min:02d}:{sec:02d}'


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.gui = GUI(self)

        # set ctrl-w to close timer
        self.bind('<Control-w>', lambda _: self.destroy())

        # wire button behavior
        self.gui.reset_button.set_command(self.reset)
        for time_button in self.gui.time_buttons:
            time_button.configure(command=lambda t=time_button.time_minutes: self.start_timer(t))

        # configure App behavior
        self.gui.show_time_buttons()

        # configure placeholder
        self._timer = None

        self._update_timer_text_id = None

    def start_timer(self, time_minutes: int):
        time_seconds = time_minutes * _SEC_PER_MIN
        time_millis = time_seconds * _MILLI_PER_SEC

        self.after(time_millis, self.end_timer)
        self._timer = Timer(time_minutes)
        self.update_timer_text()

        self.gui.show_reset_button()

    def end_timer(self):
        self.after_cancel(self._update_timer_text_id)
        self._force_to_front()
        self.gui.reset_button.start_blinking()

    def update_timer_text(self):
        self._update_timer_text_id = self.after(_TIMER_TEXT_UPDATE_PERIOD,
                                                self.update_timer_text)
        self.gui.reset_button.hover_text.set(self._timer.get_time_str())

    def reset(self):
        if self._update_timer_text_id is not None:
            self.after_cancel(self._update_timer_text_id)

        self.gui.reset_button.stop_blinking()
        self.gui.show_time_buttons()

    def _force_to_front(self):
        """TODO"""
        # de minimize
        self.deiconify()

        # lift to top of stack
        self.lift()

        # windows OS specific steps
        self.attributes("-topmost", True)
        self.after_idle(self.attributes, "-topmost", False)


def main():
    App().mainloop()

    return 0


if __name__ == '__main__':
    sys.exit(main())
