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

def select_datatype(type):
    datatype_button = locate_and_click(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\Data_type.png", confidence=0.88)
    pg.moveTo(datatype_button.x+100,datatype_button.y,duration=.02)
    pg.click()
    pg.write(type)


def select_calculated_column():
    calculated_buton = pg.locateCenterOnScreen(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\custom.png", confidence=0.9)  
    pg.moveTo(calculated_buton.x+20,calculated_buton.y-15, duration=0.5)
    pg.click()


def select_custom_column():
    custom_button = pg.locateCenterOnScreen(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\custom.png", confidence=0.8)  
    pg.moveTo(custom_button.x+20,custom_button.y+15, duration=0.5)
    pg.click()


def add_column(name,type,literal=None):
    time.sleep(1)
    locate_and_click(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\add_column.png")


    #column name
    name_button = locate_and_click(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\column_name.jpg",confidence=0.87)
    pg.moveTo(name_button.x+100,name_button.y)
    pg.click()
    pg.write(name)

    #column type
    if type in {"Calculated", "calculated"}:
        select_calculated_column()
        
        #type literal
        literal_button = locate_and_click(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\literal.png", confidence=0.85)
        pg.moveTo(literal_button.x+100, literal_button.y)
        pg.click()
        pg.write(literal)
        time.sleep(0.7)

        #select datatype as string
        select_datatype("string")


    elif type in {"Custom", "custom"}:
        select_custom_column()
        
        #select datatype as string
        select_datatype("string")
    time.sleep(0.5)
    locate_and_click(r"C:\Users\PushkrajKulkarni\IDCP\Automation\images\save.png")
    time.sleep(2)



if __name__ == "__main__":
    time.sleep(3)

    #format {"column name": ("Calculated/custom", "__literal"), ...}
    columns = {
    "Change Management Load": (
        "Calculated",
        "__FORMULA__RUNAPI(1,LOADGLOBALLINKEDMASTERLISTMAP,Org;;#Org ID#;;PMST_f;;Configuration Management Plan;;ChangeManagement;;All;Data;Element;Detail;;Concat;;true)"
    ),
    "Change Management Fetch": (
        "Calculated",
        "__FORMULA__RUNAPI(1,FETCHCHILDLOOKUPVALUES,Org;;#Org ID#;;PMST_f;;Configuration Management Plan;;ChangeManagement;;All;Data;Element;Detail;Concat;;All;;LOV)"
    ),
    "Change Management Sorted String": (
        "Calculated",
        "__FORMULA__RUNAPI(1,GETSORTEDSTRINGVALUES,REPLACE(#Change Management Fetch#,;,--);;STRING;;--;;1)"
    ),

    "Change Management AddTableRow1": (
    "Calculated",
    "__FORMULA__RUNAPI(EQ(GETEFORMACTION(),LOAD),ADDTABLEROW,Prj;;#OWNERID#;;#ITEMTYPE#;;#ITEMID#;;Configuration Management Plan;;ChangeManagement;;;;0;;;;Y;;Element$$GETSTRPART(GETSTRPART(#Change Management Sorted String#,--,0),@$,1)@@Detail$$GETSTRPART(GETSTRPART(#Change Management Sorted String#,--,0),@$,2))"
    ),

    "Change Management AddTableRow2": (
    "Calculated",
    "__FORMULA__RUNAPI(EQ(GETEFORMACTION(),LOAD),ADDTABLEROW,Prj;;#OWNERID#;;#ITEMTYPE#;;#ITEMID#;;Configuration Management Plan;;ChangeManagement;;;;0;;;;Y;;Element$$GETSTRPART(GETSTRPART(#Change Management Sorted String#,--,1),@$,1)@@Detail$$GETSTRPART(GETSTRPART(#Change Management Sorted String#,--,1),@$,2))"
    ),

    "Change Management AddTableRow3": (
    "Calculated",
    "__FORMULA__RUNAPI(EQ(GETEFORMACTION(),LOAD),ADDTABLEROW,Prj;;#OWNERID#;;#ITEMTYPE#;;#ITEMID#;;Configuration Management Plan;;ChangeManagement;;;;0;;;;Y;;Element$$GETSTRPART(GETSTRPART(#Change Management Sorted String#,--,2),@$,1)@@Detail$$GETSTRPART(GETSTRPART(#Change Management Sorted String#,--,2),@$,2))"
    ),

    "Change Management AddTableRow4": (
    "Calculated",
    "__FORMULA__RUNAPI(EQ(GETEFORMACTION(),LOAD),ADDTABLEROW,Prj;;#OWNERID#;;#ITEMTYPE#;;#ITEMID#;;Configuration Management Plan;;ChangeManagement;;;;0;;;;Y;;Element$$GETSTRPART(GETSTRPART(#Change Management Sorted String#,--,3),@$,1)@@Detail$$GETSTRPART(GETSTRPART(#Change Management Sorted String#,--,3),@$,2))"
    ),

    "Change Management AddTableRow5": (
    "Calculated",
    "__FORMULA__RUNAPI(EQ(GETEFORMACTION(),LOAD),ADDTABLEROW,Prj;;#OWNERID#;;#ITEMTYPE#;;#ITEMID#;;Configuration Management Plan;;ChangeManagement;;;;0;;;;Y;;Element$$GETSTRPART(GETSTRPART(#Change Management Sorted String#,--,4),@$,1)@@Detail$$GETSTRPART(GETSTRPART(#Change Management Sorted String#,--,4),@$,2))"
    )
    }
    for column in columns:
        add_column(column, columns[column][0], columns[column][1])