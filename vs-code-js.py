from adafruit_hid.keycode import Keycode

app = {
    'name' : 'VS Code: JS',
    'macros' : [
        # 1st row ----------
        (0x000405, 'd.qS', 'document.querySelector(\''),
        (0x000405, 'd.qSA', 'document.querySelectorAll(\''),
        (0x001317, 'fc', ['import { FC } from "react"', Keycode.ENTER, -Keycode.ENTER, Keycode.ENTER, -Keycode.ENTER, 'export const : FC = () => {', Keycode.ENTER, -Keycode.ENTER, 'return null', Keycode.UP_ARROW, -Keycode.UP_ARROW]),
        # 2nd row ----------
        (0x021d1e, 'i18n', ['{i18n.translate("")}', Keycode.LEFT_ARROW, -Keycode.LEFT_ARROW, Keycode.LEFT_ARROW, -Keycode.LEFT_ARROW, Keycode.LEFT_ARROW, -Keycode.LEFT_ARROW]),
        (0x153228, 'log', 'console.log('),
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
