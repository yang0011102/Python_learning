# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 16:22:12 2018

@author: yang
"""

import tkinter as tk
window= tk.Tk()
window.title('None')
window.geometry('200x200')

var1=tk.StringVar()
l=tk.Label(window,bg='white',
           width=5,
           textvariable=var1)
l.pack()

def print_sel():
    value=lb.get(lb.curselection())
    var1.set(value)

but1=tk.Button(window,text='print_sel',
              command=print_sel)
but1.pack()

var2=tk.StringVar()
var2.set((11,5,23))
lb=tk.Listbox(window,listvariable=var2)
list_items=[123,'g',123,321]
for i in list_items:
    lb.insert('end',i)
lb.pack()

window.mainloop()