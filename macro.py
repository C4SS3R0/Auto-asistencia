import pyautogui
import time
import keyboard
import win32api, win32con

def sleep (dur) :
    time.sleep(dur)

def click (x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    sleep(0.3)

def nombre () :
    pyautogui.keyDown('shift')
    pyautogui.press('m')
    pyautogui.keyUp('shift')
    pyautogui.press('a')
    pyautogui.press('t')
    pyautogui.press('i')
    pyautogui.press('a')
    pyautogui.press('s')

def apellido () :
    pyautogui.keyDown('shift')
    pyautogui.press('c')
    pyautogui.keyUp('shift')
    pyautogui.press('a')
    pyautogui.press('s', presses=2)
    pyautogui.press('e')
    pyautogui.press('r')
    pyautogui.press('o')
    pyautogui.press('space')
    pyautogui.keyDown('shift')
    pyautogui.press('l')
    pyautogui.keyUp('shift')
    pyautogui.press('o')
    pyautogui.press('m')
    pyautogui.press('b')
    pyautogui.press('a')
    pyautogui.press('r')
    pyautogui.press('d')
    pyautogui.press('i')

def dni () :
    pyautogui.press('4')
    pyautogui.press('3')
    pyautogui.press('6')
    pyautogui.press('2')
    pyautogui.press('7')
    pyautogui.press('8')
    pyautogui.press('2')
    pyautogui.press('7')

def probar () :
    pyautogui.hotkey('alt', 'tab')
    pyautogui.hotkey('ctrl', 't')
    sleep(0.2)
    click(1203, 118)
    click(1179, 186)
    click(1335, 179)
    click(1581, 392)
    sleep(3)
    pyautogui.press('tab', presses=3)
    nombre()
    pyautogui.press('tab')
    apellido()
    pyautogui.press('tab')
    dni()
    pyautogui.press('tab')
    pyautogui.press('right', presses=4)
    pyautogui.press('tab', presses=3)
    # pyautogui.press('enter')


sleep(5)

probar()