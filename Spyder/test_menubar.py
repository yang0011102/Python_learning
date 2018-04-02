# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 11:26:10 2018

@author: yang
"""

import tkinter as tk
window=tk.Tk()
window.title('canvas')
window.geometry('200x200')

l=tk.Label(window,bg='white',
           text='empty')
l.pack()

c=10
def puls1():
    global c
    c=c+1
    l.config(text='now '+str(c))
def del1():
    global c
    c=c-1
    l.config(text='now '+str(c))
def new():
    global c
    c=10
    l.config(text='now '+str(c))
menubar=tk.Menu(window)
filemenu=tk.Menu(menubar)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='+++',command=puls1)
filemenu.add_command(label='---',command=del1)
filemenu.add_separator()
filemenu.add_command(label='new',command=new)
filemenu.add_separator()
filemenu.add_command(label='exit',command=window.quit)

window.config(menu=menubar)

window.mainloop()
