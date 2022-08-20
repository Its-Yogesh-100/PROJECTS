from cgitb import grey
from glob import glob
from locale import currency
import math
from tkinter import *
from turtle import color


y=Tk()
y.title("calculator")

e=Entry(y,width=30,borderwidth=3)
e.grid(row=0,column=0,columnspan=10,padx=90,pady=5)

def button_click(number):
     #e.delete(0,END)
     current=e.get()
     e.delete(0,END)
     e.insert(0,str(current)+str(number))


def button_clear():
      e.delete(0,END)


def button_add():
     first_num=e.get()
     global f_num 
     global math
     math="addition"
     f_num=int(first_num)
     e.delete(0,END)


def button_sub():
     first_num=e.get()
     global f_num 
     global math
     math="Substraction"
     f_num=int(first_num)
     e.delete(0,END)

def button_mult():
     first_num=e.get()
     global f_num 
     global math
     math="Multiplication"
     f_num=int(first_num)
     e.delete(0,END)

def button_div():
     first_num=e.get()
     global f_num 
     global math
     math="Division"
     f_num=int(first_num)
     e.delete(0,END)

def button_equal():
      second_num=e.get()
      e.delete(0,END)

      if math=="addition":
          e.insert(0,f_num+int(second_num))

      if math=="Substraction":
          e.insert(0,f_num-int(second_num))

      if math=="Multiplication":
          e.insert(0,f_num*int(second_num))

      if math=="Division":
          e.insert(0,f_num/int(second_num))

# defines button


b1=Button(y,text="1",padx=40,pady=20, command=lambda: button_click(1))
b2=Button(y,text="2",padx=40,pady=20,command=lambda: button_click(2))
b3=Button(y,text="3",padx=40,pady=20,command=lambda: button_click(3))
b4=Button(y,text="4",padx=40,pady=20,command=lambda: button_click(4))
b5=Button(y,text="5",padx=40,pady=20,command=lambda: button_click(5))
b6=Button(y,text="6",padx=40,pady=20,command=lambda: button_click(6))
b7=Button(y,text="7",padx=40,pady=20,command=lambda: button_click(7))
b8=Button(y,text="8",padx=40,pady=20,command=lambda: button_click(8))
b9=Button(y,text="9",padx=40,pady=20,command=lambda: button_click(9))
b0=Button(y,text="0",padx=40,pady=20,command=lambda: button_click(0))

b_add=Button(y,text="+",padx=40,pady=20,command=lambda: button_add)
b_equal=Button(y,text="=",padx=40,pady=20,command=button_equal)
b_clear=Button(y,text="Clear",padx=30,pady=20,borderwidth=1,  command=lambda: button_clear())

b_SUB=Button(y,text="-",padx=40,pady=20,command=button_mult)
b_mul=Button(y,text="*",padx=40,pady=20,command=button_mult)
b_div=Button(y,text="/",padx=40,pady=20,command=button_div)


#put button on screen
b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
b3.grid(row=1,column=2)

b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)

b7.grid(row=3,column=0)
b8.grid(row=3,column=1)
b9.grid(row=3,column=2)

b0.grid(row=4,column=0)

b_add.grid(row=1,column=4)
b_equal.grid(row=4,column=2)
b_clear.grid(row=4,column=1)
b_SUB.grid(row=2,column=4)
b_mul.grid(row=3,column=4)
b_div.grid(row=4,column=4)


y.mainloop()
