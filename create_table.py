import pyautogui as pg
import time
#for 8-% screen

# Wait for 5 seconds to allow you to focus the correct window
time.sleep(5)

def add_column():
        time.sleep(0.5)
    # Locate the center of the image on the screen
    #add_column_button = pg.locateCenterOnScreen(r"C:\Users\PushkrajKulkarni\Pictures\Screenshots\add_column.jpg", confidence=0.6)

    # Print the coordinates of the button found
    #print(add_column_button)

    # Check if the button was found
    #if add_column_button is not None:
        pg.moveTo(1656, 103, duration=1)  # Move to the button smoothly over 1 second
        pg.click()  # Click the left mouse button
        time.sleep(2)
        #add_coluumn_name_button = pg.locateCenterOnScreen(r"C:\Users\PushkrajKulkarni\Pictures\Screenshots\column_name.jpg", confidence=0.7)
        pg.moveTo(350, 650, duration=1)  # Move to the button smoothly over 1 second
        pg.click()  # Click the left mouse button
        pg.hotkey("ctrl","v")
        time.sleep(0.3)

    # else:
    #     print("Button not found on screen.")

def select_column_type():
        time.sleep(0.5)
    # Locate the center of the image on the screen
    #select_column_type_button = pg.locateCenterOnScreen(r"C:\Users\PushkrajKulkarni\Pictures\Screenshots\column_type.jpg", confidence=0.7)

    # Print the coordinates of the button found
    #print(select_column_type_button)

    # Check if the button was found
    #if select_column_type_button is not None:
        pg.moveTo(316, 711, duration=1)  # Move to the button smoothly over 1 second
        pg.click()  # Click the left mouse button
    # else:
    #     print("Button not found on screen.")

def select_datatype():
        time.sleep(0.5)
    # select_datatype_button = pg.locateCenterOnScreen(r"C:\Users\PushkrajKulkarni\Pictures\Screenshots\data_type.jpg", confidence=0.7)
    # # Check if the button was found
    # if select_datatype_button is not None:
        pg.moveTo(760, 850, duration=1)  # Move to the button smoothly over 1 second
        pg.click()  # Click the left mouse button
        
        time.sleep(0.3)
        pg.press('enter')
    # else:
    #     print("Button not found on screen.")

def add_literal():
        time.sleep(0.5)
    #select_datatype_button = pg.locateCenterOnScreen(r"C:\Users\PushkrajKulkarni\Pictures\Screenshots\literal.jpg", confidence=0.7)
    # Check if the button was found
    #if select_datatype_button is not None:
        pg.moveTo(615, 715, duration=1)  # Move to the button smoothly over 1 second
        pg.click()  # Click the left mouse button


        time.sleep(0.3)

        pg.moveTo(761, 510, duration=1)  # Move to the button smoothly over 1 second
        pg.click()  # Click the left mouse button
        time.sleep(0.5)
    #else:
    #   print("Button not found on screen.")

#main
        
time.sleep(7)

for i in range(70):
    time.sleep(0.2)
    print("====iteration ",i+1,"========")
    # Press the Down arrow key
    pg.press('down')
    time.sleep(0.5)
    # Press the Left arrow key
    pg.press('left')
    time.sleep(0.5)
    # Press Ctrl+C to copy
    pg.hotkey('ctrl', 'c')

    # Press Alt+Tab to switch to the other application
    pg.hotkey('alt', 'tab')

    time.sleep(1)

    #add CM AddTable1

    pg.moveTo(1656, 103, duration=1)  # Move to the button smoothly over 1 second
    pg.click()  # Click the left mouse button
    time.sleep(2)

    #add name
    pg.moveTo(350, 650, duration=1)  # Move to the button smoothly over 1 second
    pg.click()  # Click the left mouse button
    pg.hotkey("ctrl","v")
    time.sleep(0.3)

    select_column_type()

    #select_datatype()

    pg.moveTo(770, 845, duration=1)  # Move to the button smoothly over 1 second
    pg.click()  # Click the left mouse button
    
    pg.moveTo(754, 509, duration=1)  # Move to the button smoothly over 1 second
    pg.click()  # Click the left mouse button

    time.sleep(1)
    pg.hotkey('alt', 'tab')
    
    time.sleep(0.5)
    pg.press('right')
    time.sleep(0.5)

    pg.hotkey('ctrl', 'c')
    time.sleep(0.5)

    pg.hotkey('alt', 'tab')
    time.sleep(0.5)

    #add_literal()

    pg.moveTo(650, 715, duration=1)  # Move to the button smoothly over 1 second
    pg.click()  # Click the left mouse button

    pg.hotkey('ctrl', 'v')

    #save_button = pg.locateCenterOnScreen(r"C:\Users\PushkrajKulkarni\Pictures\Screenshots\save.jpg", confidence=0.7)
    pg.moveTo(1633, 973, duration=1)  # Move to the button smoothly over 1 second
    pg.click()
    time.sleep(5)

    pg.hotkey('alt', 'tab')

