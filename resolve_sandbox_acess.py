import pyautogui as pg
import time
import keyboard

pg.FAILSAFE = True

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

def resolve_state():
    # Locate the center of the image on the screen
    state_button = pg.locateCenterOnScreen(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\state.png", confidence=0.8)
    
    # Check if the button was found
    if state_button is not None:
            pg.moveTo(state_button.x+100, state_button.y, duration=0.1) 
            pg.click()  # Click the left mouse button
            time.sleep(0.1)
            
            pg.write("Resolved")

            time.sleep(0.1)
            pg.press('enter')


def fill_resolution_info():
    time.sleep(0.1)
    #resolution information
    locate_and_click(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\resolution_information.png")
    
    #Resolution Code
    locate_and_click(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\resolution_code.png")
    pg.write("Solved (Permanently)")
    time.sleep(0.1)
    pg.press('enter')
    
    #Issue Type
    locate_and_click(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\issue_type.png")
    pg.write("Authorization/Role")
    time.sleep(0.1)
    pg.press('enter')
    
    #Resolution Notes
    locate_and_click(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\resolution_notes.png")
    pg.write("Access has been provided")
    time.sleep(0.12)

    #type of resolution
    locate_and_click(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\type_of_resolution.png")
    pg.write("Permanent Fix")
    time.sleep(0.1)
    pg.press('enter')
    
    #functional area
    locate_and_click(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\functional_area.png")
    pg.write("UT")
    pg.press('enter')

    #process area
    time.sleep(0.1)
    process_area_button = pg.locateCenterOnScreen(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\process_area.png", confidence=0.93)
    pg.moveTo(process_area_button, duration=0.2)  # Move to the button smoothly over 1 second
    pg.click()  # Click the left mouse button
    time.sleep(0.1)
    pg.write("Authorization/Role")
    pg.press('enter')


def resolve_ticket():
    locate_and_click(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\resolve.png")


def add_customer_comments(tool):
    locate_and_click(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\notes.png")
    locate_and_click(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\customer_comments.png")    
    
    link_to_new_ticketing_tool = None

    if tool == "New":
        link_to_new_ticketing_tool = """For raising tickets in the future, we recommend using the below link:
        https://support.deliverycentralplatform.ibm.com/"""

    message=f"""Hello,
        Your access to the Test System has been successfully created and assigned the Project Manager role for the Test Project_UT project. 
        You can now begin utilizing the system and all its features.

        URL to Test system: https://test.deliverycentralplatform.ibm.com/digite/Request?Key=login. 
        You will need to use your IBM Internet ID/password to log in.

        Please go through the following links prior to using the Test/Sandbox:

        IDCP Enablement Microsite: https://w3.ibm.com/w3publisher/cse/ibm-delivery-central-platform
        (Demos, published, and under-development courses are listed there)
        {link_to_new_ticketing_tool}

        Thanks!"""

    pg.write(message)
    time.sleep(7)



if __name__ =="__main__":
    #time.sleep(3)  #Instead of waiting 3 sec we can take our own time to navigate andpress caps lock to start
    keyboard.wait('shift')
    ticketing_tool = pg.confirm(text='Which platform the ticket is raised from?', title='', buttons=['Old', 'New'])
    time.sleep(0.2)
    pg.scroll(1500)     # To ensure top of the page
    time.sleep(0.2)
    resolve_state()

    pg.scroll(-900)
    add_customer_comments(ticketing_tool)

    fill_resolution_info()
    #resolve_ticket()