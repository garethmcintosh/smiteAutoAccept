import pyautogui

print('Press Ctrl-C to quit.')
try:
    while True:
        pyautogui.click(x=943, y=666, clicks=1, interval=10, button='left')
except KeyboardInterrupt:
    print('Program stopped.')
