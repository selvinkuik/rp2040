from adafruit_hid.keycode import Keycode

app = {
    'name' : 'Terminal: tmux',
    'macros' : [
        # 1st row ----------
        (0x3d0203, 'crp-rg', ['tmuxinator start corporate-register', Keycode.ENTER]),
        (0x361503, 'loquet', ['tmuxinator start loquet', Keycode.ENTER]),
        (0x361e02, 'recdek', ['tmuxinator start recdek-api', Keycode.ENTER]),
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
        (0x081920, '[kill]', [Keycode.CONTROL, 'c', -Keycode.CONTROL, 'tmuxinator stop ']),
        # Encoder button ---
        (0x000000, '', [])
    ]
}
