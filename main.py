import pyautogui
import time

comment = "XD"


time.sleep(5)
for i in range(10):
    pyautogui.typewrite(comment)
    pyautogui.typewrite("\n")
    time.sleep(2)