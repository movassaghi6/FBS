import tkinter
from tkinter import messagebox
from tkinter import Frame
from tkinter import Label
from tkinter import Text
import tkinter as tk
import time
import datetime
import random

root = tk.Tk()
root.geometry("1350x750+0+0")
root.title("food billing system")
root.configure(background='orange')

Tops = Frame(root,bg='orange',bd=20,pady=5,relief=tk.RIDGE)
Tops.pack(side=tk.TOP)

lblTitle=Label(Tops,font=('arial',60,'bold'),text='سيستم حسابرسي غذا',bd=21,bg='black',
                fg='cornsilk',justify=tk.CENTER)
lblTitle.grid(row=0)


ReceiptCal_F = Frame(root,bg='orange',bd=3,relief=tk.RIDGE)
ReceiptCal_F.pack(side=tk.RIGHT)

Buttons_F=Frame(ReceiptCal_F,bg='orange',bd=3,relief=tk.RIDGE)
Buttons_F.pack(side=tk.BOTTOM)

Cal_F=Frame(ReceiptCal_F,bg='orange',bd=6,relief=tk.RIDGE)
Cal_F.pack(side=tk.TOP)

Receipt_F=Frame(ReceiptCal_F,bg='orange',bd=1,relief=tk.RIDGE)
Receipt_F.pack(side=tk.BOTTOM)

MenuFrame = Frame(root,bg='orange',bd=10,relief=tk.RIDGE)
MenuFrame.pack(side=tk.LEFT)
Cost_F=Frame(MenuFrame,bg='orange',bd=4)
Cost_F.pack(side=tk.BOTTOM)
Drinks_F=Frame(MenuFrame,bg='orange',bd=4)
Drinks_F.pack(side=tk.TOP)


Drinks_F=Frame(MenuFrame,bg='orange',bd=4,relief=tk.RIDGE)
Drinks_F.pack(side=tk.LEFT)
Food_F=Frame(MenuFrame,bg='orange',bd=4,relief=tk.RIDGE)
Food_F.pack(side=tk.RIGHT)
###################################################variables################################################

var1=tk.IntVar()
var2=tk.IntVar()
var3=tk.IntVar()
var4=tk.IntVar()
var5=tk.IntVar()
var6=tk.IntVar()
var7=tk.IntVar()
var8=tk.IntVar()
var9=tk.IntVar()
var10=tk.IntVar()
var11=tk.IntVar()
var12=tk.IntVar()
var13=tk.IntVar()
var14=tk.IntVar()
var15=tk.IntVar()
var16=tk.IntVar()

DateofOrder = tk.StringVar()
Receipt_Ref = tk.StringVar()
PaidTax = tk.StringVar()
SubTotal = tk.StringVar()
TotalCost = tk.StringVar()
CostofFood = tk.StringVar()
CostofDrinks = tk.StringVar()
ServiceCharge = tk.StringVar()

text_Input = tk.StringVar()
operator = ""

E_Sprite = tk.StringVar()
E_Pepsi = tk.StringVar()
E_Miranda = tk.StringVar()
E_Mohito = tk.StringVar()
E_Redbull = tk.StringVar()
E_Fanta = tk.StringVar()
E_CocaCola = tk.StringVar()
E_Hype = tk.StringVar()


E_HotDog = tk.StringVar()
E_HamBurger = tk.StringVar()
E_Pasta = tk.StringVar()
E_CheeseBurger = tk.StringVar()
E_ChickenBurger = tk.StringVar()
E_MiniPizza = tk.StringVar()
E_DoubleBurger = tk.StringVar()
E_Pizza = tk.StringVar()

E_Sprite.set("0")
E_Pepsi.set("0")
E_Miranda.set("0")
E_Mohito.set("0")
E_Redbull.set("0")
E_Fanta.set("0")
E_CocaCola.set("0")
E_Hype.set("0")

E_HotDog.set("0")
E_HamBurger.set("0")
E_Pasta.set("0")
E_CheeseBurger.set("0")
E_ChickenBurger.set("0")
E_MiniPizza.set("0")
E_DoubleBurger.set("0")
E_Pizza.set("0")

DateofOrder.set(time.strftime("%d/%m/%y"))

##########################################Function Declaration####################################################

def iExit():
    iExit=tkinter.messagebox.askyesno("Exit Restaurant System","Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

def Reset():

    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofFood.set("")
    CostofDrinks.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0",tk.END)


    E_Sprite.set("0")
    E_Pepsi.set("0")
    E_Miranda.set("0")
    E_Mohito.set("0")
    E_Redbull.set("0")
    E_Fanta.set("0")
    E_CocaCola.set("0")
    E_Hype.set("0")
    E_HotDog.set("0")
    E_HamBurger.set("0")
    E_Pasta.set("0")
    E_CheeseBurger.set("0")
    E_ChickenBurger.set("0")
    E_MiniPizza.set("0")
    E_DoubleBurger.set("0")
    E_Pizza.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)


    txtSprite.configure(state=tk.DISABLED)
    txtPepsi.configure(state=tk.DISABLED)
    txtMiranda.configure(state=tk.DISABLED)
    txtMohito.configure(state=tk.DISABLED)
    txtRedbull.configure(state=tk.DISABLED)
    txtFanta.configure(state=tk.DISABLED)
    txtCocaCola.configure(state=tk.DISABLED)
    txtHype.configure(state=tk.DISABLED)
    txtHotDog.configure(state=tk.DISABLED)
    txtHamBurger.configure(state=tk.DISABLED)
    txtPasta.configure(state=tk.DISABLED)
    txtCheeseBurger.configure(state=tk.DISABLED)
    txtChickenBurger.configure(state=tk.DISABLED)
    txtMiniPizza.configure(state=tk.DISABLED)
    txtDoubleBurger.configure(state=tk.DISABLED)
    txtPizza.configure(state=tk.DISABLED)

def CostofItem():
    Item1=float(E_Sprite.get())
    Item2=float(E_Pepsi.get())
    Item3=float(E_Miranda.get())
    Item4=float(E_Mohito.get())
    Item5=float(E_Redbull.get())
    Item6=float(E_Fanta.get())
    Item7=float(E_CocaCola.get())
    Item8=float(E_Hype.get())

    Item9=float(E_HotDog.get())
    Item10=float(E_HamBurger.get())
    Item11=float(E_Pasta.get())
    Item12=float(E_CheeseBurger.get())
    Item13=float(E_ChickenBurger.get())
    Item14=float(E_MiniPizza.get())
    Item15=float(E_DoubleBurger.get())
    Item16=float(E_Pizza.get())

    PriceofDrinks =(Item1 * 30) + (Item2 * 30) + (Item3 * 400) + (Item4 * 30) + (Item5 * 175) + (Item6 * 30) + (Item7 * 30) + (Item8 * 60)

    PriceofFood =(Item9 * 150) + (Item10 * 300) + (Item11 * 280) + (Item12 * 180) + (Item13 * 220) + (Item14 * 250) + (Item15 * 340) + (Item16 * 450)



    DrinksPrice = "Rial",str('%.2f'%(PriceofDrinks*1000))
    FoodPrice =  "Rial",str('%.2f'%(PriceofFood*1000))
    CostofFood.set(FoodPrice)
    CostofDrinks.set(DrinksPrice)
    SC = "Rial",str('%.2f'%(15.9*1000))
    ServiceCharge.set(SC)

    SubTotalofITEMS = "Rial",str('%.2f'%((PriceofDrinks + PriceofFood + 1.59)*1000))
    SubTotal.set(SubTotalofITEMS)

    Tax = "Rial",str('%.2f'%((PriceofDrinks + PriceofFood + 15.9) * 0.09 *1000))
    PaidTax.set(Tax)

    TT=((PriceofDrinks + PriceofFood + 1.59) * 0.09 * 1000)
    TC="Rial",str('%.2f'%((PriceofDrinks + PriceofFood + 15.9 + TT)*10))
    TotalCost.set(TC)


def chkSprite():
    if(var1.get() == 1):
        txtSprite.configure(state = tk.NORMAL)
        txtSprite.focus()
        txtSprite.delete('0',tk.END)
        E_Sprite.set("")
    elif(var1.get() == 0):
        txtSprite.configure(state = tk.DISABLED)
        E_Sprite.set("0")

def chkPepsi():
    if(var2.get() == 1):
        txtPepsi.configure(state = tk.NORMAL)
        txtPepsi.focus()
        txtPepsi.delete('0',tk.END)
        E_Pepsi.set("")
    elif(var2.get() == 0):
        txtPepsi.configure(state = tk.DISABLED)
        E_Pepsi.set("0")

def chk_Miranda():
    if(var3.get() == 1):
        txtMiranda.configure(state = tk.NORMAL)
        txtMiranda.delete('0',tk.END)
        txtMiranda.focus()
    elif(var3.get() == 0):
        txtMiranda.configure(state = tk.DISABLED)
        E_Miranda.set("0")

def chk_Mohito():
    if(var4.get() == 1):
        txtMohito.configure(state = tk.NORMAL)
        txtMohito.delete('0',tk.END)
        txtMohito.focus()
    elif(var4.get() == 0):
        txtMohito.configure(state = tk.DISABLED)
        E_Mohito.set("0")

def chk_Redbull():
    if(var5.get() == 1):
        txtRedbull.configure(state = tk.NORMAL)
        txtRedbull.delete('0',tk.END)
        txtRedbull.focus()
    elif(var5.get() == 0):
        txtRedbull.configure(state = tk.DISABLED)
        E_Redbull.set("0")

def chk_Fanta():
    if(var6.get() == 1):
        txtFanta.configure(state = tk.NORMAL)
        txtFanta.delete('0',tk.END)
        txtFanta.focus()
    elif(var6.get() == 0):
        txtFanta.configure(state = tk.DISABLED)
        E_Fanta.set("0")

def chk_CocaCola():
    if(var7.get() == 1):
        txtCocaCola.configure(state = tk.NORMAL)
        txtCocaCola.delete('0',tk.END)
        txtCocaCola.focus()
    elif(var7.get() == 0):
        txtCocaCola.configure(state = tk.DISABLED)
        E_CocaCola.set("0")

def chk_Hype():
    if(var8.get() == 1):
        txtHype.configure(state = tk.NORMAL)
        txtHype.delete('0',tk.END)
        txtHype.focus()
    elif(var8.get() == 0):
        txtHype.configure(state = tk.DISABLED)
        E_Hype.set("0")

def chk_HotDog():
    if(var9.get() == 1):
        txtHotDog.configure(state = tk.NORMAL)
        txtHotDog.delete('0',tk.END)
        txtHotDog.focus()
    elif(var9.get() == 0):
        txtHotDog.configure(state = tk.DISABLED)
        E_HotDog.set("0")

def chk_HamBurger():
    if(var10.get() == 1):
        txtHamBurger.configure(state = tk.NORMAL)
        txtHamBurger.delete('0',tk.END)
        txtHamBurger.focus()
    elif(var10.get() == 0):
        txtHamBurger.configure(state = tk.DISABLED)
        E_HamBurger.set("0")

def chk_Pasta():
    if(var11.get() == 1):
        txtPasta.configure(state = tk.NORMAL)
        txtPasta.delete('0',tk.END)
        txtPasta.focus()
    elif(var11.get() == 0):
        txtPasta.configure(state = tk.DISABLED)
        E_Pasta.set("0")

def chk_CheeseBurger():
    if(var12.get() == 1):
        txtCheeseBurger.configure(state = tk.NORMAL)
        txtCheeseBurger.delete('0',tk.END)
        txtCheeseBurger.focus()
    elif(var12.get() == 0):
        txtCheeseBurger.configure(state = tk.DISABLED)
        E_CheeseBurger.set("0")

def chk_ChickenBurger():
    if(var13.get() == 1):
        txtChickenBurger.configure(state = tk.NORMAL)
        txtChickenBurger.delete('0',tk.END)
        txtChickenBurger.focus()
    elif(var13.get() == 0):
        txtChickenBurger.configure(state = tk.DISABLED)
        E_ChickenBurger.set("0")

def chk_MiniPizza():
    if(var14.get() == 1):
        txtMiniPizza.configure(state = tk.NORMAL)
        txtMiniPizza.delete('0',tk.END)
        txtMiniPizza.focus()
    elif(var14.get() == 0):
        txtMiniPizza.configure(state = tk.DISABLED)
        E_MiniPizza.set("0")

def chk_DoubleBurger():
    if(var15.get() == 1):
        txtDoubleBurger.configure(state =tk. NORMAL)
        txtDoubleBurger.delete('0',tk.END)
        txtDoubleBurger.focus()
    elif(var15.get() == 0):
        txtDoubleBurger.configure(state = tk.DISABLED)
        E_DoubleBurger.set("0")

def chk_Pizza():
    if(var16.get() == 1):
        txtPizza.configure(state = tk.NORMAL)
        txtPizza.delete('0',tk.END)
        txtPizza.focus()
    elif(var16.get() == 0):
        txtPizza.configure(state = tk.DISABLED)
        E_Pizza.set("0")

def Receipt():
    txtReceipt.delete("1.0",tk.END)
    x=random.randint(10908,500876)
    randomRef= str(x)
    Receipt_Ref.set("Bill"+ randomRef)


    txtReceipt.insert(tk.END,'\t\t\t'+Receipt_Ref.get() +'\t'+ DateofOrder.get() +'\n')
    txtReceipt.insert(tk.END,'اقلام\t\t\t\t'+"قيمت اقلام \n")
    txtReceipt.insert(tk.END,'اسپرايت:\t\t\t\t' + E_Sprite.get() +'\n')
    txtReceipt.insert(tk.END,'پپسي:\t\t\t\t'+ E_Pepsi.get()+'\n')
    txtReceipt.insert(tk.END,'ميراندا:\t\t\t\t'+ E_Miranda.get()+'\n')
    txtReceipt.insert(tk.END,'موهيتو:\t\t\t\t'+ E_Mohito.get()+'\n')
    txtReceipt.insert(tk.END,'ردبول:\t\t\t\t'+ E_Redbull.get()+'\n')
    txtReceipt.insert(tk.END,'فانتا:\t\t\t\t'+ E_Fanta.get()+'\n')
    txtReceipt.insert(tk.END,'کوکاکولا:\t\t\t\t'+ E_CocaCola.get()+'\n')
    txtReceipt.insert(tk.END,'هايپ:\t\t\t\t'+ E_Hype.get()+'\n')
    txtReceipt.insert(tk.END,'هات داگ:\t\t\t\t'+ E_HotDog.get()+'\n')
    txtReceipt.insert(tk.END,'همبرگر:\t\t\t\t'+ E_HamBurger.get()+'\n')
    txtReceipt.insert(tk.END,'پاستا\t\t\t\t'+ E_Pasta.get()+'\n')
    txtReceipt.insert(tk.END,'چيزبرگر:\t\t\t\t'+ E_CheeseBurger.get()+'\n')
    txtReceipt.insert(tk.END,'چيکن برگر:\t\t\t\t'+ E_ChickenBurger.get()+'\n')
    txtReceipt.insert(tk.END,'ميني پيتزا:\t\t\t\t'+ E_MiniPizza.get()+'\n')
    txtReceipt.insert(tk.END,'دوبل برگر:\t\t\t\t'+ E_DoubleBurger.get()+'\n')
    txtReceipt.insert(tk.END,'پيتزا:\t\t\t\t'+ E_Pizza.get()+'\n')
    txtReceipt.insert(tk.END,'قيمت نوشيدني ها:\t\t\t'+ CostofDrinks.get()+"\n")
    txtReceipt.insert(tk.END,'ماليات:\t\t\t'+PaidTax.get()+"\n")
    txtReceipt.insert(tk.END,'قيمت غذاها:\t\t\t'+ CostofFood.get()+"\n")
    txtReceipt.insert(tk.END,'زيرمجموع:\t\t\t'+ str(SubTotal.get())+"\n")
    txtReceipt.insert(tk.END,'هزينه خدمات:\t\t\t'+ ServiceCharge.get()+"\n")
    txtReceipt.insert(tk.END,'کل:\t\t\t'+ str(TotalCost.get())+"\n")


#########################################Drinks####################################################################
Sprite=tk.Checkbutton(Drinks_F,text='اسپرايت',variable=var1,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='orange',command=chkSprite).grid(row=0,sticky=tk.W)
Pepsi=tk.Checkbutton(Drinks_F,text='پپسي',variable=var2,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='orange',command=chkPepsi).grid(row=1,sticky=tk.W)
Miranda=tk.Checkbutton(Drinks_F,text='ميراندا',variable=var3,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='orange',command=chk_Miranda).grid(row=2,sticky=tk.W)
Mohito=tk.Checkbutton(Drinks_F,text='موهيتو',variable=var4,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='orange',command=chk_Mohito).grid(row=3,sticky=tk.W)
Redbull=tk.Checkbutton(Drinks_F,text='ردبول',variable=var5,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='orange',command=chk_Redbull).grid(row=4,sticky=tk.W)
Fanta=tk.Checkbutton(Drinks_F,text='فانتا',variable=var6,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='orange',command=chk_Fanta).grid(row=5,sticky=tk.W)
CocaCola=tk.Checkbutton(Drinks_F,text='کوکاکولا',variable=var7,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='orange',command=chk_CocaCola).grid(row=6,sticky=tk.W)
Hype=tk.Checkbutton(Drinks_F,text='هايپ',variable=var8,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='orange',command=chk_Hype).grid(row=7,sticky=tk.W)
##############################################Drink Entry###############################################################

txtSprite = tk.Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=tk.LEFT,state=tk.DISABLED
                        ,textvariable=E_Sprite)
txtSprite.grid(row=0,column=1)

txtPepsi = tk.Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=tk.LEFT,state=tk.DISABLED
                        ,textvariable=E_Pepsi)
txtPepsi.grid(row=1,column=1)

txtMiranda = tk.Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=tk.LEFT,state=tk.DISABLED
                        ,textvariable=E_Miranda)
txtMiranda.grid(row=2,column=1)

txtMohito= tk.Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=tk.LEFT,state=tk.DISABLED
                        ,textvariable=E_Mohito)
txtMohito.grid(row=3,column=1)

txtRedbull = tk.Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=tk.LEFT,state=tk.DISABLED
                        ,textvariable=E_Redbull)
txtRedbull.grid(row=4,column=1)

txtFanta = tk.Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=tk.LEFT,state=tk.DISABLED
                        ,textvariable=E_Fanta)
txtFanta.grid(row=5,column=1)

txtCocaCola = tk.Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=tk.LEFT,state=tk.DISABLED
                        ,textvariable=E_CocaCola)
txtCocaCola.grid(row=6,column=1)

txtHype = tk.Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=tk.LEFT,state=tk.DISABLED
                        ,textvariable=E_Hype)
txtHype.grid(row=7,column=1)
#############################################Foods######################################################################

HotDog = tk.Checkbutton(Food_F,text="هات داگ\t\t\t ",variable=var9,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='orange',command=chk_HotDog).grid(row=0,sticky=tk.W)
HamBurger = tk.Checkbutton(Food_F,text="همبرگر",variable=var10,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='orange',command=chk_HamBurger).grid(row=1,sticky=tk.W)
Pasta = tk.Checkbutton(Food_F,text="پاستا ",variable=var11,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='orange',command=chk_Pasta).grid(row=2,sticky=tk.W)
CheeseBurger = tk.Checkbutton(Food_F,text="چيزبرگر ",variable=var12,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='orange',command=chk_CheeseBurger).grid(row=3,sticky=tk.W)
ChickenBurger = tk.Checkbutton(Food_F,text="چيکن برگر ",variable=var13,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='orange',command=chk_ChickenBurger).grid(row=4,sticky=tk.W)
MiniPizza = tk.Checkbutton(Food_F,text="ميني پيتزا ",variable=var14,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='orange',command=chk_MiniPizza).grid(row=5,sticky=tk.W)
DubleBuerger = tk.Checkbutton(Food_F,text="دوبل برگر ",variable=var15,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='orange',command=chk_DoubleBurger).grid(row=6,sticky=tk.W)
Pizza = tk.Checkbutton(Food_F,text="پيتزا ",variable=var16,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='orange',command=chk_Pizza).grid(row=7,sticky=tk.W)
################################################Entry Box For Cake##########################################################
txtHotDog=tk.Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=tk.LEFT,state=tk.DISABLED,
                        textvariable=E_HotDog)
txtHotDog.grid(row=0,column=1)

txtHamBurger=tk.Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=tk.LEFT,state=tk.DISABLED,
                        textvariable=E_HamBurger)
txtHamBurger.grid(row=1,column=1)

txtPasta=tk.Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=tk.LEFT,state=tk.DISABLED,
                        textvariable=E_Pasta)
txtPasta.grid(row=2,column=1)

txtCheeseBurger=tk.Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=tk.LEFT,state=tk.DISABLED,
                        textvariable=E_CheeseBurger)
txtCheeseBurger.grid(row=3,column=1)

txtChickenBurger=tk.Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=tk.LEFT,state=tk.DISABLED,
                        textvariable=E_ChickenBurger)
txtChickenBurger.grid(row=4,column=1)

txtMiniPizza=tk.Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=tk.LEFT,state=tk.DISABLED,
                        textvariable=E_MiniPizza)
txtMiniPizza.grid(row=5,column=1)

txtDoubleBurger=tk.Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=tk.LEFT,state=tk.DISABLED,
                        textvariable=E_DoubleBurger)
txtDoubleBurger.grid(row=6,column=1)

txtPizza=tk.Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=tk.LEFT,state=tk.DISABLED,
                        textvariable=E_Pizza)
txtPizza.grid(row=7,column=1)
###########################################ToTal Cost################################################################################
lblCostofDrinks=Label(Cost_F,font=('arial',14,'bold'),text='قيمت نوشيدني ها\t',bg='orange',
                fg='black',justify=tk.CENTER)
lblCostofDrinks.grid(row=0,column=0,sticky=tk.W)
txtCostofDrinks=tk.Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=tk.RIGHT,textvariable=CostofDrinks)
txtCostofDrinks.grid(row=0,column=1)

lblCostofFood=Label(Cost_F,font=('arial',14,'bold'),text='قيمت غذاها  ',bg='orange',
                fg='black',justify=tk.CENTER)
lblCostofFood.grid(row=1,column=0,sticky=tk.W)
txtCostofFood=tk.Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=tk.RIGHT,textvariable=CostofFood)
txtCostofFood.grid(row=1,column=1)

lblServiceCharge=Label(Cost_F,font=('arial',14,'bold'),text='هزينه خدمات',bg='orange',
                fg='black',justify=tk.CENTER)
lblServiceCharge.grid(row=2,column=0,sticky=tk.W)
txtServiceCharge=tk.Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=tk.RIGHT,textvariable=ServiceCharge)
txtServiceCharge.grid(row=2,column=1)
###########################################################Payment information###################################################

lblPaidTax=Label(Cost_F,font=('arial',14,'bold'),text='\tماليات',bg='orange',bd=7,
                fg='black',justify=tk.CENTER)
lblPaidTax.grid(row=0,column=2,sticky=tk.W)
txtPaidTax=tk.Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=tk.RIGHT,textvariable=PaidTax)
txtPaidTax.grid(row=0,column=3)

lblSubTotal=Label(Cost_F,font=('arial',14,'bold'),text='\tزيرکل',bg='orange',bd=7,
                fg='black',justify=tk.CENTER)
lblSubTotal.grid(row=1,column=2,sticky=tk.W)
txtSubTotal=tk.Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=tk.RIGHT,textvariable=SubTotal)
txtSubTotal.grid(row=1,column=3)

lblTotalCost=Label(Cost_F,font=('arial',14,'bold'),text='\tکل',bg='orange',bd=7,
                fg='black',justify=tk.CENTER)
lblTotalCost.grid(row=2,column=2,sticky=tk.W)
txtTotalCost=tk.Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=tk.RIGHT,textvariable=TotalCost)
txtTotalCost.grid(row=2,column=3)

#############################################RECEIPT###############################################################################
txtReceipt=Text(Receipt_F,width=46,height=12,bg='white',bd=4,font=('arial',12,'bold'))
txtReceipt.grid(row=0,column=0)


###########################################BUTTONS################################################################################
btnTotal=tk.Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='مجموع',
                        bg='orange',command=CostofItem).grid(row=0,column=0)
btnReceipt=tk.Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='رسيد',
                        bg='orange',command=Receipt).grid(row=0,column=1)
btnReset=tk.Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='تنظيم مجدد',
                        bg='orange',command=Reset).grid(row=0,column=2)
btnExit=tk.Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='خروج',
                        bg='orange',command=iExit).grid(row=0,column=3)

###################################Calculator Display################################################################################




def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator = ""
    text_Input.set("")

def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""




#############################################Calculator###############################################################################
txtDisplay=tk.Entry(Cal_F,width=45,bg='white',bd=4,font=('arial',12,'bold'),justify=tk.RIGHT,textvariable=text_Input)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")

###########################################CALCULATOR BUTTONS################################################################################
btn7=tk.Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='7',
                        bg='orange',command=lambda:btnClick(7)).grid(row=2,column=0)
btn8=tk.Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='8',
                        bg='orange',command=lambda:btnClick(8)).grid(row=2,column=1)
btn9=tk.Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='9',
                        bg='orange',command=lambda:btnClick(9)).grid(row=2,column=2)
btnAdd=tk.Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='+',
                        bg='orange',command=lambda:btnClick('+')).grid(row=2,column=3)
###########################################CALCULATOR BUTTONS################################################################################
btn4=tk.Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='4',
                        bg='orange',command=lambda:btnClick(4)).grid(row=3,column=0)
btn5=tk.Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='5',
                        bg='orange',command=lambda:btnClick(5)).grid(row=3,column=1)
btn6=tk.Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='6',
                        bg='orange',command=lambda:btnClick(6)).grid(row=3,column=2)
btnSub=tk.Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='-',
                        bg='orange',command=lambda:btnClick('-')).grid(row=3,column=3)
###########################################CALCULATOR BUTTONS################################################################################
btn1=tk.Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='1',
                        bg='orange',command=lambda:btnClick(1)).grid(row=4,column=0)
btn2=tk.Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='2',
                        bg='orange',command=lambda:btnClick(2)).grid(row=4,column=1)
btn3=tk.Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='3',
                        bg='orange',command=lambda:btnClick(3)).grid(row=4,column=2)
btnMulti=tk.Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='*',
                        bg='orange',command=lambda:btnClick('*')).grid(row=4,column=3)
###########################################CALCULATOR BUTTONS################################################################################
btn0=tk.Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='0',
                        bg='orange',command=lambda:btnClick(0)).grid(row=5,column=0)
btnClear=tk.Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='C',
                        bg='orange',command=btnClear).grid(row=5,column=1)
btnEqual=tk.Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='=',
                        bg='orange',command=btnEquals).grid(row=5,column=2)
btnDiv=tk.Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='/',
                        bg='orange',command=lambda:btnClick('/')).grid(row=5,column=3)







root.mainloop()
