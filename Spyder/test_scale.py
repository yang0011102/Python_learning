# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 10:07:40 2018

@author: yang
scale 尺度,滑动条
"""

import tkinter as tk

window=tk.Tk()
window.title('Scale')
window.geometry('200x200')

l=tk.Label(window,bg='white',
           width='20',
           text='滑动')
l.pack()

def print_sel(v):
    l.config(text='it is '+v)

s=tk.Scale(window,label='try',
           from_=0,to=10,
           orient=tk.HORIZONTAL,
           length=200,
           showvalue=0,
           tickinterval=2,
           resolution=0.01,
           command=print_sel)
s.pack()

window.mainloop()