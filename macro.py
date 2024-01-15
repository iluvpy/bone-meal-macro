from pynput import keyboard
from pynput.mouse import Button, Controller 
import threading
import time
import os

KEYBIND_SAVE_FILE = "keybind.txt"

class Macro:
    def __init__(self, keybind) -> None:
        self.mouse = Controller()
        self.running = False
        self.keybind = keybind
        self.macro_thr = threading.Thread(target=self.run)
        self.macro_thr.start()


    def keybind_pressed(self):
        self.running = not self.running

    def run(self):
        while True:
            if self.running:
                self.mouse.click(Button.right, 1) # place crop
                time.sleep(0.005)
                self.mouse.click(Button.right, 6) # bonemeal crop
                time.sleep(0.005)
                self.mouse.click(Button.left, 1) # break crop
                time.sleep(0.005)
            else: 
                time.sleep(.05)


def on_press_wrapper(macro: Macro):
    def on_press(key):
        try:
            k = key.char  # single-char keys
        except Exception:
            k = key.name  # other keys
        if k == macro.keybind:
            macro.keybind_pressed()
            print(f"macro: {'active' if macro.running else 'inactive'}")
    return on_press

keybind = None
if KEYBIND_SAVE_FILE not in os.listdir():
    while True:
        keybind = input("macro keybind (single letter or f1,f2,f3..): ")
        if not keybind.startswith("f") and len(keybind) > 1:
            print("please only use letters or f1-n keys")
            continue
        break

    save = input("Save this keybind? (y/n) ")
    if save == "y":
        with open(KEYBIND_SAVE_FILE, "w+") as f:
            f.write(keybind)
        print("keybind saved in 'keybind.txt', you can change it from there next time \n(remember to use the right format though)")
else:
    with open(KEYBIND_SAVE_FILE, "r") as f:
        keybind = f.read()

macro = Macro(keybind)
listener = keyboard.Listener(on_press=on_press_wrapper(macro))
listener.start()  # start to listen on a separate thread
listener.join()  # remove if main thread is polling self.keys