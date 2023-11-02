import pyautogui
import time
import keyboard
import win32api, win32con

nombre = "matias"

apellido = "cassero lombardi"

dni = "43627827"

url = "https://docs.google.com/forms/d/e/1FAIpQLSdQp76cRFGK42BL2JtOTPZRrzilBI_jdZLc6QMZjTzZgX9FYQ/viewform"

def sleep (dur) :
    time.sleep(dur)

def click (x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    sleep(0.3)

def escDNI () :
    for caracter in dni :
        pyautogui.press(caracter)
        

def escribir (valor) :
    lastCar = ""
    for caracter in valor :
        if caracter == " ":
            pyautogui.press('space')
        if lastCar == " " or lastCar == "" :
            pyautogui.keyDown('shift')
            pyautogui.press(caracter)
            pyautogui.keyUp('shift')
        else :
            pyautogui.press(caracter)
        lastCar = caracter

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
    escribir(nombre)
    pyautogui.press('tab')
    escribir(apellido)
    pyautogui.press('tab')
    escDNI()
    pyautogui.press('tab')
    pyautogui.press('right', presses=4)
    pyautogui.press('tab', presses=3)
    pyautogui.press('enter')


sleep(3)

probar()