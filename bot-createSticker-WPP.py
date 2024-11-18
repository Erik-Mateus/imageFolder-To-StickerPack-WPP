import pyautogui;
import os

from time import sleep

def criarFig():
    pyautogui.doubleClick (1294,150, duration = 0.5)
    pyautogui.click (1872,998, duration = 0.5)
    sleep(1)
    pyautogui.click(1585,825, duration = 0.5)
    pyautogui.click (1294,150, duration = 0.5)
    pyautogui.press('delete')


imgPastExisting = os.listdir("./IMgPACk")

for imgs in imgPastExisting:
    criarFig()
    

