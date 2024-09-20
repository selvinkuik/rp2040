from adafruit_hid.keycode import Keycode

app = {
    'name' : 'Mac: HotKeys',
    'macros' : [
        # 1st row ----------
        (0x000405, 'Bscamp', [Keycode.COMMAND, Keycode.OPTION, '1']),
        (0x000405, 'Chrome', [Keycode.COMMAND, Keycode.OPTION, '5']),
        (0x001317, 'Docker', [Keycode.COMMAND, Keycode.OPTION, '2']),
        # 2nd row ----------
        (0x021d1e, 'Finder', [Keycode.COMMAND, Keycode.OPTION, '3']),
        (0x153228, 'Fork', [Keycode.COMMAND, Keycode.OPTION, '4']),
        (0x403410, 'Mimest.', [Keycode.COMMAND, Keycode.OPTION, '6']),
        # 3rd row ----------
        (0x301f00, 'Slack', [Keycode.COMMAND, Keycode.OPTION, '7']),
        (0x281500, 'Term.', [Keycode.COMMAND, Keycode.OPTION, '8']),
        (0x250c01, 'VS Code', [Keycode.COMMAND, Keycode.OPTION, '9']),
        # 4th row ----------
        (0x230604, '[<Tab]', [Keycode.COMMAND, Keycode.SHIFT, '[']),
        (0x1f0708, '[Cycle]', [Keycode.COMMAND, '`']),
        (0x1f0708, '[Tab>]', [Keycode.COMMAND, Keycode.SHIFT, ']']),
        # Encoder button ---
        (0x000000, '', [])
    ]
}
