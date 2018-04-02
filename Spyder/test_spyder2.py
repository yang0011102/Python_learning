# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 15:38:58 2018

@author: yang
"""

import tkinter as tk
window= tk.Tk()
window.title('None')
window.geometry('200x200')

e=tk.Entry(window,show='*')
e.pack()

def insert_point():
    var=e.get()
    tt.insert('insert',var)
def insert_end():
    var=e.get()
    tt.insert('end',var)

but1=tk.Button(window,text='insert point',
              command=insert_point)
but1.pack()

but2=tk.Button(window,text='insert end',
              command=insert_end)
but2.pack()

tt=tk.Text(window,height=2)
tt.pack()
window.mainloop()