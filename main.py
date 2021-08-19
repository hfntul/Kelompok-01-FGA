from tkinter import*
import random
import time
import csv

root = Tk()
root.geometry("1080x810+0+0")
root.title("Restaurant Management System")

Tops = Frame(root,width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
f1.pack(side=TOP)

f2 = Frame(root,width = 900,height=500,relief=SUNKEN)
f2.pack(side=TOP)

f3 = Frame(root,width = 900,height=500,relief=SUNKEN)
f3.pack(side=TOP)

#------------------TIME--------------
localtime=time.asctime(time.localtime(time.time()))

#-----------------JUDUL------------
lblgaris1= Label(Tops,text=" ",fg="steel blue")
lblgaris1.grid(row=0,columnspan=15)

lblgaris2 = Label(Tops,text=" ",fg="steel blue")
lblgaris2.grid(row=1,columnspan=15)

lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="Restaurant Management System",fg="steel blue",bd=10,anchor='w')
lblinfo.grid(row=2,column=0)
lblinfo = Label(Tops, font=( 'aria' ,20, ),text=localtime,fg="steel blue",anchor=W)
lblinfo.grid(row=3,column=0)

#-----------------JUDUL------------

text_Input=StringVar()
operator =""

#-----------------TOTAL------------
def Ref():
    x=random.randint(12980, 50876)
    randomRef = str(x)
    rand.set(randomRef)

    cof =float(Fries.get())
    colfries= float(Largefries.get())
    cob= float(Burger.get())
    cofi= float(Filet.get())
    cochee= float(Cheese_burger.get())
    codr= float(Drinks.get())
    cuang= int(Uang.get())

    costoffries = cof*15000
    costoflargefries = colfries*20000
    costofburger = cob*25000
    costoffilet = cofi*25000
    costofcheeseburger = cochee*30000
    costofdrinks = codr*15000

    costofmeal = "Rp.",str('%.2f'% (costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks))
    PayTax=((costoffries +  costoflargefries + costofburger + costoffilet +  costofcheeseburger + costofdrinks)*0.2)
    Totalcost=(costoffries +  costoflargefries + costofburger + costoffilet  + costofcheeseburger + costofdrinks)
    Ser_Charge=((costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks)/99)
    semua = (PayTax + Totalcost + Ser_Charge)
    Service="Rp.",str('%.2f'% Ser_Charge)
    OverAllCost="Rp.",str('%.2f'%(PayTax + Totalcost + Ser_Charge))
    PaidTax="Rp.",str('%.2f'% PayTax)
    TotKemb = (cuang - semua)
    Kembal = "Rp.",str('%.2f'% TotKemb)

    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Subtotal.set(costofmeal)
    Total.set(OverAllCost)
    Uang.set(cuang)
    Kembalian.set(Kembal)

#---------------------------------

#-----------------EXIT------------

def qexit():
    root.destroy()

#---------------------------------

#----------------RESET------------

def reset():
    localtime=time.asctime(time.localtime(time.time()))
    rand.set(int(0))
    Fries.set(int(0))
    Largefries.set(int(0))
    Burger.set(int(0))
    Filet.set(int(0))
    Subtotal.set(int(0))
    Total.set(int(0))
    Service_Charge.set(int(0))
    Drinks.set(int(0))
    Tax.set(int(0))
    cost.set(int(0))
    Cheese_burger.set(int(0))
    Uang.set(int(0))
    Kembalian.set(int(0))
    lblinfo = Label(Tops, font=( 'aria' ,20, ),text=localtime,fg="steel blue",anchor=W)
    lblinfo.grid(row=3,column=0)

#---------------------------------

#----------------INISIASI------------

rand = StringVar()
Fries = StringVar()
Largefries = StringVar()
Burger = StringVar()
Filet = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
cost = StringVar()
Cheese_burger = StringVar()
Uang = StringVar()
Kembalian = StringVar()

#---------------------------------

#-------------TAMPILAN INPUT--------------------
lblgaris1= Label(f1,text=" ",fg="steel blue")
lblgaris1.grid(row=0,columnspan=15)

lblgaris2 = Label(f1,text=" ",fg="steel blue")
lblgaris2.grid(row=1,columnspan=15)

lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Order No.",fg="steel blue",bd=10,anchor='w')
lblreference.grid(row=2,column=0)
txtreference = Entry(f1,font=('ariel' ,16,'bold'), textvariable=rand , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtreference.grid(row=2,column=1)

lblfries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Fries Meal",fg="steel blue",bd=10,anchor='w')
lblfries.grid(row=3,column=0)
txtfries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Fries , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtfries.grid(row=3,column=1)

lblLargefries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Lunch Meal",fg="steel blue",bd=10,anchor='w')
lblLargefries.grid(row=4,column=0)
txtLargefries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Largefries , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtLargefries.grid(row=4,column=1)

lblburger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Burger Meal",fg="steel blue",bd=10,anchor='w')
lblburger.grid(row=5,column=0)
txtburger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Burger , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtburger.grid(row=5,column=1)

lblFilet = Label(f1, font=( 'aria' ,16, 'bold' ),text="Pizza Meal",fg="steel blue",bd=10,anchor='w')
lblFilet.grid(row=6,column=0)
txtFilet = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Filet , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtFilet.grid(row=6,column=1)

lblCheese_burger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cheese burger",fg="steel blue",bd=10,anchor='w')
lblCheese_burger.grid(row=7,column=0)
txtCheese_burger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Cheese_burger , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtCheese_burger.grid(row=7,column=1)

lblDrinks = Label(f1, font=( 'aria' ,16, 'bold' ),text="Drinks",fg="steel blue",bd=10,anchor='w')
lblDrinks.grid(row=8,column=0)
txtDrinks = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Drinks , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtDrinks.grid(row=8,column=1)

#--------------------------------------------------------------------------------------

lblcost = Label(f1, font=( 'aria' ,16, 'bold' ),text="Sub Total",fg="steel blue",bd=10,anchor='w')
lblcost.grid(row=2,column=2)
txtcost = Entry(f1,font=('ariel' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtcost.grid(row=2,column=3)

lblService_Charge = Label(f1, font=( 'aria' ,16, 'bold' ),text="Service Charge",fg="steel blue",bd=10,anchor='w')
lblService_Charge.grid(row=3,column=2)
txtService_Charge = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtService_Charge.grid(row=3,column=3)

lblTax = Label(f1, font=( 'aria' ,16, 'bold' ),text="Tax",fg="steel blue",bd=10,anchor='w')
lblTax.grid(row=4,column=2)
txtTax = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtTax.grid(row=4,column=3)

lblTotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Total",fg="steel blue",bd=10,anchor='w')
lblTotal.grid(row=5,column=2)
txtTotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtTotal.grid(row=5,column=3)

lblUang = Label(f1, font=( 'aria' ,16, 'bold' ),text="Uang",fg="steel blue",bd=10,anchor='w')
lblUang.grid(row=7,column=2)
txtUang = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Uang , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtUang.grid(row=7,column=3)

lblKembl = Label(f1, font=( 'aria' ,16, 'bold' ),text="Kembalian",fg="steel blue",bd=10,anchor='w')
lblKembl.grid(row=8,column=2)
txtKembl = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Kembalian , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtKembl.grid(row=8,column=3)

#---------------------------------

#-----------------------------------------INFO------------------------------------------
lblgaris1= Label(f2,text=" ",fg="steel blue")
lblgaris1.grid(row=0,columnspan=15)

lblgaris2 = Label(f2,text=" ",fg="steel blue")
lblgaris2.grid(row=1,columnspan=15)

lblpelanggan = Label(f2, font=( 'aria' ,16, 'bold' ),text="Total of Coustomer",fg="steel blue", justify=RIGHT)
lblpelanggan.grid(row=2,column=0)

lblpelanggan = Label(f2, font=( 'aria' ,16, 'bold' ),text="Income",fg="steel blue", justify=RIGHT)
lblpelanggan.grid(row=3,column=0)

#---------------------------------

#-----------------------------------------TOMBOL BAWAH------------------------------------------
lblgaris1= Label(f3,text=" ",fg="steel blue")
lblgaris1.grid(row=0,columnspan=15)

lblgaris2 = Label(f3,text=" ",fg="steel blue")
lblgaris2.grid(row=1,columnspan=15)

btnTotal=Button(f3,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="powder blue",command=Ref)
btnTotal.grid(row=2, column=1)

btnprint=Button(f3,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PRINT", bg="powder blue",command=qexit)
btnprint.grid(row=2, column=2)

btnreset=Button(f3,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="powder blue",command=reset)
btnreset.grid(row=2, column=3)

btnexit=Button(f3,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="powder blue",command=qexit)
btnexit.grid(row=2, column=4)

#---------------------------------

#-----------------ISI MENU ----------------
def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Fries Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="15000", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Lunch Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="20000", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Burger Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25000", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pizza Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25000", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cheese Burger", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="30000", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Drinks", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="15000", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=3)

    roo.mainloop()

#--------------BUTTON MENU -------------------

btnprice=Button(f3,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="MENU", bg="powder blue",command=price)
btnprice.grid(row=2, column=0)

root.mainloop()
