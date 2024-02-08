import tkinter as gui
from core import*
from fsmanager import* # file/string manager

root = gui.Tk()

#string_list = StringData()

chars = ScanFile(".dependencies\chars.txt")
strings = ScanFile(".dependencies\gui_text.txt")


def CollectWidgets(): # Function for retrieving checkbox values
    return [widget.get() for widget in(c1, c2, c3, c4, c5, c6)]


def GButton(): # Generate pwd button
    lbl1["text"] = GeneratePwd(s1.get(), CloneChars(chars, CollectWidgets()))


def MButton(): # Mix pwd button
    result = lbl1.cget(key="text")
    lbl1["text"] = MixSequence([result[i] for i in range(len(result))])


def RButton(): # Reverse pwd button
    lbl1["text"] = lbl1.cget(key="text")[::-1]


def PButton(): # Process pwd button
    lbl1["text"] = ProcessPwd(lbl1.cget(key="text"), CloneChars(chars, CollectWidgets()))


root.title(strings[0])
root.geometry("400x200+1000+200")
#root.resizable(False)
root.configure(bg="gray")
icon = gui.PhotoImage(file=".dependencies\Elite-icon.png")
root.iconphoto(False, icon)

lbl1 = gui.Label(text=" ", width=30, font="bold")
lbl1.place(x=10, y=10) # Вынужденное решениеz

btn1 = gui.Button(text=strings[7], activebackground="red", activeforeground="yellow", height=2, command=GButton).place(x=120, y=50)

btn2 = gui.Button(text=strings[8], activebackground="blue", activeforeground="yellow", height=2, width=4, command=MButton).place(x=200, y=50)

btn3 = gui.Button(text=strings[9], activebackground="green", activeforeground="yellow", height=2, width=4,command=RButton).place(x=250, y=50)

btn4 = gui.Button(text="HUI", command=PButton).place(x=300, y=50)

#btn4 = gui.Button(text=strings[9], activebackground="green", activeforeground="yellow", height=2, width=4,command=RDButton).place(x=300, y=50)


#btn3 = gui.Button(text=strings[9], activebackground="green", activeforeground="yellow", command=RDButton).place(x=110, y=100)

s1 = gui.IntVar()
c1 = gui.IntVar(value=1)
c2 = gui.IntVar(value=1)
c3 = gui.IntVar(value=1)
c4 = gui.IntVar(value=1)
c5 = gui.IntVar(value=1)
c6 = gui.IntVar(value=1)

slide = gui.Scale(orient="horizontal", from_=1, to=25, variable=s1).place(x=10, y=50)
s1.set(15)

cb1 = gui.Checkbutton(text=strings[1], variable=c1, offvalue=0, onvalue=1, width=15, anchor="w").place(x=160, y=130)

cb2 = gui.Checkbutton(text=strings[2], variable=c2, offvalue=0, onvalue=1, width=15, anchor="w").place(x=10, y=130)

cb3 = gui.Checkbutton(text=strings[3], variable=c3, offvalue=0, onvalue=1, width=15, anchor="w").place(x=10, y=100)

cb4 = gui.Checkbutton(text=strings[4], variable=c4, offvalue=0, onvalue=1, width=15, anchor="w").place(x=160, y=100)

cb5 = gui.Checkbutton(text=strings[5], variable=c5, offvalue=0, onvalue=1, width=15, anchor="w").place(x=160, y=160)

cb6 = gui.Checkbutton(text=strings[6], variable=c6, offvalue=0, onvalue=1, width=15, anchor="w").place(x=10, y=160)

#stestb = gui.Button(text="FJFjf").grid(column=0, row=7)


root.mainloop()
