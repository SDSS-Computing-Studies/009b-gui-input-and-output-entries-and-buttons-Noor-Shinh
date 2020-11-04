"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""
import tkinter as tk 
from tkinter import *
import math 
win=tk.Tk()
win.title("Factoring Simple Trinomials")
eoutput=StringVar()
variable1=StringVar()
variable2=StringVar()

def factor():
    a=1
    b=a1.get()
    c=a2.get()
    b=int(b)
    c=int(c)
    d=variable1.get()
    e=variable2.get()
    if d=="+":
        b=b*1
    elif x1=="-":
        b=b*-1
    if e=="+":
        c=c*1
    elif x2=="-":
        c=c*-1
    stepx1=(b*-1)
    stepx2=math.pow(b,2)-(4*a*c)
    stepx2=math.sqrt(stepx2)
    stepx3=(stepx1)+(stepx2) 
    stepx4=(stepx3)/(2*a)
    stepy1=(b*-1)
    stepy2=math.pow(b,2)-(4*a*c)
    stepy2=math.sqrt(stepy2)
    stepy3=(stepy1)-(stepy2) 
    stepy4=(stepy3)/(2*a)
    stepx4=round(stepx4,2)
    stepy4=round(stepy4,2)
    if stepx4>0:
        stepx5=("x"+str(stepx4*-1))
    elif stepx4<0:
        stepx5=("x+"+str(stepx4*-1))
    if stepy4>0:
        stepy5=("x"+str(stepy4*-1))
    elif stepy4<0:
        stepy5=("x+"+str(stepy4*-1))
    numlist=[stepy5,stepx5]
    eoutput.set(numlist)

l1=Label(win,text="bx value")
l2=Label(win,text="c value")
l3=Label(win,text="ax value is always equal to 1")
a1=Entry(win,width=40)
a2=Entry(win,width=40)
x1=OptionMenu(win,variable1,"+","-")
x2=OptionMenu(win,variable2,"+","-")
b1=Button(win,text="Factor",command=factor)
f1=Label(win,textvariable=eoutput)

l1.grid(row=1,column=1,sticky=E)
a1.grid(row=1,column=2,sticky=W)
l2.grid(row=2,column=1,sticky=E)
a2.grid(row=2,column=2,sticky=W)
x1.grid(row=1,column=3,)
x2.grid(row=2,column=3,)
b1.grid(row=3,column=1)
f1.grid(row=4,column=1)
win.mainloop()
