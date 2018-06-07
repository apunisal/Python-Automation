#!/usr/bin/env python
# Using pyhton for searching stuff on webrowser 
# Package Used pyautogui

import pyautogui
import webbrowser
import time

try:

# User's input

  text = input("What you want to serarch : ")
  print(text)

# Open Browser

  str="https://www.google.com"
  webbrowser.open(str)

# Used to locate pointer position 
# print(pyautogui.position())

# Pause program till browser starts
  time.sleep(3) 

# search
  pyautogui.click(455,433)
  pyautogui.typewrite(text)
  pyautogui.typewrite(["enter"])
except:
  print(" ")
