from adafruit_hid.keycode import Keycode

app = {
    'name' : 'VS Code: SCSS',
    'macros' : [
        # 1st row ----------
        (0x3d0203, '@sm-on', '@include small-only {'),
        (0x361503, '@md-up', '@include medium-up {'),
        (0x361e02, '@lg-up', '@include large-up {'),
        # 2nd row ----------
        (0x3e1602, 'var()', 'var(--'),
        (0x000000, '', []),
        (0x000000, '', []),
        # 3rd row ----------
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),
        # 4th row ----------
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),
        # Encoder button ---
        (0x000000, '', [])
    ]
}
