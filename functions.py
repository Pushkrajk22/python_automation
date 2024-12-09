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


def locate_and_click(image_path, retries=3, confidence=0.8):
    time.sleep(0.1)
    for attempt in range(retries):
        try:
            located_button = pg.locateCenterOnScreen(image_path, confidence=confidence)
            if located_button:
                pg.moveTo(located_button, duration=0.1)
                pg.click()
                return True  # Successful click
            else:
                print(f"Attempt {attempt + 1}: Button not found: {image_path}")
        except Exception as e:
            print(f"Attempt {attempt + 1}: Error locating or clicking image {image_path}: {e}")
        
        time.sleep(2)  # Wait for 1 second before retrying

    print(f"Failed to locate or click image {image_path} after {retries} attempts.")
    return False  # Return False after failing multiple attempts
