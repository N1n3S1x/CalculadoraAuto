import pyautogui
from pyautogui import *
import time as t
import os
import psutil as psutil
from psutil import *
import pygetwindow as gw

listaDiretorio_atual = os.listdir(r"images\calcwin")
dic_posicoes = {}
# print(dic_posicoes)
indice_dic = []
posicao_dic = []
dic_op = {
    "+": "adicao",
    "-": "subtracao",
    "/": "divisao",
    "*": "mutiplicacao",
}
comandosAuto = []


class Automa:
    def automacao():

        nomes_processos = [i.name() for i in psutil.process_iter()]
        janela = gw.getWindowsWithTitle("calculadora")
        # Verifica se o proesso da Calculadora esteja em Execução
        if "CalculatorApp.exe" in nomes_processos:
            # Altena para a janela da Calculadora, Caso o Processo esteja em Execução
            if janela:
                # Focar na janela do processo
                janela[1].activate()

                # Aguardar um curto período para garantir que o foco tenha mudado
                t.sleep(2)
        else:
            t.sleep(1)
            pyautogui.hotkey("win", "r")
            t.sleep(2)
            pyautogui.write("calc", 0.1)
            t.sleep(1)
            pyautogui.press("enter")
            print("CalculatorApp.exe" in (i.name() for i in psutil.process_iter()))
        Automa.localizar()
        Automa.mouse()

    def mouse():
        t.sleep(0.7)
        # pyautogui.click(x,y,clicks=1,interval=0.8,button='left')
        for c in comandosAuto:
            x, y = dic_posicoes.get(f"{c}.png")
            pyautogui.moveTo(x, y, 0.3)
            pyautogui.click()
        t.sleep(0.5)
        pyautogui.press('enter')
        return

    def localizar():
        global comandosAuto
        global dic_posicoes
        t.sleep(3)
        for i in listaDiretorio_atual:
            posicoes = list(pyautogui.locateCenterOnScreen(f"images\calcwin\{i}", confidence=0.8))
            dic_posicoes[i] = posicoes

        #  x , y = posicoesComan[0], posicoesComan[1]
        #return Automa.mouse(x, y)

        print(comandosAuto)
        print(dic_posicoes)
        #print(x,y)

    def receberComando(comando):

        for coman in comando:
            # print(coman)
            for nome in listaDiretorio_atual:
                if coman == str(nome[:-4]):
                    numeros = coman
                    comandosAuto.append(numeros)

                    None
            if coman in dic_op:
                operacao = dic_op.get(coman)
                comandosAuto.append(operacao)
                # print(comandosAuto)

            else:
                None
        # Apagar
        if comando == "apagar":
            del comandosAuto[-1]

        return comandosAuto


# Automa.localizar()
