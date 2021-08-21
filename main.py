from tkinter import*
import random
import time
import csv
import pandas as pd
from datetime import datetime

totalPemasukan = 0
namaFile = datetime.today().strftime('%Y-%m-%d')

########## FUNGSI TOTAL ##########
def totalFunction():
    global totalPemasukan

    x = random.randint(12980, 50876)
    randomRef = str(x)
    idOrder.set(randomRef)

    food_1 = float(Makanan1.get())
    food_2 = float(Makanan2.get())
    food_3 = float(Makanan3.get())
    food_4 = float(Makanan4.get())
    food_5 = float(Makanan5.get())
    drink= float(Minuman.get())
    intUang= int(Uang.get())

    totalFood1 = food_1 * 15000
    totalFood2 = food_2 * 20000
    totalFood3 = food_3 * 25000
    totalFood4 = food_4 * 25000
    totalFood5 = food_5 * 30000
    totalDrinks = drink * 15000

    hargaBersih = round(totalFood1 + totalFood2 + totalFood3 + totalFood4 + totalFood5 + totalDrinks)
    hargaBersihRp = "Rp.", str('%.2f'% hargaBersih)

    hargaServis = round((totalFood1 + totalFood2 + totalFood3 + totalFood4 + totalFood5 + totalDrinks)/99)
    hargaServisRp = "Rp.", str('%.2f'% hargaServis)

    hargaPajak = round((totalFood1 + totalFood2 + totalFood3 + totalFood4 + totalFood5 + totalDrinks) * 0.2)
    hargaPajakRp= "Rp.", str('%.2f'% hargaPajak)

    hargaTotal = round(hargaPajak + hargaBersih + hargaServis)
    hargaTotalRp = "Rp.", str(('%.2f'% hargaTotal))

    hargaKembalian = round(intUang - hargaTotal)

    totalPemasukan += (hargaTotal)

    if hargaKembalian < 0:
        totalPemasukan -= (hargaTotal)
        hargaKembalianRp = "Uang Tidak Cukup"

    else:
        hargaKembalianRp = "Rp.", str('%.2f'% hargaKembalian)

        totalPemasukanRp = "Rp"+str(totalPemasukan) 

        dataPenjualan = [localtime, randomRef, str('%.0f'% food_1), str('%.0f'% food_2), str('%.0f'% food_3), str('%.0f'% food_4), str('%.0f'% food_5), \
                        str('%.0f'% drink), 'Rp' + str(hargaBersih), 'Rp' + str(hargaServis), 'Rp' + str(hargaPajak), 'Rp' + str(hargaTotal), \
                        'Rp' + str(intUang), 'Rp' + str(hargaKembalian), 'Rp' + str(totalPemasukan)]

        fileName = 'Data Penjualan'+'-'+namaFile+'.csv'

        with open(fileName, 'a') as f:
            w=csv.writer(f, quoting=csv.QUOTE_ALL)
            w.writerow(dataPenjualan)

        file = open(fileName)
        reader = csv.reader(file)
        lines= len(list(reader)) - 1

        df = pd.read_csv(fileName)
        df.to_csv(fileName, header=["Waktu Pemesanan","Id Order","Makanan 1","Makanan 2","Makanan 3","Makanan 4","Makanan 5","Minuman",\
                                    "Harga Bersih","Harga Servis","Harga Pajak","Harga Total","Uang","Kembalian","Pemasukan"], index=False)

        Pelanggan.set(lines)
        Income.set(totalPemasukanRp)
    
    Subtotal.set(hargaBersihRp)
    Service_Charge.set(hargaServisRp)
    Tax.set(hargaPajakRp)
    Total.set(hargaTotalRp)
    Uang.set(intUang)
    Kembalian.set(hargaKembalianRp)
    
########## FUNGSI EXIT ##########
def exitFunction():
    root.destroy()

########## FUNGSI RESET ##########
def resetFunction():
    localtime=time.asctime(time.localtime(time.time()))
    labelWaktu = Label(judulCont, font=( 'aria' , 20, ), text=localtime, fg="steel blue", anchor=W)
    labelWaktu.grid(row=3, column=0)
    idOrder.set(int(0))
    Makanan1.set(int(0))
    Makanan2.set(int(0))
    Makanan3.set(int(0))
    Makanan4.set(int(0))
    Makanan5.set(int(0))
    Subtotal.set(int(0))
    Minuman.set(int(0))
    Total.set(int(0))
    Service_Charge.set(int(0))
    Tax.set(int(0))
    Uang.set(int(0))
    Kembalian.set(int(0))

########## FUNGSI LIST MENU ##########
def list_menu():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="_____________", fg="white", anchor=W)
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

#######################################################################################################################
#######################################################################################################################

root = Tk()
root.geometry("1080x850+0+0")
root.title("Restaurant Management System")

judulCont = Frame(root, width = 1600, height=50, relief=SUNKEN)
judulCont.pack(side=TOP)

inputCont = Frame(root, width = 900, height=700, relief=SUNKEN)
inputCont.pack(side=TOP)

infoCont = Frame(root, width = 900, height=500, relief=SUNKEN)
infoCont.pack(side=TOP)

buttonCont = Frame(root, width = 900, height=500, relief=SUNKEN)
buttonCont.pack(side=TOP)

########## FETCH TIME ##########
localtime=time.asctime(time.localtime(time.time()))

########## TAMPILAN JUDUL ##########
lblgaris1= Label(judulCont, text=" ", fg="steel blue")
lblgaris1.grid(row=0, columnspan=15)

lblgaris2 = Label(judulCont, text=" ", fg="steel blue")
lblgaris2.grid(row=1, columnspan=15)

labelResto = Label(judulCont, font=( 'aria' , 30, 'bold' ), text="Restaurant Management System", fg="steel blue", bd=10, anchor='w')
labelResto.grid(row=2, column=0)
labelWaktu = Label(judulCont, font=( 'aria' , 20, ), text=localtime, fg="steel blue", anchor=W)
labelWaktu.grid(row=3, column=0)


text_Input=StringVar()
operator =""

########## INISIASI ##########
idOrder = StringVar()
Makanan1 = StringVar()
Makanan2 = StringVar()
Makanan3 = StringVar()
Makanan4 = StringVar()
Makanan5 = StringVar()
Minuman = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Tax = StringVar()
Uang = StringVar()
Kembalian = StringVar()
Income = StringVar()
Pelanggan = StringVar()

########## TAMPILAN INPUT ##########
lblgaris1= Label(inputCont, text=" ", fg="steel blue")
lblgaris1.grid(row=0, columnspan=15)

lblgaris2 = Label(inputCont, text=" ", fg="steel blue")
lblgaris2.grid(row=1, columnspan=15)

labelOrder = Label(inputCont, font=( 'aria' , 16, 'bold' ), text="Id Order", fg="steel blue", bd=10, anchor='w')
labelOrder.grid(row=2, column=0)
inputOrder = Entry(inputCont, font=('ariel' , 16, 'bold'), textvariable=idOrder , bd=6, insertwidth=4, bg="powder blue" , justify='right')
inputOrder.grid(row=2, column=1)

labelMakanan1 = Label(inputCont, font=( 'aria' , 16, 'bold' ), text="Fries Meal", fg="steel blue", bd=10, anchor='w')
labelMakanan1.grid(row=3, column=0)
inputMakanan1 = Entry(inputCont, font=('ariel' , 16, 'bold'), textvariable=Makanan1 , bd=6, insertwidth=4, bg="powder blue" , justify='right')
inputMakanan1.grid(row=3, column=1)

labelMakanan2 = Label(inputCont, font=( 'aria' , 16, 'bold' ), text="Lunch Meal", fg="steel blue", bd=10, anchor='w')
labelMakanan2.grid(row=4, column=0)
inputMakanan2 = Entry(inputCont, font=('ariel' , 16, 'bold'), textvariable=Makanan2 , bd=6, insertwidth=4, bg="powder blue" , justify='right')
inputMakanan2.grid(row=4, column=1)

labelMakanan3 = Label(inputCont, font=( 'aria' , 16, 'bold' ), text="Burger Meal", fg="steel blue", bd=10, anchor='w')
labelMakanan3.grid(row=5, column=0)
inputMakanan3 = Entry(inputCont, font=('ariel' , 16, 'bold'), textvariable=Makanan3 , bd=6, insertwidth=4, bg="powder blue" , justify='right')
inputMakanan3.grid(row=5, column=1)

labelMakanan4 = Label(inputCont, font=( 'aria' , 16, 'bold' ), text="Pizza Meal", fg="steel blue", bd=10, anchor='w')
labelMakanan4.grid(row=6, column=0)
inputMakanan4= Entry(inputCont, font=('ariel' , 16, 'bold'), textvariable=Makanan4 , bd=6, insertwidth=4, bg="powder blue" , justify='right')
inputMakanan4.grid(row=6, column=1)

labelMakanan5 = Label(inputCont, font=( 'aria' , 16, 'bold' ), text="Cheese burger", fg="steel blue", bd=10, anchor='w')
labelMakanan5.grid(row=7, column=0)
inputMakanan5 = Entry(inputCont, font=('ariel' , 16, 'bold'), textvariable=Makanan5, bd=6, insertwidth=4, bg="powder blue" , justify='right')
inputMakanan5.grid(row=7, column=1)

labelMinuman = Label(inputCont, font=( 'aria' , 16, 'bold' ), text="Drinks", fg="steel blue", bd=10, anchor='w')
labelMinuman.grid(row=8, column=0)
inputMinuman = Entry(inputCont, font=('ariel' , 16, 'bold'), textvariable=Minuman , bd=6, insertwidth=4, bg="powder blue" , justify='right')
inputMinuman.grid(row=8, column=1)

#--------------------------------------------------------------------------------------

labelSubTotal = Label(inputCont, font=( 'aria' , 16, 'bold' ), text="Sub Total", fg="steel blue", bd=10, anchor='w')
labelSubTotal.grid(row=2, column=2)
boxSubTotal = Entry(inputCont, font=('ariel' , 16, 'bold'), textvariable=Subtotal , bd=6, insertwidth=4, bg="powder blue" , justify='right')
boxSubTotal.grid(row=2, column=3)

labelService = Label(inputCont, font=( 'aria' , 16, 'bold' ), text="Service Charge", fg="steel blue", bd=10, anchor='w')
labelService.grid(row=3, column=2)
boxService = Entry(inputCont, font=('ariel' , 16, 'bold'), textvariable=Service_Charge , bd=6, insertwidth=4, bg="powder blue" , justify='right')
boxService.grid(row=3, column=3)

labelTax = Label(inputCont, font=( 'aria' , 16, 'bold' ), text="Tax", fg="steel blue", bd=10, anchor='w')
labelTax.grid(row=4, column=2)
boxTax = Entry(inputCont, font=('ariel' , 16, 'bold'), textvariable=Tax , bd=6, insertwidth=4, bg="powder blue" , justify='right')
boxTax.grid(row=4, column=3)

labelTotal = Label(inputCont, font=( 'aria' , 16, 'bold' ), text="Total", fg="steel blue", bd=10, anchor='w')
labelTotal.grid(row=5, column=2)
boxTotal = Entry(inputCont, font=('ariel' , 16, 'bold'), textvariable=Total , bd=6, insertwidth=4, bg="powder blue" , justify='right')
boxTotal.grid(row=5, column=3)

labelUang = Label(inputCont, font=( 'aria' , 16, 'bold' ), text="Uang", fg="steel blue", bd=10, anchor='w')
labelUang.grid(row=7, column=2)
inputUang = Entry(inputCont, font=('ariel' , 16, 'bold'), textvariable=Uang , bd=6, insertwidth=4, bg="powder blue" , justify='right')
inputUang.grid(row=7, column=3)

labelKembalian = Label(inputCont, font=( 'aria' , 16, 'bold' ), text="Kembalian", fg="steel blue", bd=10, anchor='w')
labelKembalian.grid(row=8, column=2)
boxKembalian = Entry(inputCont, font=('ariel' , 16, 'bold'), textvariable=Kembalian , bd=6, insertwidth=4, bg="powder blue" , justify='right')
boxKembalian.grid(row=8, column=3)


########## TAMPILAN INFO KESELURUHAN ##########
lblgaris1= Label(infoCont, text=" ", fg="steel blue")
lblgaris1.grid(row=0, columnspan=15)

lblgaris2 = Label(infoCont, text=" ", fg="steel blue")
lblgaris2.grid(row=1, columnspan=15)

lblpelanggan = Label(infoCont, font=( 'aria' , 16, 'bold' ), text="Total Coustomer", fg="steel blue", justify=RIGHT)
lblpelanggan.grid(row=2, column=0)
lblpelanggan = Label(infoCont, font=( 'aria' , 16, 'bold' ), textvariable=Pelanggan, fg="steel blue", justify=RIGHT)
lblpelanggan.grid(row=3, column=0)

lblpelanggan = Label(infoCont, font=( 'aria' , 16, 'bold' ), text="Income", fg="steel blue", justify=RIGHT)
lblpelanggan.grid(row=4, column=0)
lblpelanggan = Label(infoCont, font=( 'aria' , 16, 'bold' ), textvariable=Income, fg="steel blue", justify=RIGHT)
lblpelanggan.grid(row=5, column=0)

########## TOMBOL MENU ##########
lblgaris1= Label(buttonCont, text=" ", fg="steel blue")
lblgaris1.grid(row=0, columnspan=15)

lblgaris2 = Label(buttonCont, text=" ", fg="steel blue")
lblgaris2.grid(row=1, columnspan=15)

buttonMenu = Button(buttonCont, padx=16, pady=8, bd=10 , fg="black", font=('ariel' , 16, 'bold'), width=10, text="MENU", bg="powder blue", command=list_menu)
buttonMenu.grid(row=2, column=0)

buttonTotal = Button(buttonCont, padx=16, pady=8, bd=10 , fg="black", font=('ariel' , 16, 'bold'), width=10, text="TOTAL", bg="powder blue", command=totalFunction)
buttonTotal.grid(row=2, column=1)

buttonPrint = Button(buttonCont, padx=16, pady=8, bd=10 , fg="black", font=('ariel' , 16, 'bold'), width=10, text="PRINT", bg="powder blue", command=exitFunction)
buttonPrint.grid(row=2, column=2)

buttonReset = Button(buttonCont, padx=16, pady=8, bd=10 , fg="black", font=('ariel' , 16, 'bold'), width=10, text="RESET", bg="powder blue", command=resetFunction)
buttonReset.grid(row=2, column=3)

buttonExit = Button(buttonCont, padx=16, pady=8, bd=10 , fg="black", font=('ariel' , 16, 'bold'), width=10, text="EXIT", bg="powder blue", command=exitFunction)
buttonExit.grid(row=2, column=4)

root.mainloop()
