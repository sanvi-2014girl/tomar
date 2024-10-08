from tkinter import *
#screen
window = Tk()
window.title("tkinter GUI")
window.geometry('500x500')
window.configure(bg='pink')
#add widgets
x = Label(text = "Hey welcome to codingal!",bg="#ff0000", fg = "white")
x.pack()
#entry
e = Entry(window,width= 30)
e.pack()
e2 = Entry(window,width= 30)
e2.pack()
#label
L = Label(window,text="",bg = "blue",fg="white",width = 50)
L.pack()
#btn function
def sayhello():
    num1 = int(e.get())
    num2 = int(e2.get())
    mul = num1*num2
    L.config(text="Result is:"+str(mul))
#btn
b = Button(window, text="click here!",command= sayhello)
b.pack()
window.mainloop()