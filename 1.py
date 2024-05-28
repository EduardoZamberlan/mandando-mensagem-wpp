import pyautogui
import time

pyautogui.hotkey('win',  'r')

time.sleep(1)

pyautogui.press('backspace')

time.sleep(1)

pyautogui.write('control panel')

time.sleep(1)

pyautogui.press('enter')