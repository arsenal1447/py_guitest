#!/usr/bin/python

import tkinter
import tkinter.messagebox

top = tkinter.Tk()
# Code to add widgets will go here...
# def helloCallBack():
#     tkinter.messagebox.showinfo("Hello Python","Hello World")
#
# B = tkinter.Button(top,text="Hello Python,人生苦短，我用python",command = helloCallBack())
#
# B.pack()
C = tkinter.Canvas(top,bg = "grey",height = 250,width = 300)

coord = 10,50,240,210
arc = C.create_arc(coord,start=0,extent = 150,fill= "yellow")

C.pack()

top.mainloop()