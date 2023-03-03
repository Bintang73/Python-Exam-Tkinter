import tkinter as tk
from tkinter import *
from tkinter import messagebox

class ExampleApp():
    def __init__(self):
        self.window = Tk()
        self.window.resizable(1280,720)
        self.window.maxsize(1280, 720)
        self.window.minsize(1280, 720)
        self.label1 = Label(self.window, text="", width=10)
        self.label1.place(x=66,y=172)
        self.label1.pack()
        self.label2 = Label(self.window, text="", width=10)
        self.label2.place(x=80,y=200)
        self.label2.pack()
        self.label3 = Label(self.window, text="", width=10)
        self.label3.place(x=90,y=250)
        self.label3.pack()
        self.remaining = 0
        # self.upcomingtest = Button(self.window, bg = "#FFFFFF", activebackground="#DDDDDD", borderwidth=0, height=20, width=170)
        # self.upcomingtest.place(x=66,y=172)
        self.temp = int(00)*3600 + int(00)*60 + int(10)
        self.countdown(self.temp)
        self.window.mainloop()

    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.window.destroy()
            messagebox.showinfo("Selesai!", "Soal sudah selesai!")
            #self.label.configure(text="time's up!")
        else:
            mins,secs = divmod(self.remaining,60)
            #mins = divmod(mins, 60)
        
            # using format () method to store the value up to
            # two decimal places
            
            #self.label1.configure(text="{0:2d}".format(hours))
            self.label2.configure(text="{0:2d}".format(mins))
            self.label3.configure(text="{0:2d}".format(secs))
            
            self.remaining = self.remaining - 1
            self.window.after(1000, self.countdown)

if __name__ == "__main__":
    ExampleApp()