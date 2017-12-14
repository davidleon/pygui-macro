import time
from pynput import keyboard, mouse

current_time = 0
scripts = []


def on_mouse_move(x, y):
    print(x, y)


def on_mouse_click(x, y, button, pressed):
    print(x, y, button, pressed)


def on_mouse_scroll(x, y, dx, dy):
    print(x, y, dx, dy)


def on_key_press(key):
    """
    begin的时候设置当前时间
    :param key:
    :return:
    """
    global scripts
    if '_name_' in key.__dict__:
        char = key._name_
    elif 'char' in key.__dict__:
        char = key.char
    else:
        char = None

    print(char)

    global current_time
    scripts.append(' '.join(['KEY_PRESS', str(int(time.time()) - current_time), 'None' if char is None else char]))
    current_time = int(time.time())

    if key == keyboard.Key.esc:
        return False


def on_key_release(key):
    global scripts
    if '_name_' in key.__dict__:
        char = key._name_
    elif 'char' in key.__dict__:
        char = key.char
    else:
        char = 'None'

    global current_time
    scripts.append(' '.join(['KEY_RELEASE', str(int(time.time()) - current_time), 'None' if char is None else char]))
    current_time = int(time.time())


def set_current_time():
    global current_time
    current_time = int(time.time())


def get_scripts():
    global scripts
    return scripts
