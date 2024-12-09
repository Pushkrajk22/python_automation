import pyautogui as pg
import time
import keyboard
import pyperclip

pg.FAILSAFE = True

pg.PAUSE = 0.5

def paste_clipboard_on_tab_v():
    while True:
        # Check if 'Tab' and 'V' are pressed together
        if keyboard.is_pressed('tab') and keyboard.is_pressed('v'):
            if keyboard.is_pressed('v'):
                # Get the text from the clipboard
                clipboard_text = pyperclip.paste()
                pg.write(clipboard_text)  # Print the clipboard content
                # Wait a little to avoid multiple prints in one key press
                keyboard.wait('tab')  # Wait for the 'Tab' key to be released

while True:
    keyboard.wait('tab','v')
    # Start the function
    paste_clipboard_on_tab_v()
