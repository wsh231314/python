'''
Created on Sep 6, 2016

@author: shawn.shaohua.wang
'''
from tkinter import *
import tkinter.messagebox as messagebox

class HelloApp(Frame):
    def __init__(self, master=None):
        super(HelloApp, self).__init__()
        self.pack()
        self.addWidgets()
    
    def addWidgets(self):
        self.name = Entry(self)
        self.name.pack()
        self.okBtn = Button(self, text='Ok', command=self.pressOk)
        self.okBtn.pack()
    
    def pressOk(self):
        name = self.name.get()
        messagebox.showinfo('Hello', 'Hello ' + name)
    
appshow = HelloApp()
appshow.master.title('TTTTT')
appshow.mainloop()