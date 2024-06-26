from adafruit_hid.keycode import Keycode

app = {
    'name' : 'Mac: Rectangle',
    'macros' : [
        # 1st row ----------
        (0x3d0203, '<', [Keycode.CONTROL, Keycode.OPTION, Keycode.LEFT_ARROW]),
        (0x361503, 'C', [Keycode.CONTROL, Keycode.OPTION, 'c']),
        (0x361e02, '>', [Keycode.CONTROL, Keycode.OPTION, Keycode.RIGHT_ARROW]),
        # 2nd row ----------
        (0x3e1602, '< 2/3', [Keycode.CONTROL, Keycode.OPTION, 'e']),
        (0x3f2d02, '[C]', [Keycode.CONTROL, Keycode.OPTION, Keycode.COMMAND, 'r', -Keycode.CONTROL, -Keycode.OPTION, -Keycode.COMMAND, 0.5, Keycode.CONTROL, Keycode.OPTION, 'c']),
        (0x1c2912, '> 2/3', [Keycode.CONTROL, Keycode.OPTION, 't']),
        # 3rd row ----------
        (0x0d221c, '< 1/3', [Keycode.CONTROL, Keycode.OPTION, 'd']),
        (0x0f1d1c, 'C 1/3', [Keycode.CONTROL, Keycode.OPTION, 'f']),
        (0x000000, '> 1/3', [Keycode.CONTROL, Keycode.OPTION, 'g']),
        # 4th row ----------
        (0x000000, '', []),
        (0x000000, '', []),
        (0x081920, '[Switch]', [Keycode.CONTROL, Keycode.OPTION, Keycode.COMMAND, Keycode.RIGHT_ARROW]),
        # Encoder button ---
        (0x000000, '', [])
    ]
}
