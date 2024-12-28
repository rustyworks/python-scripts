import pyautogui


# pyautogui.moveTo(1, 1)
width, height = pyautogui.size()
current_position = pyautogui.position()
if current_position == (1, 1):
    pyautogui.moveTo(width // 2, height // 2)
else:
    pyautogui.moveTo(1, 1)
