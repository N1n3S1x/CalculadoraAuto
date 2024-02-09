
import CalculadoraAuto
import tkinter as tk
from tkinter import *

from operator import *
import operator as op
from tkinter import ttk

import pyautogui_exemplo as atu




foto = PhotoImage(file="images\divisao.png")
foto2 = PhotoImage(file="images\maisoumenos.png")
foto3 = PhotoImage(file=r"images\backspace.png")
foto4 = PhotoImage(file=r"images\sub.png")
foto5 = PhotoImage(file=r"images\multipl.png")
foto6 = PhotoImage(file=r"images\add.png")


foto = foto.subsample(15, 15)
foto2 = foto2.subsample(15, 15)
foto3 = foto3.subsample(15, 15)
foto4 = foto4.subsample(15, 15)
foto5 = foto5.subsample(15, 15)
foto6 = foto6.subsample(15, 15)


count = 0

def botao(nm, frm_):
    
    # Botões
    btn = tk.Button(
        f'CalculadoraAuto.{frm_}',
        text=str(nm),
        command=lambda: CalculadoraAuto.entrarValores(nm),
        height=2,
        width=5,
        font="Ivy 13 bold",
        relief=RAISED,
        overrelief=RIDGE,
    ).pack(side="left", padx=5)
    
    return None

   
tk.Button(CalculadoraAuto.frm2, text="Automatizar", command=atu.automacao).pack()

for i in range(0, 3):
    for n in range(1, 4):
        count += 1
        botao(count, CalculadoraAuto.tptcl[i])
            
            
            
