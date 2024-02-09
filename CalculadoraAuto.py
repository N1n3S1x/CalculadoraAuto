# Arquivo do Julio Cezar

# Calculadora Automatizada

import tkinter as tk
from tkinter import *

from operator import *
import operator as op
from tkinter import ttk

import pyautogui_exemplo as atu

count = 0


# cores
cor1 = "#feffff"  # white/branca
cor2 = "#38576b"
cor3 = "#ECEFF1"
cor4 = "#FFAB40"  # Orange/laranja


# Dicionário de operadores

dic_op = {
    "+": op.add,
    "-": op.sub,
    "/": op.truediv,
    "*": op.mul,
}


# função do Botão


def botao(nm, frm_):
    if nm == foto:
        # Divisão
        tk.Button(
            frm_,
            image=nm,
            command=lambda: entrarValores("/"),
            height=45,
            width=55,
            bg=cor4,
        ).pack(side="right")
    elif nm == foto2:
        # Mais ou Menos
        tk.Button(
            frm_,
            image=nm,
            command=lambda: entrarValores(""),
            height=45,
            width=55,
            bg=cor4,
        ).pack(side="left")
    elif nm == foto3:
        # Apagar
        tk.Button(
            frm_,
            image=nm,
            height=45,
            command=lambda: entrarValores("apagar"),
            width=55,
            bg=cor4,
        ).pack(side="left")
    elif nm == foto4:
        # Subtração
        tk.Button(
            frm_,
            image=nm,
            height=45,
            command=lambda: entrarValores("-"),
            width=55,
            bg=cor4,
        ).pack(side="left")
    elif nm == foto5:
        # Multiplicação
        tk.Button(
            frm_,
            image=nm,
            height=45,
            command=lambda: entrarValores("*"),
            width=55,
            bg=cor4,
        ).pack(side="left")
    elif nm == foto6:
        # Adição
        tk.Button(
            frm_,
            image=nm,
            height=45,
            command=lambda: entrarValores("+"),
            width=55,
            bg=cor4,
        ).pack(side="left", padx=4)
    # elif nm == ",":
    # Virgula
    #    tk.Button(
    #        frm_,text=str(nm),height=2,width=5,font="Ivy 13 bold",relief=RAISED,overrelief=RIDGE,bg=cor4).pack(side="left", padx=5)
    else:
        # Botões
        btn = tk.Button(
            frm_,
            text=str(nm),
            command=lambda: entrarValores(nm),
            height=2,
            width=5,
            font="Ivy 13 bold",
            relief=RAISED,
            overrelief=RIDGE,
        ).pack(side="left", padx=5)


# janela Tk
janelaTk = tk.Tk()
janelaTk.geometry("280x370")
janelaTk.title("Caluladora revolucionária")
janelaTk.configure(background=cor2)


#
ttk.Separator(janelaTk, orient=HORIZONTAL).grid(row=1, column=1, ipadx=135, pady=3)
ttk.Separator(janelaTk, orient=HORIZONTAL).grid(row=6, column=1, ipadx=135, pady=5)


#


# Frame

tela = Frame(janelaTk, width=280, height=70, bg=cor2, cursor="dot")
tela.grid(column=1, row=0, pady=10)

frm_tecl = Frame(janelaTk, width=280, background=cor2).grid(column=1, row=2)

frm2 = Frame(janelaTk, width=280, height=70, background=cor2)
frm2.grid(
    column=1,
    row=7,
    # pady=5,
)

# ferramentas = Frame(frm_tecl, width=280, height=100)
# ferramentas.grid(column=1, row=1, pady=10, padx=75)

teclasl1 = Frame(frm_tecl, background=cor2)
teclasl1.grid(column=1, row=2)

teclasl2 = Frame(frm_tecl, background=cor2)
teclasl2.grid(column=1, row=3)

teclasl3 = Frame(frm_tecl, background=cor2)
teclasl3.grid(column=1, row=4)

teclasl4 = Frame(frm_tecl, background=cor2)
teclasl4.grid(column=1, row=5)

tptcl = (teclasl1, teclasl2, teclasl3, teclasl4)


# texto label
valorVariavel = StringVar()


# label
app_tela = Label(
    tela,
    textvariable=valorVariavel,
    width=19,
    height=3,
    padx=7,
    relief="flat",
    anchor="e",
    bd=0,
    justify=RIGHT,
    font=("Ivy 18 "),
    bg="#37474F",
    fg=cor1,
)
app_tela.place(x=0, y=0)

# lista de botões
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

#   Caixa de texto

# caixa_texto = tk.Entry(tela)

# caixa_texto.configure(textvariable=texto)
# caixa_texto.pack(pady=20)
# Lista de Botões

for i in range(0, 3):
    for n in range(1, 4):
        count += 1
        botao(count, tptcl[i])

# Botões
botao(foto, teclasl4)
# botao(foto2, teclasl4)
botao(foto3, teclasl1)

botao(foto4, teclasl2)
botao(foto5, teclasl3)
botao(foto6, teclasl4)

botao("0", teclasl4)
botao(",", teclasl4)
tk.Button(frm2, text="Automatizar", command=atu.automacao).pack()


# Memória Calculadora
todosValores = ""


def entrarValores(event):
    global todosValores
    if event == "apagar":

        todosValores = todosValores[:-1]
        valorVariavel.set(todosValores)
    else:
        todosValores += str(event)
        # resultado = eval(todosValores)
        valorVariavel.set(todosValores)


janelaTk.mainloop()
