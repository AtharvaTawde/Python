import pyautogui
import time

def openGmail():
    string = 'Namrata76'
    print(pyautogui.position())
    pyautogui.click(599, 1057)
    time.sleep(0.5)
    pyautogui.click(262, 7)
    time.sleep(0.5)
    pyautogui.write(string, interval=0.02)
    pyautogui.press('enter')
    time.sleep(0.5)

def openOddyseyware():
    print(pyautogui.position())
    pyautogui.click(599, 1057)
    time.sleep(0.5)
    pyautogui.click(262, 7)
    time.sleep(0.5)
    pyautogui.typewrite('du', interval=0.005)
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(0.5)

def sendEmail():
    print(pyautogui.position())
    pyautogui.doubleClick(1303, 1059)
    time.sleep(3)
    pyautogui.typewrite('aaryantawde0817', interval=0.1)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.typewrite('Namrata76', interval=0.1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.typewrite('atharvatawde894')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    for i in range(4):
        pyautogui.typewrite('This is an automated message', interval=0.1)
        pyautogui.press('enter')
        time.sleep(1)
    pyautogui.click(555, 445)
    time.sleep(3)
    pyautogui.press('r')
sendEmail()