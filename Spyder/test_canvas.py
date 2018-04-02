# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 10:40:17 2018

@author: yang
"""
import tkinter as tk
window=tk.Tk()
window.title('canvas')
window.geometry('200x200')

canv=tk.Canvas(window,bg='white',
               height=100,width=200)
x0,y0,x1,y1=50,50,80,80
oval=canv.create_oval(x0,y0,x1,y1)
line=canv.create_line(x0,y0,x1,y1)
arc=canv.create_arc(x0+30,y0,x1+30,y1,
                    start=30,extent=120)
canv.pack()

def mov():
    canv.move(arc,0,10)
but=tk.Button(window,text='click',
              command=mov).pack()
window.mainloop()

