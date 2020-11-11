from pynput.keyboard import Key, Controller
import time

Keyboard = Controller()

time.sleep(5)
while True:
    for letter in "Ура":
        Keyboard.press(letter)
        Keyboard.release(letter)
    Keyboard.press(Key.enter)
