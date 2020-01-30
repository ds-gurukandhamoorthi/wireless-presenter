#!/usr/bin/env python3
import os

from evdev import InputDevice, ecodes
dev = InputDevice('/dev/input/event15')

with dev.grab_context():
    for event in dev.read_loop():
        if (event.code, event.value) == (ecodes.KEY_PAGEDOWN, 1):
            os.system('~/bin/page-turner next')
        elif (event.code, event.value) == (ecodes.KEY_PAGEUP, 1):
            os.system('~/bin/page-turner prior')
