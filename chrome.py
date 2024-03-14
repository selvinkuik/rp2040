from adafruit_hid.keycode import Keycode

app = {
    'name' : 'Chrome',
    'macros' : [
        # 1st row ----------
        (0x3d0203, 'Dv tls', [Keycode.COMMAND, Keycode.OPTION, 'i']),
        (0x361503, 'Inspct', [Keycode.COMMAND, Keycode.SHIFT, 'c']),
        (0x361e02, 'Dck ps', [Keycode.COMMAND, Keycode.SHIFT, 'd']),
        # 2nd row ----------
        (0x3e1602, 'Mob br', [Keycode.COMMAND, Keycode.SHIFT, 'm']),
        (0x3f2d02, 'Bkmk br', [Keycode.COMMAND, Keycode.SHIFT, 'b']),
        (0x000000, '', []),
        # 3rd row ----------
        (0x0d221c, '[<Tab]', [Keycode.COMMAND, '[']),
        (0x000000, '', []),
        (0x0f1d1c, '[Tab>]', [Keycode.COMMAND, ']']),
        # 4th row ----------
        (0x000000, '', []),
        (0x11171d, '[Reload]', [Keycode.COMMAND, 'R']),
        (0x081920, '[Focus]', [Keycode.COMMAND, Keycode.OPTION, '3']),
        # Encoder button ---
        (0x000000, '', [])
    ]
}
