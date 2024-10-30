#Add Fields in the segment 
'''This program is capable of adding field and configuring its type as checkbox or Dropdown...
    This needs a json of the input according to which the field will be configured
    Capable of creating a dropdown field and adding values to the list
'''
import pyautogui as pg
import time
import keyboard
import json
import functions

pg.FAILSAFE = True

def move_and_click(x,y,msg):
    pg.moveTo(x, y, duration=0.5) 
    pg.click()  # Click the left mouse button
    time.sleep(0.5)
    pg.write(msg)
    time.sleep(0.5)
    print("clicked", msg)

if __name__ =="__main__":
    #time.sleep(3)  #Instead of waiting 3 sec we can take our own time to navigate andpress caps lock to start
    keyboard.wait('shift')
    fields = [ {'label':"CIC", "datatype":"String", "controltype":'Radio Button', "displaylength":"", "displayheight":"", 'inputlength':"250", "drop":"true", "values":["GIC", "LA"]}
              ]
    
    for field in fields :
        keyboard.wait('shift')

        # label = 910,350
        move_and_click(910,350,field["label"])

        # datatype = 700 , 560
        move_and_click(700,560,field["datatype"])
        
        # controltype =1430,560
        move_and_click(1430,560,field["controltype"])

        if field["drop"] == "true":
            time.sleep(0.5)
            pg.scroll(-500)
            time.sleep(0.5)

            for value in field["values"]:
                #Add values 670 , 320
                pg.click(670, 320)
                time.sleep(0.3)
                pg.write(value)
                time.sleep(0.5)
                print(value)

                #click 660, 365
                pg.click(660,365)
                time.sleep(0.5)
                

        pg.moveTo(1600,380)
        pg.click()
        time.sleep(0.5)
        pg.scroll(-1500)
        time.sleep(0.5)

        move_and_click(1430,560,field["controltype"])
        print("controltype")

        # display lenght 720 , 720
        move_and_click(715,715,field["displaylength"])
        print("displaylength")

        # ddisplayheight 1420 , 720
        move_and_click(1460,710,field["displayheight"])
        print("displayheight")

        # input length 720, 850
        move_and_click(720,850,field["inputlength"])
        print("inputlength")

        #save 1392, 956
        pg.click(1392,956)