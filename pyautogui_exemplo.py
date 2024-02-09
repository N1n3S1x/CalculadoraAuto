import pyautogui
import time

def automacao():
    time.sleep(3)
    # Movendo o mouse para uma posição inicial
    pyautogui.moveTo(100, 100, duration=1)  # Mova o mouse para as coordenadas (100, 100) durante 1 segundo

    # Arrastando o mouse para uma nova posição
    pyautogui.dragTo(200, 200, duration=1)  # Arraste o mouse para as coordenadas (200, 200) durante 1 segundo

    # Aguardando por alguns segundos
    time.sleep(2)

    # Enviando comandos do teclado
    pyautogui.typewrite("Olá, mundo!", interval=0.1)  # Digita o texto com um intervalo de 0.1 segundo entre cada caractere

    # Pressionando e segurando uma tecla
    pyautogui.keyDown('shift')

    # Digitando algumas teclas enquanto a tecla shift está pressionada
    pyautogui.typewrite(['a', 'b', 'c'])

    # Liberando a tecla shiftOl, mu
    pyautogui.keyUp('shift')

    # Aguardando antes de encerrar o script
    time.sleep(2)

    # Movendo o mouse de volta para a posição inicial
    pyautogui.moveTo(100, 100, duration=1)

    # Encerrando o script
    pyautogui.alert("Script concluído. Pressione OK para sair.")

