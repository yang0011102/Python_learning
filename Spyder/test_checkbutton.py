# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 10:42:52 2018

@author: yang
Checkbutton 勾选
"""
import tkinter as tk
window=tk.Tk()
window.title('Checkbutton')
window.geometry('200x200')

l=tk.Label(window,width=20,
           bg='white',
           text='Checkbutton')
l.pack()

def print_sel():
    if   (var1.get()==1)&(var2.get()==1):
        l.config(text='都是')
    elif (var1.get()==0)&(var2.get()==1):
        l.config(text='选项2')
    elif (var1.get()==1)&(var2.get()==0):
        l.config(text='选项1')
    else: 
        l.config(text='都不')
var1=tk.IntVar()
ck1=tk.Checkbutton(window,text='选项1',
                   variable=var1,
                   onvalue=1,offvalue=0,
                   command=print_sel)
ck1.pack()
var2=tk.IntVar()
ck2=tk.Checkbutton(window,text='选项2',
                   variable=var2,
                   onvalue=1,offvalue=0,
                   command=print_sel)
ck2.pack()
window.mainloop()
