import pyautogui as pg
import time
import keyboard

def locate_and_click(image_path):
    time.sleep(0.1)
    try:
        located_button = pg.locateCenterOnScreen(image_path, confidence=0.8)
        if located_button is not None:
            pg.moveTo(located_button, duration=0.1)
            pg.click()  # Click the left mouse button
            time.sleep(0.2)
    except Exception as e:
         print("Error from locate_and_click: Image not find to click")

    return located_button
