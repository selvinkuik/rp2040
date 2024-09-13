from adafruit_hid.keycode import Keycode

app = {
    'name' : 'Numpad',
    'macros' : [
        # 1st row ----------
        (0x000405, '7', ['7']),
        (0x000405, '8', ['8']),
        (0x001317, '9', ['9']),
        # 2nd row ----------
        (0x021d1e, '4', ['4']),
        (0x153228, '5', ['5']),
        (0x403410, '6', ['6']),
        # 3rd row ----------
        (0x301f00, '1', ['1']),
        (0x281500, '2', ['2']),
        (0x250c01, '3', ['3']),
        # 4th row ----------
        (0x230604, '0', ['0']),
        (0x1f0708, '[Bcksp].', [Keycode.BACKSPACE]),
        (0x1f0708, '[Enter]', [Keycode.ENTER]),
        # Encoder button ---
        (0x000000, '', [])
    ]
}
