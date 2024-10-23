import pyautogui as pg
import time

pg.FAILSAFE = True


def locate_and_click(image_path, confidence=0.8):
    time.sleep(0.1)
    located_button = pg.locateCenterOnScreen(image_path,confidence=confidence)
    pg.moveTo(located_button, duration=0.5)  # Move to the button smoothly over 1 second
    pg.click()  # Click the left mouse button
    time.sleep(0.2)
    return located_button


def add_table(table_name):
    #locate_and_click(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\add_table.png", confidence=0.9)
    table_name_button = locate_and_click(r"images\table_name.png",confidence=0.85)
    pg.click(table_name_button.x+100,table_name_button.y)
    pg.write(table_name)
    time.sleep(0.3)

if __name__ == "__main__":
    time.sleep(2)
    add_table("Configuration_Management")