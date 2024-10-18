import pyautogui as pg
import time

pg.FAILSAFE = True

time.sleep(4)


for i in range(300):
    pg.scroll(-142)
    time.sleep(0.1)
    pg.click()

    time.sleep(0.1)