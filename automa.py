
import pyautogui 
from pyautogui import *
import time as t
import os

listaDiretorio_atual = os.listdir(r'images\calcwin')
dic_posicoes = {}
#print(dic_posicoes)
indice_dic = []
posicao_dic = []
dic_op = {
    "+": 'adicao',
    "-": 'subtracao',
    "/": 'divisao',
    "*": 'mutiplicacao',
}
comandosAuto = []


class Automa():
    def automacao():
        #t.sleep(1)
        #pyautogui.hotkey('win','r')
        #t.sleep(2)
        #pyautogui.write('calc',0.1)
        #t.sleep(1)
        #pyautogui.press('enter')
        
        #Automa.localizar()
        #mouse()
        None
        
        
        
    def mouse(x,y):
        #pyautogui.click(x,y,clicks=1,interval=0.8,button='left')
        pyautogui.moveTo(x,y,0.3)
        pyautogui.click()


    def localizar():
        global dic_posicoes
        t.sleep(3)
        for i in listaDiretorio_atual:
            posicoes = list(pyautogui.locateCenterOnScreen(f'images\calcwin\{i}'))
            dic_posicoes[i] = posicoes
            print(dic_posicoes)
            print("ola")
            
    def receberComando(comando):
           
        for coman in comando:
            for nome in listaDiretorio_atual:
                if coman == str(nome[:-4]):
                    print("ola")
                
            
 



nomesa = 'Multipicacao.png'

#print(nomesa[-4:])
#print(listaDiretorio_atual)
    #posicao = (dic_posicoes.get('2.png'))


