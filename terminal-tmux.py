from adafruit_hid.keycode import Keycode

app = {
    'name' : 'Terminal: tmux',
    'macros' : [
        # 1st row ----------
        (0x000405, 'cibyn', ['tmuxinator start call-it-by-your-name', Keycode.ENTER]),
        (0x000405, 'crp-rg', ['tmuxinator start corporate-register', Keycode.ENTER]),
        (0x001317, 'loquet', ['tmuxinator start loquet', Keycode.ENTER]),
        # 2nd row ----------
        (0x021d1e, 'recdek', ['tmuxinator start recdek-api', Keycode.ENTER]),
        (0x000000, '', []),
        (0x000000, '', []),
        # 3rd row ----------
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),
        # 4th row ----------
        (0x230604, '[<Tab]', [Keycode.CONTROL, 'b', -Keycode.CONTROL, Keycode.UP_ARROW]),
        (0x1f0708, '[kill]', [Keycode.CONTROL, 'c', -Keycode.CONTROL, 'tmuxinator stop ']),
        (0x1f0708, '[Tab>]', [Keycode.CONTROL, 'b', -Keycode.CONTROL, Keycode.DOWN_ARROW]),
        # Encoder button ---
        (0x000000, '', [])
    ]
}
