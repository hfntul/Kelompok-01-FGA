from tkinter import*
import random
import time
import csv
import pandas as pd
from datetime import datetime
from PIL import Image,ImageTk

totalPemasukan = 0
namaFile = datetime.today().strftime('%Y-%m-%d-p')

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
    totalFood2 = food_2 * 15000
    totalFood3 = food_3 * 12000
    totalFood4 = food_4 * 10000
    totalFood5 = food_5 * 18000
    totalDrinks = drink * 5000

    hargaBersih = round(totalFood1 + totalFood2 + totalFood3 + totalFood4 + totalFood5 + totalDrinks)
    hargaBersihRp = "Rp.", str('%.2f'% hargaBersih)

    hargaServis = round((totalFood1 + totalFood2 + totalFood3 + totalFood4 + totalFood5 + totalDrinks)*0.01)
    hargaServisRp = "Rp.", str('%.2f'% hargaServis)

    hargaPajak = round((totalFood1 + totalFood2 + totalFood3 + totalFood4 + totalFood5 + totalDrinks)*0.02)
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
    labelWaktu = Label(judulCont, font=( 'Consolas' , 20, ), text=localtime, fg="steel blue", anchor=W,bg="#F6F6F6")
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
    menu = Tk()
    menu.geometry("420x220+0+0")
    menu.title("Harga")
    lblinfo = Label(menu, font=('Consolas', 15, 'bold'), text="MENU", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(menu, font=('Consolas', 15, 'bold'), text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(menu, font=('Consolas', 15, 'bold'), text="HARGA", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(menu, font=('Consolas', 15, 'bold'), text="Nasi Goreng", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(menu, font=('Consolas', 15, 'bold'), text="Rp15000", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(menu, font=('Consolas', 15, 'bold'), text="Nasi Uduk", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(menu, font=('Consolas', 15, 'bold'), text="Rp15000", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(menu, font=('Consolas', 15, 'bold'), text="Lontong Sayur", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(menu, font=('Consolas', 15, 'bold'), text="Rp12000", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(menu, font=('Consolas', 15, 'bold'), text="Bubur Ayam", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(menu, font=('Consolas', 15, 'bold'), text="Rp10000", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(menu, font=('Consolas', 15, 'bold'), text="Soto Betawi", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(menu, font=('Consolas', 15, 'bold'), text="Rp18000", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(menu, font=('Consolas', 15, 'bold'), text="Teh Manis", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(menu, font=('Consolas', 15, 'bold'), text="Rp5000", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=3)

    menu.mainloop()

########## FUNGSI INPUT GAMBAR ##########
def inputGambar(path, baris):
    image= (Image.open(path))
    resized_image= image.resize((55,55), Image.ANTIALIAS)
    img= ImageTk.PhotoImage(resized_image)
    label1 = Label(inputCont, bg="#F6F6F6", image=img)
    label1.image = img
    label1.grid(row=baris, column=0)

#######################################################################################################################
#######################################################################################################################

root = Tk()
root.geometry("1920x10800+0+0")
root.title("Restaurant Nusantara")

image= (Image.open("img/bg.png"))
resized_image= image.resize((1920,1080), Image.ANTIALIAS)
img= ImageTk.PhotoImage(resized_image)
label1 = Label(root, image=img)
label1.image = img
label1.place(x = 0,y = 0)

judulCont = Frame(root, width = 1600, height=50, relief=SUNKEN, bg="#F6F6F6")
judulCont.pack(side=TOP)

inputCont = Frame(root, width = 900, height=700, relief=SUNKEN, bg="#F6F6F6")
inputCont.pack(side=TOP)

infoCont = Frame(root, width = 900, height=500, relief=SUNKEN, bg="#F6F6F6")
infoCont.pack(side=TOP)

buttonCont = Frame(root, width = 900, height=500, relief=SUNKEN, bg="#F6F6F6")
buttonCont.pack(side=TOP)

########## FETCH TIME ##########
localtime=time.asctime(time.localtime(time.time()))

########## TAMPILAN JUDUL ##########
lblgaris1= Label(judulCont, text=" ", bg="#F6F6F6")
lblgaris1.grid(row=0, columnspan=15)

lblgaris2 = Label(judulCont, text=" ",bg="#F6F6F6")
lblgaris2.grid(row=1, columnspan=15)

labelResto = Label(judulCont, font=( 'Consolas' , 30, 'bold' ), text="Restaurant Nusantara", fg="steel blue", bg="#F6F6F6", bd=10, anchor='w')
labelResto.grid(row=2, column=0)
labelWaktu = Label(judulCont, font=( 'Consolas' , 20, ), text=localtime, fg="steel blue", bg="#F6F6F6", anchor=W)
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
lblgaris1= Label(inputCont, text=" ",bg="#F6F6F6")
lblgaris1.grid(row=0, columnspan=15)

lblgaris2 = Label(inputCont, text=" ",bg="#F6F6F6")
lblgaris2.grid(row=1, columnspan=15)

labelOrder = Label(inputCont, font=( 'Consolas' , 18, 'bold' ), text="Id Order", fg="steel blue", bg="#F6F6F6", bd=10, anchor='w', padx=10, pady=10)
labelOrder.grid(row=2, column=1)
inputOrder = Entry(inputCont, font=('Consolas' , 18, 'bold'), textvariable=idOrder , bd=6, insertwidth=4, bg="powder blue" , justify='right')
inputOrder.grid(row=2, column=2)


labelMakanan1 = Label(inputCont, font=( 'Consolas' , 18, 'bold' ), text="Nasi Goreng", fg="steel blue", bg="#F6F6F6", bd=10, anchor='w', padx=10, pady=10)
labelMakanan1.grid(row=3, column=1)
inputMakanan1 = Entry(inputCont, font=('Consolas' , 18, 'bold'), textvariable=Makanan1 , bd=6, insertwidth=4, bg="powder blue" , justify='right')
inputMakanan1.grid(row=3, column=2)

inputGambar("img/makanan1.png", 3)

labelMakanan2 = Label(inputCont, font=( 'Consolas' , 18, 'bold' ), text="Nasi Uduk", fg="steel blue", bg="#F6F6F6",  bd=10, anchor='w', padx=10, pady=10)
labelMakanan2.grid(row=4, column=1)
inputMakanan2 = Entry(inputCont, font=('Consolas' , 18, 'bold'), textvariable=Makanan2 , bd=6, insertwidth=4, bg="powder blue" , justify='right')
inputMakanan2.grid(row=4, column=2)

inputGambar("img/makanan2.png", 4)

labelMakanan3 = Label(inputCont, font=( 'Consolas' , 18, 'bold' ), text="Lontong Sayur", fg="steel blue", bg="#F6F6F6", bd=10, anchor='w', padx=10, pady=10)
labelMakanan3.grid(row=5, column=1)
inputMakanan3 = Entry(inputCont, font=('Consolas' , 18, 'bold'), textvariable=Makanan3 , bd=6, insertwidth=4, bg="powder blue" , justify='right')
inputMakanan3.grid(row=5, column=2)

inputGambar("img/makanan3.png", 5)

labelMakanan4 = Label(inputCont, font=( 'Consolas' , 18, 'bold' ), text="Bubur Ayam", fg="steel blue", bg="#F6F6F6", bd=10, anchor='w', padx=10, pady=10)
labelMakanan4.grid(row=6, column=1)
inputMakanan4= Entry(inputCont, font=('Consolas' , 18, 'bold'), textvariable=Makanan4 , bd=6, insertwidth=4, bg="powder blue" , justify='right')
inputMakanan4.grid(row=6, column=2)

inputGambar("img/makanan4.png", 6)

labelMakanan5 = Label(inputCont, font=( 'Consolas' , 18, 'bold' ), text="Soto Betawi", fg="steel blue", bg="#F6F6F6", bd=10, anchor='w', padx=10, pady=10)
labelMakanan5.grid(row=7, column=1)
inputMakanan5 = Entry(inputCont, font=('Consolas' , 18, 'bold'), textvariable=Makanan5, bd=6, insertwidth=4, bg="powder blue" , justify='right')
inputMakanan5.grid(row=7, column=2)

inputGambar("img/makanan5.png", 7)

labelMinuman = Label(inputCont, font=( 'Consolas' , 18, 'bold' ), text="Teh Manis", fg="steel blue", bg="#F6F6F6",  bd=10, anchor='w', padx=10, pady=10)
labelMinuman.grid(row=8, column=1)
inputMinuman = Entry(inputCont, font=('Consolas' , 18, 'bold'), textvariable=Minuman , bd=6, insertwidth=4, bg="powder blue" , justify='right')
inputMinuman.grid(row=8, column=2)

inputGambar("img/minuman.png", 8)

#--------------------------------------------------------------------------------------

labelSubTotal = Label(inputCont, font=( 'Consolas' , 18, 'bold' ), text="Sub Total", fg="steel blue", bg="#F6F6F6", bd=10, anchor='w')
labelSubTotal.grid(row=2, column=3)
boxSubTotal = Entry(inputCont, font=('Consolas' , 18, 'bold'), textvariable=Subtotal , bd=6, insertwidth=4, bg="powder blue" , justify='right')
boxSubTotal.grid(row=2, column=4)

labelService = Label(inputCont, font=( 'Consolas' , 18, 'bold' ), text="Service Charge", fg="steel blue", bg="#F6F6F6", bd=10, anchor='w')
labelService.grid(row=3, column=3)
boxService = Entry(inputCont, font=('Consolas' , 18, 'bold'), textvariable=Service_Charge , bd=6, insertwidth=4, bg="powder blue" , justify='right')
boxService.grid(row=3, column=4)

labelTax = Label(inputCont, font=( 'Consolas' , 18, 'bold' ), text="Tax", fg="steel blue", bg="#F6F6F6", bd=10, anchor='w')
labelTax.grid(row=4, column=3)
boxTax = Entry(inputCont, font=('Consolas' , 18, 'bold'), textvariable=Tax , bd=6, insertwidth=4, bg="powder blue" , justify='right')
boxTax.grid(row=4, column=4)

labelTotal = Label(inputCont, font=( 'Consolas' , 18, 'bold' ), text="Total", fg="steel blue", bg="#F6F6F6",  bd=10, anchor='w')
labelTotal.grid(row=5, column=3)
boxTotal = Entry(inputCont, font=('Consolas' , 18, 'bold'), textvariable=Total , bd=6, insertwidth=4, bg="powder blue" , justify='right')
boxTotal.grid(row=5, column=4)

labelUang = Label(inputCont, font=( 'Consolas' , 18, 'bold' ), text="Uang", fg="steel blue", bg="#F6F6F6", bd=10, anchor='w')
labelUang.grid(row=7, column=3)
inputUang = Entry(inputCont, font=('Consolas' , 18, 'bold'), textvariable=Uang , bd=6, insertwidth=4, bg="powder blue" , justify='right')
inputUang.grid(row=7, column=4)

labelKembalian = Label(inputCont, font=( 'Consolas' , 18, 'bold' ), text="Kembalian", fg="steel blue", bg="#F6F6F6", bd=10, anchor='w')
labelKembalian.grid(row=8, column=3)
boxKembalian = Entry(inputCont, font=('Consolas' , 18, 'bold'), textvariable=Kembalian , bd=6, insertwidth=4, bg="powder blue" , justify='right')
boxKembalian.grid(row=8, column=4)


########## TAMPILAN INFO KESELURUHAN ##########
lblgaris1= Label(infoCont, text=" ", bg="#F6F6F6")
lblgaris1.grid(row=0, columnspan=15)

lblgaris2 = Label(infoCont, text=" ", bg="#F6F6F6")
lblgaris2.grid(row=1, columnspan=15)

lblpelanggan = Label(infoCont, font=( 'Consolas' , 18, 'bold' ), text="Total Coustomer", fg="steel blue", bg="#F6F6F6", justify=RIGHT)
lblpelanggan.grid(row=2, column=0)
lblpelanggan = Label(infoCont, font=( 'Consolas' , 18, 'bold' ), textvariable=Pelanggan, fg="steel blue", bg="#F6F6F6",  justify=RIGHT)
lblpelanggan.grid(row=3, column=0)

lblpelanggan = Label(infoCont, font=( 'Consolas' , 18, 'bold' ), text="Income", fg="steel blue", bg="#F6F6F6", justify=RIGHT)
lblpelanggan.grid(row=4, column=0)
lblpelanggan = Label(infoCont, font=( 'Consolas' , 18, 'bold' ), textvariable=Income, fg="steel blue", bg="#F6F6F6", justify=RIGHT)
lblpelanggan.grid(row=5, column=0)

########## TOMBOL MENU ##########
lblgaris1= Label(buttonCont, text=" ", fg="steel blue", bg="#F6F6F6", )
lblgaris1.grid(row=0, columnspan=15)

lblgaris2 = Label(buttonCont, text=" ", fg="steel blue", bg="#F6F6F6", )
lblgaris2.grid(row=1, columnspan=15)

buttonMenu = Button(buttonCont, padx=16, pady=8, bd=10 , fg="black", font=('Consolas' , 16, 'bold'), width=10, text="MENU", bg="powder blue", command=list_menu)
buttonMenu.grid(row=2, column=0)

buttonTotal = Button(buttonCont, padx=16, pady=8, bd=10 , fg="black", font=('Consolas' , 16, 'bold'), width=10, text="TOTAL", bg="powder blue", command=totalFunction)
buttonTotal.grid(row=2, column=1)

buttonReset = Button(buttonCont, padx=16, pady=8, bd=10 , fg="black", font=('Consolas' , 16, 'bold'), width=10, text="RESET", bg="powder blue", command=resetFunction)
buttonReset.grid(row=2, column=3)

buttonExit = Button(buttonCont, padx=16, pady=8, bd=10 , fg="black", font=('Consolas' , 16, 'bold'), width=10, text="EXIT", bg="powder blue", command=exitFunction)
buttonExit.grid(row=2, column=4)

root.mainloop()
