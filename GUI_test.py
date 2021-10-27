# -*- coding:utf-8 -*-
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry("200x200")

# this will create style object
style = Style()
# this will create a style and we'll name it W.TButton (ttk.Button)
style.configure('W.TButton', font=('calibri', 10, 'bold', 'underline'),
                foreground='red')
# affecting style to the button
btn1 = Button(root, text="Quit !",
              style="W.TButton",
              command=root.destroy)
btn1.grid(row=0, column=2, padx=50)
btn2 = Button(root, text="Click Me !!", command=None)
btn2.grid(row=1, column=2, pady=10, padx = 50)

root.mainloop()