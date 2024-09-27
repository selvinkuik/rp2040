from adafruit_hid.keycode import Keycode

app = {
    'name' : 'VS Code: Liquid',
    'macros' : [
        # 1st row ----------
        (0x000405, '{%', '{% '),
        (0x000405, '{%-', ['{%-', Keycode.RIGHT_ARROW, '-', Keycode.LEFT_ARROW, -Keycode.LEFT_ARROW, Keycode.LEFT_ARROW, Keycode.SPACE]),
        (0x001317, '{{ | t', ['{{  | t', Keycode.LEFT_ARROW, -Keycode.LEFT_ARROW, Keycode.LEFT_ARROW, -Keycode.LEFT_ARROW, Keycode.LEFT_ARROW, -Keycode.LEFT_ARROW, Keycode.LEFT_ARROW, -Keycode.LEFT_ARROW, "'"]),
        # 2nd row ----------
        (0x000000, '', []),
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
