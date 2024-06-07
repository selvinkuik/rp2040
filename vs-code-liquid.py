from adafruit_hid.keycode import Keycode

app = {
    'name' : 'VS Code: Shopify',
    'macros' : [
        # 1st row ----------
        (0x3d0203, '{%', '{% '),
        (0x361503, '{%-', ['{%-', Keycode.RIGHT_ARROW, '-', Keycode.LEFT_ARROW, -Keycode.LEFT_ARROW, Keycode.LEFT_ARROW, Keycode.SPACE]),
        (0x361e02, '{{ | t', ['{{  | t', Keycode.LEFT_ARROW, -Keycode.LEFT_ARROW, Keycode.LEFT_ARROW, -Keycode.LEFT_ARROW, Keycode.LEFT_ARROW, -Keycode.LEFT_ARROW, Keycode.LEFT_ARROW, -Keycode.LEFT_ARROW, "'"]),
        # 2nd row ----------
        (0x3e1602, 'i18n', ['{i18n.translate("")}', Keycode.LEFT_ARROW, -Keycode.LEFT_ARROW, Keycode.LEFT_ARROW, -Keycode.LEFT_ARROW, Keycode.LEFT_ARROW, -Keycode.LEFT_ARROW]),
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
