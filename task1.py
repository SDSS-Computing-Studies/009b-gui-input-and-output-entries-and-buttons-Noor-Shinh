"""
##### Task 1
Create a "Madlib" that has the users enter in a variety of noun/verb/adjectives.
When they press a button, it should update the contents of a label to display
the completed madlib.
What is a madlib? Visit https://www.madlibs.com/printables/ to see some Madlibs
you might use in your assignment
"""
import tkinter as tk 
from tkinter import *
win=tk.Tk()
eoutput=StringVar()


def madlib():
    Holiday=a1.get()
    Noun=a2.get()
    Place=a3.get()
    Person=a4.get()
    Adjective=a5.get()
    Body=a6.get()
    Verb=a7.get()
    Adjective2=a8.get()
    Adjective3=a9.get()
    Food=a10.get()
    Plural=a11.get()
    
    story ="I cant believe its already"+ Holiday + "!I can't wait to put on my"+Noun+"and visit every"+Place+"in my neighbourhood.This year I am going to dress up as"+ Person+" with" + Adjective2+Body+". Before I "+ Verb+"I make sure to grab my"+Adjective3+Noun+"to hold all of my"+Food+"Finally all of my"+Plural+"are ready to go"
    eoutput.set(story)
    f1entry.delete(0,END)
    f1entry.insert(0,story)

a1=Entry(win,text="Enter a Holiday",width=40)
a2=Entry(win,text="Enter a Noun",width=40)
a3=Entry(win,text="Enter an Place",width=40)
a4=Entry(win,text="Enter a Person",width=40) 
a5=Entry(win,text="Enter a Adjective",width=40)
a6=Entry(win,text="Enter a Body Part",width=40)
a7=Entry(win,text="Enter a Verb",width=40)
a8=Entry(win,text="Enter another Adjective",width=40)
a9=Entry(win,text="Enter another Adjective",width=40)
a10=Entry(win,text="Enter a type of Food",width=40)
a11=Entry(win,text="Enter a Plural Noun",width=40)
b1=Button(win,text="Finalise Madlib",command=madlib)
f1=Entry(win,textvariable=eoutput,width=40)

a1.pack()
a2.pack()
a3.pack()
a4.pack()
a5.pack()
a6.pack()
a7.pack()
a8.pack()
a9.pack()
a10.pack()
a11.pack()
b1.pack()
f1.pack()
win.mainloop()