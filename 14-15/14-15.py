"""
from tkinter import*

def com(event):
    print("Вы нажали на ", event.keysym)

w = Tk()
w.geometry("150x50")

w.bind("<Key>", com)

t= Label(w, text="нажми на любую клавишу на калвиатуре")
t.pack()
w.mainloop()
"""

"""
from tkinter import*
from turtle import*

def com(event):
    if event.keysym == "Up":
        fd(10)
    if event.keysym == "Down":
        bk(10)
    if event.keysym == "Right":
        rt(45)
    if event.keysym == "Left":
        lt(45)
w=Tk()
w.geometry("150x50")

w.bind("<Key>", com)

t=Label(w,text="управляй черепашкой")
t.pack()

w.mainloop()
"""
"""
from tkinter import*
from turtle import*
width(5)
color("red")
up()
goto(-300,200)
down()

click = 1
def turtlemouv(event):
    global click
    click+=1
    t.config(text=click)

    if event.keysym == "Up":
        fd(10)
    if event.keysym == "Down":
        bk(10)
    if event.keysym == "Right":
        rt(45)
    if event.keysym == "Left":
        lt(45)

w=Tk()
w.geometry("200x130")

w.bind("<Key>", turtlemouv)

t=Label(w,text="Click")
t.pack()

w.mainloop()
"""

from tkinter import *


alphavit=["а", "б", "в", "г", "ґ", "д",
   "е", "є", "ж", "з", "и", "і",
   "ї", "й", "к", "л", "м", "н",
   "о", "п", "р", "с", "т", "у",
   "ф", "х", "ц", "ч", "ш", "щ",
   "ь", "ю", "я"]


def coding():
    symbol = e1.get()
    key = int(e2.get())

    if symbol not in alphavit:
        l3.config(text="Такой символ не существует")

    else:
        ind = alphavit.index(symbol) + key

        if ind > 32:
            cods = alphavit[ind-33]
            l3.config(text="Закодированый символ - " + cods)
        else:
            cods = alphavit[ind]
            l3.config(text="Закодированый символ - " + cods)


root = Tk()
root.geometry("200x160")
root.title("Код Цезаря")

l1 = Label(root, text="Код Цезаря ", fg="red")
l1.place(x=70,y=0)

l2 = Label(root, text="Введите символ")
l2.place(x=0,y=30)

e1 = Entry(root,width = 10)
e1.place(x=100,y=30)

l3 = Label(root, text="Введите ключ")
l3.place(x=0,y=60)

e2 = Entry(root,width = 10)
e2.place(x=100,y=60)


l3 = Label(root, text="Закодированый символ - ", fg = "blue" )
l3.place(x=0,y=90)

b1 = Button(root, text="Закодировать", command = coding)
b1.place(x=60,y=120)


root.mainloop()






















