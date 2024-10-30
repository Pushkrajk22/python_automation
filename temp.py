# # to select and delete rows

import pyautogui as pg
import time
import keyboard

pg.FAILSAFE = True

# time.sleep(3)


# # for i in range(300):
# #     pg.scroll(-142)
# #     time.sleep(0.1)
# #     pg.click()

# #     time.sleep(0.1)

keyboard.wait("shift")
# for i in range(41):
#     pg.click()
#     time.sleep(0.1)

import os

# List of JSON filenames to create
filenames = [
    "CONTRACT MANAGEMENT",
    "SUPPLIER THIRD PARTY MANAGEMENT",
    "PROGRAM MANAGEMENT ",
    "OPERATIONS",
    "PROJECT MANAGEMENT",
    "PROJECT PREPARATION",
    "DEVOPS SETUP",
    "BUSINESS BLUEPRINT",
    "REALISATION",
    "FINAL PREPARATION",
    "GO LIVE AND SUPPORT",
    "TRANSITION PLANNING",
    "APPLICATION TRANSITION",
    "INFRASTRUCTURE SETUP",
    "SECURITY REGULATORY COMPLIANCE"
]

# Create each JSON file as an empty file
for filename in filenames:
    # with open(filename + ".json", 'w') as file:
    #     file.write(" ")  # Create an empty JSON object in each file
    os.remove(filename+".json")
