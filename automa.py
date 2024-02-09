#import CalculadoraAuto as calc
import pyautogui 
from pyautogui import *
import time as t
import os


lista_posicoes = []


def localizar():
    diretorio_atual = os.listdir(r'C:\python\Prova\CalculadoraAuto\images\calcwin')
    for i in diretorio_atual:
        t.sleep(2)
   # None
   # t.sleep(4)
        posicoes = list(pyautogui.locateCenterOnScreen(f'C:\python\Prova\CalculadoraAuto\images\calcwin\{i}'))
        global lista_posicoes
        lista_posicoes.append(posicoes)
        
        print(posicoes)
   # #pyautogui.click(posicoes)
   # print(posicoes)
    

print(lista_posicoes)
t.sleep(4)
localizar()
print(lista_posicoes)
