import pyautogui as pg
import time
import keyboard

def locate_and_click(image_path, confidence = 0.8):
    time.sleep(0.1)
    located_button = pg.locateCenterOnScreen(image_path, confidence= confidence)
    pg.moveTo(located_button, duration=0.1)
    pg.click()  # Click the left mouse button
    time.sleep(0.2)
    return located_button
