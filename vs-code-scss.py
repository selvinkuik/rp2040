from adafruit_hid.keycode import Keycode

app = {
    'name' : 'VS Code: SCSS',
    'macros' : [
        # 1st row ----------
        (0x000405, '@sm-on', '@include medium-up {'),
        (0x000405, '@lg-dn', '@include large-down {'),
        (0x001317, '@lg-up', '@include large-up {'),
        # 2nd row ----------
        (0x021d1e, 'var()', 'var(--'),
        (0x153228, '&__', '&__'),
        (0x403410, '&--', '&--'),
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
