from adafruit_hid.keycode import Keycode

app = {
    'name' : 'Mac: Rectangle',
    'macros' : [
        # 1st row ----------
        (0x000405, '<', [Keycode.CONTROL, Keycode.OPTION, Keycode.LEFT_ARROW]),
        (0x000405, 'C', [Keycode.CONTROL, Keycode.OPTION, 'c']),
        (0x001317, '>', [Keycode.CONTROL, Keycode.OPTION, Keycode.RIGHT_ARROW]),
        # 2nd row ----------
        (0x021d1e, '< 2/3', [Keycode.CONTROL, Keycode.OPTION, 'e']),
        (0x153228, '[C]', [Keycode.CONTROL, Keycode.OPTION, Keycode.COMMAND, 'r', -Keycode.CONTROL, -Keycode.OPTION, -Keycode.COMMAND, 0.5, Keycode.CONTROL, Keycode.OPTION, 'c']),
        (0x403410, '> 2/3', [Keycode.CONTROL, Keycode.OPTION, 't']),
        # 3rd row ----------
        (0x301f00, '< 1/3', [Keycode.CONTROL, Keycode.OPTION, 'd']),
        (0x281500, 'C 1/3', [Keycode.CONTROL, Keycode.OPTION, 'f']),
        (0x250c01, '> 1/3', [Keycode.CONTROL, Keycode.OPTION, 'g']),
        # 4th row ----------
        (0x000000, '', []),
        (0x000000, '', []),
        (0x1f0708, '[Switch]', [Keycode.CONTROL, Keycode.OPTION, Keycode.COMMAND, Keycode.RIGHT_ARROW]),
        # Encoder button ---
        (0x000000, '', [])
    ]
}
