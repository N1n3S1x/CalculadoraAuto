#import CalculadoraAuto as calc
import pyautogui 
from pyautogui import *
import time as t
import os

diretorio_atual = os.listdir(r'images\calcwin')
dic_posicoes = {}
indice = []
posicao = []


def automacao():
    t.sleep(1)
    pyautogui.hotkey('win','r')
    t.sleep(2)
    pyautogui.write('calc',0.1)
    t.sleep(1)
    pyautogui.press('enter')
    
    
def mouse(x,y):
    #pyautogui.click(x,y,clicks=1,interval=0.8,button='left')
    pyautogui.moveTo(x,y,0.3)
    pyautogui.click()


def localizar():
    global dic_posicoes
    t.sleep(3)
    for i in diretorio_atual:
        posicoes = list(pyautogui.locateCenterOnScreen(f'images\calcwin\{i}'))
        dic_posicoes[i] = posicoes 



#automacao()
localizar()

posicao = (dic_posicoes.get('2.png'))


print(x,y)