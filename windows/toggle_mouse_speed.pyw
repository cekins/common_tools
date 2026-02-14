"""
This script toggles windows mouse speed between 11 and 4 for the two different mice I like to use

Changelog
2026-02-14 - created
"""

import windows_mouse_speed_control

FAST_SPEED = 11
SLOW_SPEED = 4


def main():
    if windows_mouse_speed_control.get_mouse_speed() != FAST_SPEED:
        new_speed = FAST_SPEED
    else:
        new_speed = SLOW_SPEED

    windows_mouse_speed_control.set_mouse_speed(new_speed)


if __name__ == "__main__":
    main()
