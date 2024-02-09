# Arquivo do Julio Cezar

# Calculadora Automatizada

import tkinter as tk
from tkinter import *

import pyautogui_exemplo as atu

count = 0


def botao(nm, frm_):
    if nm == foto:

        tk.Button(frm_, image=nm, height=45, width=45).pack(side="right", padx=10)
        return nm
    elif nm == foto2:
        tk.Button(frm_, image=nm, height=45, width=45).pack(side="left", padx=10)
    elif nm == foto3:
        tk.Button(frm_, image=nm, height=45, width=45).pack(side="left", padx=10)
    elif nm == foto4:
        tk.Button(frm_, image=nm, height=45, width=45).pack(side="left", padx=10)
    elif nm == foto5:
        tk.Button(frm_, image=nm, height=45, width=45).pack(side="left", padx=10)
    elif nm == foto6:
        tk.Button(frm_, image=nm, height=45, width=45).pack(side="left", padx=10)
    else:
        btn = tk.Button(frm_, text=str(nm), width=5, height=3).pack(
            side="left", padx=10)

# janela Tk
janelaTk = tk.Tk()
janelaTk.geometry("280x450")
janelaTk.title("Caluladora revolucionária")

texto = tk.StringVar()
# Frame

frm = Frame(janelaTk, width=350, height=100, bg="blue", cursor="dot")
frm.grid(column=1, row=0, pady=10, padx=75)


frm2 = Frame(janelaTk, width=450, height=70, bg="blue")
frm2.grid(column=1, row=6, pady=5)

ferramentas = Frame(janelaTk, width=350, height=100)
ferramentas.grid(column=1, row=1, pady=10, padx=75)

teclasl1 = Frame(janelaTk, width=450, height=70)
teclasl1.grid(column=1, row=2, pady=5)

teclasl2 = Frame(janelaTk, width=450, height=70)
teclasl2.grid(column=1, row=3, pady=5)

teclasl3 = Frame(janelaTk, width=450, height=70)
teclasl3.grid(column=1, row=4, pady=5)

teclasl4 = Frame(janelaTk, width=450, height=70)
teclasl4.grid(column=1, row=5, pady=5)

tptcl = (teclasl1, teclasl2, teclasl3, teclasl4)
# label

label = tk.Label(janelaTk)
label.grid(column=4, row=2)

# lista de botões
foto = PhotoImage(file="Prova\images\divisao.png") 
foto2 = PhotoImage(file="Prova\images\maisoumenos.png")
foto3 = PhotoImage(file=r"Prova\images\backspace.png")
foto4 = PhotoImage(file=r"Prova\images\sub.png")
foto5 = PhotoImage(file=r"Prova\images\multipl.png")
foto6 = PhotoImage(file=r"Prova\images\add.png")


foto = foto.subsample(15, 15)
foto2 = foto2.subsample(15, 15)
foto3 = foto3.subsample(15, 15)
foto4 = foto4.subsample(15, 15)
foto5 = foto5.subsample(15, 15)
foto6 = foto6.subsample(15, 15)

#   Caixa de texto

caixa_texto = tk.Entry(frm)

caixa_texto.configure(textvariable=texto)
caixa_texto.pack(pady=20)
# Lista de Botões

for i in range(0, 3):
    for n in range(1, 4):
        count += 1
        botao(count, tptcl[i])
        
# Botões
botao(foto, teclasl4)
botao(foto2, teclasl4)
botao(foto3, ferramentas)

botao(foto4, teclasl2)
botao(foto5, teclasl3)
botao(foto6, teclasl1)

botao("0", teclasl4)
botao(",", teclasl4)
tk.Button(frm2, text="Automatizar",command=atu.automacao).pack()

janelaTk.mainloop()
