from adafruit_hid.keycode import Keycode

app = {
    'name' : 'Chrome',
    'macros' : [
        # 1st row ----------
        (0x000405, 'Dv tls', [Keycode.COMMAND, Keycode.OPTION, 'i']),
        (0x000405, 'Inspct', [Keycode.COMMAND, Keycode.SHIFT, 'c']),
        (0x001317, 'Dck ps', [Keycode.COMMAND, Keycode.SHIFT, 'd']),
        # 2nd row ----------
        (0x021d1e, 'Mob br', [Keycode.COMMAND, Keycode.SHIFT, 'm']),
        (0x153228, 'Bkmk br', [Keycode.COMMAND, Keycode.SHIFT, 'b']),
        (0x000000, '', []),
        # 3rd row ----------
        (0x301f00, '[<Tab]', [Keycode.COMMAND, '[']),
        (0x000000, '', []),
        (0x250c01, '[Tab>]', [Keycode.COMMAND, ']']),
        # 4th row ----------
        (0x000000, '', []),
        (0x1f0708, '[Reload]', [Keycode.COMMAND, 'R']),
        (0x1f0708, '[Focus]', [Keycode.COMMAND, Keycode.OPTION, '5']),
        # Encoder button ---
        (0x000000, '', [])
    ]
}
