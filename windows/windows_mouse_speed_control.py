"""
This library allows the switching of windows 11 mouse speed settings using python

Changelog
2026-02-14 - created
"""

import ctypes

_GET_MOUSE_SPEED = 112
_SET_MOUSE_SPEED = 113
_SYSTEM_PARAMS_FUNC = ctypes.windll.user32.SystemParametersInfoA


def set_mouse_speed(value):
    _SYSTEM_PARAMS_FUNC(_SET_MOUSE_SPEED, 0, value, 0)


def get_mouse_speed():
    speed = ctypes.c_int()
    _SYSTEM_PARAMS_FUNC(_GET_MOUSE_SPEED, 0, ctypes.byref(speed), 0)
    return speed.value