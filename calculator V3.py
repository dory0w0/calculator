from tkinter import *
window= Tk()
window.geometry("365x410")
window.config(bg="#e5e18c")
window.title("calculator")
iconj = PhotoImage(file="calc.png")
window.iconphoto(True,iconj)
window.config()

screen = Entry()
screen.place(x=50, y=30)
screen.config(font=("arial",25),width=15,)

def num1():
    screen.insert(END, "1")
B1 = Button(window,text="1",font=("arial",25))
B1.config(command=num1)
B1.pack()
B1.place(x=50, y=100)
def num2():
    screen.insert(END, "2")
B2 = Button(window,text="2",font=("arial",25))
B2.config(command=num2)
B2.pack()
B2.place(x=110, y=100)
def num3():
    screen.insert(END, "3")
B3 = Button(window,text="3",font=("arial",25))
B3.config(command=num3)
B3.pack()
B3.place(x=170, y=100)
def num4():
    screen.insert(END, "4")
B4 = Button(window,text="4",font=("arial",25))
B4.config(command=num4)
B4.pack()
B4.place(x=50, y=180)
def num5():
    screen.insert(END, "5")
B5 = Button(window,text="5",font=("arial",25))
B5.config(command=num5)
B5.place(x=110, y=180)
def num6():
    screen.insert(END, "6")
B6 = Button(window,text="6",font=("arial",25))
B6.config(command=num6)
B6.place(x=170, y=180)
def num7():
    screen.insert(END, "7")
B7 = Button(window,text="7",font=("arial",25))
B7.config(command=num7)
B7.place(x=50, y=260)
def num8():
    screen.insert(END, "8")
B8 = Button(window,text="8",font=("arial",25))
B8.config(command=num8)
B8.place(x=110, y=260)
def num9():
    screen.insert(END, "9")
B9 = Button(window,text="9",font=("arial",25))
B9.config(command=num9)
B9.place(x=170, y=260)
def num0():
    screen.insert(END, "0")
B0 = Button(window,text="0",font=("arial",25))
B0.config(command=num0)
B0.place(x=110, y=340)

def addition():
    screen.insert(END, "+")
Badd = Button(window,text="+",font=("arial",25))
Badd.config(command=addition)
Badd.place(x=230, y=100)

def subtraction():
    screen.insert(END, "-")
Bsub = Button(window,text="-",font=("arial",25))
Bsub.config(command=subtraction)
Bsub.place(x=230, y=180)

def multiplication():
    screen.insert(END, "*")
Bmul = Button(window,text="*",font=("arial",25))
Bmul.config(command=multiplication)
Bmul.place(x=230, y=260)

def clearn():
    screen.delete("0", END)
clear = Button(window,text="AC",font=("arial",25))
clear.config(command=clearn)
clear.place(x=281, y=190)

def shwresult():
    result = eval(screen.get())
    screen.delete("0", END)
    screen.insert(END, result)
resultb = Button(window,text="=",font=("arial",25))
resultb.config(command=shwresult)
resultb.place(x=170, y=340)

def backspace():
    screen.delete(len(screen.get())-1)
Bback = Button(window,text="⌫",font=("arial",25))
Bback.config(command=backspace)
Bback.place(x=281, y=270)

window.mainloop()