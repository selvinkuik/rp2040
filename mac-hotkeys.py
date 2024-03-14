from adafruit_hid.keycode import Keycode

app = {
    'name' : 'Mac: HotKeys',
    'macros' : [
        # 1st row ----------
        (0x3d0203, 'Chrome', [Keycode.COMMAND, Keycode.OPTION, '3']),
        (0x361503, 'Docker', [Keycode.COMMAND, Keycode.OPTION, '8']),
        (0x361e02, 'Finder', [Keycode.COMMAND, Keycode.OPTION, '1']),
        # 2nd row ----------
        (0x3e1602, 'Fork', [Keycode.COMMAND, Keycode.OPTION, '2']),
        (0x3f2d02, 'Missive', [Keycode.COMMAND, Keycode.OPTION, '4']),
        (0x1c2912, 'Slack', [Keycode.COMMAND, Keycode.OPTION, '5']),
        # 3rd row ----------
        (0x0d221c, 'Term.', [Keycode.COMMAND, Keycode.OPTION, '6']),
        (0x0f1d1c, 'VS Code', [Keycode.COMMAND, Keycode.OPTION, '7']),
        (0x000000, '', []),
        # 4th row ----------
        (0x11171d, '[<Tab]', [Keycode.COMMAND, Keycode.SHIFT, '[']),
        (0x11171d, '[Tab>]', [Keycode.COMMAND, Keycode.SHIFT, ']']),
        (0x081920, '[Cycle]', [Keycode.COMMAND, '`']),
        # Encoder button ---
        (0x000000, '', [])
    ]
}
