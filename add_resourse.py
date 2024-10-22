import pyautogui as pg
import time
import keyboard
import json
import functions

pg.FAILSAFE = True

if __name__ =="__main__":
    # Read JSON data from a file
    with open('users.json', 'r') as file:
        users = json.load(file)

    keyboard.wait('shift')
    functions.locate_and_click(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\project_setup.png")
    functions.locate_and_click(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\additional_resources.png")
    time.sleep(4)
    functions.locate_and_click(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\add_user.png")
    time.sleep(2)
    pg.press('tab')
    pg.press('tab')
    pg.write("User Addition")
    functions.locate_and_click(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\save_blue.png")
    time.sleep(5)

    mail_button = pg.locateCenterOnScreen(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\resourse_mail_id.png", confidence=0.7)
    pg.click(mail_button.x, mail_button.y+50)
    
    #Loop through each user and extract 'mail' and 'role'
    for user in users["users"]:
        pg.write(user["mail"])
        time.sleep(0.2)
        for i in range(4):
            pg.press("tab")
            time.sleep(0.1)
        pg.write(user["role"])
        pg.press("tab")
        time.sleep(0.1)
        pg.press("tab")
        time.sleep(0.1)
    
    functions.locate_and_click(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\save_blue.png")
    time.sleep(7)

    functions.locate_and_click(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\submit_blue.png")
    time.sleep(1.5)

    functions.locate_and_click(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\ok_blue.png")
    time.sleep(0.5)

    functions.locate_and_click(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\complete_blue.png")
    