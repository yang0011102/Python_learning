# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 11:53:54 2018

@author: yang
"""
import tkinter as tk
window=tk.Tk()
window.title('frame')
window.geometry('200x200')
tk.Label(window,text='test').pack()

frm=tk.Frame(window)
frm.pack()
frml=tk.Frame(frm)
frml.pack(side='left')
frmr=tk.Frame(frm)
frmr.pack(side='right')

tk.Label(frml,text='left1').pack()
tk.Label(frml,text='left2').pack()
tk.Label(frmr,text='right1').pack()
window.mainloop()
