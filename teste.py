from tkinter import *

janela = Tk()
janela.title("Frame")
janela.geometry('320x250')


f_1 = Frame(janela, width=150, height=100, bg="blue")
f_1.grid(row=0, column=0, padx=5, pady=5)

f_2 = Frame(janela, width=150, height=100, bg="yellow")
f_2.grid(row=0, column=1,padx=5, pady=5)

f_3 = Frame(janela, width=150, height=100, bg="red")
f_3.grid(row=1, column=0,padx=5, pady=5)

f_4 = Frame(janela, width=150, height=100, bg="green")
f_4.grid(row=1, column=1,padx=5, pady=5)

# colocando itens no primeiro frame
l_1 = Label(f_1, text="Frame azul", width=22)
l_1.grid(column=0, row=0, stick=NSEW)

l_2 = Label(f_2, text="Frame amarela", width=22)
l_2.grid(column=0, row=0)

l_3 = Label(f_3, text="Frame vermelha", width=22)
l_3.grid(column=0, row=0, stick=NSEW)

l_4 = Label(f_4, text="Frame verde", width=22)
l_4.grid(column=0, row=0)

janela.mainloop()

# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# ttk.Button(frm, text="Ola").grid(column=2, row=1)
# btn = ttk.Button(frm,)

# fred = Button( text="ola",fg="yellow", bg="blue", )


# fred["fg"] = "red"
# fred["bg"] = "blue"
# fred.config(fg="red", bg="blue")
# fred.grid(column=2,row=2)

# print(btn.configure().keys())
# print(" ")
# print(set(btn.configure().keys()) - set(frm.configure().keys()))
# root.mainloop()
