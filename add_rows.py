import pyautogui as pg
import time
import keyboard
import json

pg.FAILSAFE = True

def locate_and_click(image_path, confidence=0.7):
    time.sleep(0.1)
    located_button = pg.locateCenterOnScreen(image_path, confidence=confidence)
    pg.moveTo(located_button, duration=0.1)
    pg.click()  # Click the left mouse button
    time.sleep(0.2)
    return located_button
    

def add_row(activity, selection):
    # Image file to locate
    image_selection = r"C:\Users\PushkrajKulkarni\Pictures\Screenshots\DESC.png"
    image_activity = r"C:\Users\PushkrajKulkarni\Pictures\Screenshots\Screenshot 2024-10-18 185012.png"

    #filling activity
    button = locate_and_click(image_activity)
    pg.click(button.x-200,button.y)
    pg.write(activity)
    time.sleep(2)

    for i in selection:
        locate_and_click(image_activity)
        pg.write(i)
        time.sleep(0.2)

def add_row_manually(activity, selection):

    pg.write(activity)
    time.sleep(0.8)

    for i in selection:
        pg.press("tab")
        pg.write(i)
        time.sleep(0.09)
    
    pg.press("tab")
    time.sleep(0.09)
    pg.press("tab")
    time.sleep(0.09)
    pg.press("tab")
    time.sleep(0.09)
    pg.press("tab")
    time.sleep(0.09)
    pg.press("tab")
    


if __name__ =="__main__":

    file_names = [

    "APPLICATION_TRANSITION",
   
    ]

    for file in file_names:

        print(file)
        print()    
        #time.sleep(3)  #Instead of waiting 3 sec we can take our own time to navigate andpress caps lock to start
        keyboard.wait("shift")

        # Read the data from the file
        with open(f"{file}.json", 'r') as file:
            data = json.load(file)

        for row in data["rows"]:
            activity = row["activity"]  
            selection = row["selection"]
            #print(f"Activity: {activity}, Selection: {selection}")

            add_row_manually(activity, selection)