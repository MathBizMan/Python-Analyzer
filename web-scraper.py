import tkinter as tk
from tkinter import*
import random
import time
#---------------------------------
root = tk.Tk()

root.geometry("1600x800+0+0")
root.title("resturant management system")

text_input = StringVar()
operator = ""

#-------frame------------------------------------------------
tops = Frame(root, width = 1600, height= 50, bg="blue", relief=SUNKEN)
tops.pack(side=TOP)

f1 = Frame(root, width = 800,height = 700,  relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width = 300, height = 700,  relief=SUNKEN)
f2.pack(side=RIGHT)

#---------------------time---------------------

lotime = time.asctime(time.localtime(time.time()))

#-------------font---label---------------------------

lblinfo = Label(tops, font=('arial', 50, 'bold'), text="Resturant management", fg="steel Blue", bd=10, anchor="w")
lblinfo.grid(row=0,column=0)
lblinfo = Label(tops, font=('arial', 20, 'bold'), text=lotime, fg="steel Blue", bd=10, anchor="w")
lblinfo.grid(row=1, column=0)
#----------------------calculator-------------------
def btnclick(number):
   global operator
   operator=operator + str(number)
   text_input.set(operator)

def btnclear():
   global operator
   operator=""
   text_input.set("")
def btnequal():
   global operator
   sump = str(eval(operator))
   operator=""
   text_input.set(sump)
   
def ref():
   x = random.randint(12908,54487)
   randomref = str(x)
   rand.set(randomref)
   

   cof = float(fries.get())
   cod = float(drink.get())
   cofilet = float(filet.get())
   cobur = float(burger.get())
   coch = float(chicken_burger.get())
   coche = float(cheese_burger.get())

   
   costoffries = cof * 0.99
   costofdr = cod * 1.00
   costofilet = cofilet * 2.99
   costbu = cobur * 2.87
   costofcoch = coch * 2.89
   costofche = coche * 2.89

   comeal = "$", str('%.2f' % (costoffries + costofdr + costofilet
                               + costbu + costofcoch + costofche ))
   paytax = ((costoffries + costofdr + costofilet + costbu
                               + costofcoch + costofche ) * 0.2)
   totalcost = (costoffries + costofdr + costofilet + costbu
                               + costofcoch + costofche )
   ser_cost = ((costoffries + costofdr + costofilet + costbu
                               + costofcoch + costofche )/99)
