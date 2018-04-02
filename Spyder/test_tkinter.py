# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 10:38:17 2018

@author: yang

用于在spyder中测试tkinter
当前python版本：Anaconda3.6
"""
import tkinter as tk

window=tk.Tk()
window.title('a window')
window.geometry('200x100')

var=tk.StringVar()
#------------
label=tk.Label(window,textvariable=var,
               bg='white',
               font=('Arial',12),
               width=15,height=2)
label.pack()
#--------------
pb=False
def hit():
    global pb
    if pb==False:
        pb=True
        var.set('yep')
    else:
        pb=False
        var.set('nope')
b=tk.Button(window,text='test',
                 width='15',
                 height='2',
                 command=hit)
b.pack()


window.mainloop()
