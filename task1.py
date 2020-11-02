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



def madlib():
    Holiday=a1.get
    Noun=a2.get
    Place=a3.get
    Person=a4.get
    Adjective=a5.get
    Body=a6.get
    Verb=a7.get
    Adjective2=a8.get
    Adjective3=a9.get
    Food=a10.get
    Plural=a11.get
    
output1=("Enter a Holiday")
output2=("Enter a Noun")
output3=("Enter an Place")
output4=("Enter a Person") 
output5=("Enter a Adjective")
output6=("Enter a Body Part")
output7=("Enter a Verb")
output8=("Enter another Adjective")
output9=("Enter another Adjective")
output10=("Enter a type ofFood")
output11=("Enter a Plural Noun")
output1= StringVar()
output2= StringVar()
output3= StringVar()
output4= StringVar()
output5= StringVar()
output6= StringVar()
output7= StringVar()
output8= StringVar()
output9= StringVar()
output10= StringVar()
output11= StringVar()


l1=Label(win,text="I can't believe its already")
a1=Entry(win,text="Enter a Holiday")
b1=Button(win,command=madlib)

l1.pack()
a1.pack()
b1.pack()
win.mainloop()
