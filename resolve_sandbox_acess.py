import pyautogui as pg
import time

pg.FAILSAFE = True

def locate_and_click(image_path):
    time.sleep(0.1)
    located_button = pg.locateCenterOnScreen(image_path, confidence=0.8)
    pg.moveTo(located_button, duration=0.1)  # Move to the button smoothly over 1 second
    pg.click()  # Click the left mouse button
    time.sleep(0.2)

def resolve_state():
    # Locate the center of the image on the screen
    state_button = pg.locateCenterOnScreen(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\state.png", confidence=0.8)
    
    # Check if the button was found
    if state_button is not None:
            pg.moveTo(state_button, duration=0.5)  # Move to the button smoothly over 1 second
            pg.click()  # Click the left mouse button
            time.sleep(0.2)
            resolved_button = pg.locateCenterOnScreen(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\resolved.png", confidence=0.8)
            pg.moveTo(resolved_button, duration=0.5)  # Move to the button smoothly over 1 second
            pg.click()  # Click the left mouse button
            #pg.hotkey("ctrl","v")
            time.sleep(0.2)

def fill_resolution_info():
    time.sleep(0.2)
    #resolution information
    locate_and_click(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\resolution_information.png")
    
    #Resolution Code
    locate_and_click(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\resolution_code.png")
    locate_and_click(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\solved_permanently.png")

    #Issue Type
    locate_and_click(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\issue_type.png")
    locate_and_click(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\authorization-role.png")

    #Resolution Notes
    locate_and_click(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\resolution_notes.png")
    message = "Access has been provided"

    pg.write(message)
    time.sleep(0.2)

    #type of resolution
    locate_and_click(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\type_of_resolution.png")

    locate_and_click(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\permanent_fix.png")

    #functional area
    locate_and_click(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\functional_area.png")
    pg.press('U')
    pg.press('enter')

    #process area
    time.sleep(0.2)
    process_area_button = pg.locateCenterOnScreen(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\process_area.png", confidence=0.93)
    pg.moveTo(process_area_button, duration=0.2)  # Move to the button smoothly over 1 second
    pg.click()  # Click the left mouse button
    time.sleep(0.1)
    pg.press('A')
    pg.press('enter')


def resolve_ticket():
    locate_and_click(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\resolve.png")


def add_customer_comments():
    locate_and_click(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\notes.png")
    locate_and_click(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\customer_comments.png")
    message = """Hello,
        Your access to the Test System has been successfully created and
        assigned Project Manager role to Test Project_UT project. You can now begin utilizing
        the system and all its features.
        URL to Test system : https://test.deliverycentralplatform.ibm.com/digite/Request?Key=login , you need to use IBM Internet id/password to login.
        Request to go through below links prior to use Test/sandbox:
        IDCP Enablement Microsite https://w3.ibm.com/w3publisher/cse/ibm-delivery-central-platform
        I have shared the URL of test system and also Please to go through
        enablement
        (demos, published and under development courses are listed there)
        Thanks!!"""

    message2="""Hello,
        Your access to the Test System has been successfully created and assigned the Project Manager role for the Test Project_UT project. You can now begin utilizing the system and all its features.

        URL to Test system: https://test.deliverycentralplatform.ibm.com/digite/Request?Key=login. 
        You will need to use your IBM Internet ID/password to log in.

        Please go through the following links prior to using the Test/Sandbox:

        IDCP Enablement Microsite: https://w3.ibm.com/w3publisher/cse/ibm-delivery-central-platform
        (Demos, published, and under-development courses are listed there)
        For raising tickets in the future, we recommend using the following link:
        http://support.deliverycentralplatform.ibm.com/

        Thanks!"""
    
    pg.write(message2)
    time.sleep(7)



if __name__ =="__main__":
    time.sleep(3)
    pg.scroll(1500)
    time.sleep(0.3)
    resolve_state()
    pg.scroll(-900)
    add_customer_comments()
    fill_resolution_info()
    resolve_ticket()