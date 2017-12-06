#!/usr/bin/python
#Referenz: https://www.tutorialspoint.com/python/python_gui_programming.htm

from Tkinter import * # for python2
#import tkinter # for python3

top = Tk()
var = StringVar()
label = Label( top, textvariable=var, relief=RAISED )

num = 1

def helloCallBack():
	global num

	if (num):
		var.set("Hey!? How are you doing?")
		label.pack()
		num = 0
	else:
		var.set("Good and you ?")
		label.pack()
		num = 1
		

B = Button(top, text="Hello", command = helloCallBack)

B.pack()

top.mainloop()
