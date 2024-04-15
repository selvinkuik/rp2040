from adafruit_hid.keycode import Keycode

app = {
    'name' : 'Mac: HotKeys',
    'macros' : [
        # 1st row ----------
        (0x3d0203, 'Bscamp', [Keycode.COMMAND, Keycode.OPTION, '1']),
        (0x361503, 'Chrome', [Keycode.COMMAND, Keycode.OPTION, '5']),
        (0x361e02, 'Docker', [Keycode.COMMAND, Keycode.OPTION, '2']),
        # 2nd row ----------
        (0x3e1602, 'Finder', [Keycode.COMMAND, Keycode.OPTION, '3']),
        (0x3f2d02, 'Fork', [Keycode.COMMAND, Keycode.OPTION, '4']),
        (0x1c2912, 'Missive', [Keycode.COMMAND, Keycode.OPTION, '6']),
        # 3rd row ----------
        (0x0d221c, 'Slack', [Keycode.COMMAND, Keycode.OPTION, '7']),
        (0x0f1d1c, 'Term.', [Keycode.COMMAND, Keycode.OPTION, '8']),
        (0x000000, 'VS Code', [Keycode.COMMAND, Keycode.OPTION, '9']),
        # 4th row ----------
        (0x11171d, '[<Tab]', [Keycode.COMMAND, Keycode.SHIFT, '[']),
        (0x11171d, '[Tab>]', [Keycode.COMMAND, Keycode.SHIFT, ']']),
        (0x081920, '[Cycle]', [Keycode.COMMAND, '`']),
        # Encoder button ---
        (0x000000, '', [])
    ]
}
