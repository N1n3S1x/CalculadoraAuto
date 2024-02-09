import tkinter as tk
from tkinter import ttk

def click(label):
    label.configure(text=texto.get())

janela_principal = tk.Tk()
janela_principal.geometry('600x400+10+10')
janela_principal.title("Meu primeiro programa")

meu_label = ttk.Label(janela_principal)
meu_label.configure(text='Ola mundo', font=('Arial',40))
meu_label.pack(ipady=20)

texto = tk.StringVar()
caixa_texto = ttk.Entry(janela_principal)
caixa_texto.configure(textvariable=texto)
caixa_texto.pack(pady=20)

botao = ttk.Button(janela_principal)
botao.configure(text="Me aperte", command=lambda: click(meu_label))
botao.pack()
tk.mainloop()
