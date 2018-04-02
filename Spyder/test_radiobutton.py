# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 18:55:57 2018

@author: yang
"""
import tkinter as tk
window=tk.Tk()
window.title('Radiobutton')
window.geometry('200x200')

var1=tk.StringVar()
l=tk.Label(window,bg='white',width=20,text='empty')
l.pack()


def print_selection():
    l.config(text='you have selected '+var1.get())
rb1=tk.Radiobutton(window,text='Option A',
                   variable=var1,
                   value='A',
                   command=print_selection)
rb1.pack()
rb2=tk.Radiobutton(window,text='Option B',
                   variable=var1,
                   value='B',
                   command=print_selection)
rb2.pack()
rb3=tk.Radiobutton(window,text='Option C',
                   variable=var1,
                   value='C',
                   command=print_selection)
rb3.pack()




window.mainloop()