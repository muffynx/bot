import pyautogui
import time

URL = "https://addons.mozilla.org/th/firefox/addon/urban-vpn/"

# Open Firefox with profile 01
pyautogui.press('win')
pyautogui.typewrite('Firefox')
pyautogui.press('enter')
time.sleep(2)
pyautogui.hotkey('alt', 'd')
pyautogui.typewrite(URL)
pyautogui.press('enter')
time.sleep(3)

# Send ESC key to Firefox
pyautogui.press('esc')
time.sleep(1)

# Run python.py
pyautogui.hotkey('win', 'r')
pyautogui.typewrite('cmd')
pyautogui.press('enter')
time.sleep(1)
pyautogui.typewrite('python python.py')
pyautogui.press('enter')
time.sleep(1)

# Start 2bat.bat
pyautogui.hotkey('win', 'r')
pyautogui.typewrite('cmd')
pyautogui.press('enter')
time.sleep(1)
pyautogui.typewrite('2bat.bat')
pyautogui.press('enter')
