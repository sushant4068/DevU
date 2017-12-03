from tkinter import*
import random
import time


root=Tk()
root.title("Restaurant Management Systems")

Tops=Frame(root,width=1600,height=50,bg="powder blue",relief=SUNKEN)
Tops.pack(side=TOP)
text_Input=StringVar()
operator=""
f1=Frame(root,width=650,height=700,bg="powder blue",relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(root,width=250,height=700,bg="powder blue",relief=SUNKEN)
f2.pack(side=RIGHT)
#========================Time============================
localtime=time.asctime(time.localtime(time.time()))

#========================Info============================
labelInfo=Label(Tops,font=("aerial",50,"bold"),text="Restaurant Management Systems",fg="Steel Blue",bd=10,anchor='w')
labelInfo.grid(row=0,column=0)
labelInfo=Label(Tops,font=("aerial",10,"bold"),text=localtime,fg="Steel Blue",bd=10,anchor='w')
labelInfo.grid(row=1,column=0)
#labelInfo.pack()

#===============================Calculator=================

def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)
    
def btnClearDisplay():
    global operator
    operator=""
    text_Input.set(operator)

def btnEqulasInput():
    global operator
    sump=str(eval(operator))
    text_Input.set(sump)
    operator=""

def Ref():
    x=random.randint(12908,50876)
    randomRef=str(x)
    rand.set(randomRef)
    CoF=float(Fries.get())
    CoB=float(Burger.get())
    CoCh=float(Chicken_Role.get())
    CoD=float(Drinks.get())
    CoT=float(Tea.get())
    CoC=float(Coffee.get())

    CosttoFries=CoF * 10.25
    CosttoBurger=CoB * 50.00
    CosttoChiken=CoCh * 100.00
    CosttoDrinks=CoD * 30.00
    CosttoTea=CoT * 8.00
    CosttoCoffee=CoC * 10.00
    
    CostToMeal="$",str("%.2f" %(CosttoFries+CosttoBurger+CosttoChiken+ CosttoDrinks+CosttoTea+CosttoCoffee))
    Pay_GST=((CosttoFries+CosttoBurger+CosttoChiken+ CosttoDrinks+CosttoTea+CosttoCoffee)*0.12)

    TotalCost=(CosttoFries+CosttoBurger+CosttoChiken+ CosttoDrinks+CosttoTea+CosttoCoffee)
    OverAllCost=TotalCost+Pay_GST
    Cost.set(TotalCost )
    GST.set(Pay_GST)
    Total.set(OverAllCost
              )
def qExit():
    root.destroy()

def Reset():
    rand.set("")
    Fries.set("")
    Burger.set("")
    GST.set("")
    Drinks.set("")
    Chicken_Role.set("")
    Tea.set("")
    Coffee.set("")
    Cost.set("")
    Total.set("")
    
    
txtDisplay=Entry(f2,font=("aerial",20,"bold"),textvariable=text_Input,bd=30,insertwidth=4,bg="powder blue",justify="right")
txtDisplay.grid(columnspan=4)
btn7=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("aerial",10,"bold"),text="7",bg="powder blue",command=lambda:btnClick(7)).grid(row=2,column=0)
btn8=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("aerial",10,"bold"),text="8",bg="powder blue",command=lambda:btnClick(8)).grid(row=2,column=1)
btn9=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("aerial",10,"bold"),text="9",bg="powder blue",command=lambda:btnClick(9)).grid(row=2,column=2)
Addition=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("aerial",10,"bold"),text="+",bg="powder blue",command=lambda:btnClick("+")).grid(row=2,column=3)
                                                                                                                                        
btn4=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("aerial",10,"bold"),text="4",bg="powder blue",command=lambda:btnClick(4)).grid(row=3,column=0)
btn5=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("aerial",10,"bold"),text="5",bg="powder blue",command=lambda:btnClick(5)).grid(row=3,column=1)
btn6=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("aerial",10,"bold"),text="6",bg="powder blue",command=lambda:btnClick(6)).grid(row=3,column=2)
Subtraction=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("aerial",10,"bold"),text="-",bg="powder blue",command=lambda:btnClick("-")).grid(row=3,column=3)

btn1=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("aerial",10,"bold"),text="1",bg="powder blue",command=lambda:btnClick(1)).grid(row=4,column=0)
btn2=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("aerial",10,"bold"),text="2",bg="powder blue",command=lambda:btnClick(2)).grid(row=4,column=1)
btn3=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("aerial",10,"bold"),text="3",bg="powder blue",command=lambda:btnClick(3)).grid(row=4,column=2)
Multiplication=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("aerial",10,"bold"),text="*",bg="powder blue",command=lambda:btnClick("*")).grid(row=4,column=3)

btn0=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("aerial",10,"bold"),text="0",bg="powder blue",command=lambda:btnClick(0)).grid(row=5,column=0)
btnClear=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("aerial",10,"bold"),text="C",bg="powder blue",command=btnClearDisplay).grid(row=5,column=1)
btnEquals=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("aerial",10,"bold"),text="=",bg="powder blue",command=btnEqulasInput).grid(row=5,column=2)
Division=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("aerial",10,"bold"),text="/",bg="powder blue",command=lambda:btnClick("/")).grid(row=5,column=3)

#-------------------------------Restaurant Food Items---------------------------------------------------------------------------------
rand=StringVar()
Fries=StringVar()
Burger=StringVar()
GST=StringVar()
Drinks=StringVar()
Chicken_Role=StringVar()
Tea=StringVar()
Coffee=StringVar()
Cost=StringVar()
Total=StringVar()

labelRef=Label(f1,font=("aerial",16,"bold"),text="Reference",bd=16,anchor="w")
labelRef.grid(row=0,column=0)
txtRef=Entry(f1,font=("aerial",16,"bold"),textvariable=rand,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtRef.grid(row=0,column=1)

labelFries=Label(f1,font=("aerial",16,"bold"),text="Fries",bd=16,anchor="w")
labelFries.grid(row=1,column=0)
txtFries=Entry(f1,font=("aerial",16,"bold"),textvariable=Fries,bd=16,insertwidth=4,bg="powder blue",justify='right')
txtFries.grid(row=1,column=1)

labelBurger=Label(f1,font=("aerial",16,"bold"),text="Burger",bd=16,anchor="w")
labelBurger.grid(row=2,column=0)
txtBurger=Entry(f1,font=("aerial",16,"bold"),textvariable=Burger,bd=16,insertwidth=4,bg="powder blue",justify='right')
txtBurger.grid(row=2,column=1)

labelDrinks=Label(f1,font=("aerial",16,"bold"),text="Drinks",bd=16,anchor="w")
labelDrinks.grid(row=3,column=0)
txtDrinks=Entry(f1,font=("aerial",16,"bold"),textvariable=Drinks,bd=16,insertwidth=4,bg="powder blue",justify='right')
txtDrinks.grid(row=3,column=1)

labelChicken_Role=Label(f1,font=("aerial",16,"bold"),text="Chicken_Role",bd=16,anchor="w")
labelChicken_Role.grid(row=4,column=0)
txtChicken_Role=Entry(f1,font=("aerial",16,"bold"),textvariable=Chicken_Role,bd=16,insertwidth=4,bg="powder blue",justify='right')
txtChicken_Role.grid(row=4,column=1)

labelTea=Label(f1,font=("aerial",16,"bold"),text="Tea",bd=16,anchor="w")
labelTea.grid(row=0,column=2)
txtTea=Entry(f1,font=("aerial",16,"bold"),textvariable=Tea,bd=16,insertwidth=4,bg="powder blue",justify='right')
txtTea.grid(row=0,column=3)

labelCoffee=Label(f1,font=("aerial",16,"bold"),text="Coffee",bd=16,anchor="w")
labelCoffee.grid(row=1,column=2)
txtCoffee=Entry(f1,font=("aerial",16,"bold"),textvariable=Coffee,bd=16,insertwidth=4,bg="powder blue",justify='right')
txtCoffee.grid(row=1,column=3)

labelCost=Label(f1,font=("aerial",16,"bold"),text="Cost",bd=16,anchor="w")
labelCost.grid(row=2,column=2)
txtCost=Entry(f1,font=("aerial",16,"bold"),textvariable=Cost,bd=16,insertwidth=4,bg="powder blue",justify='right')
txtCost.grid(row=2,column=3)

labelGST=Label(f1,font=("aerial",16,"bold"),text="GST",bd=16,anchor="w")
labelGST.grid(row=3,column=2)
txtGST=Entry(f1,font=("aerial",16,"bold"),textvariable=GST,bd=16,insertwidth=4,bg="powder blue",justify='right')
txtGST.grid(row=3,column=3)

labelTotal_Cost=Label(f1,font=("aerial",16,"bold"),text="Total_Cost",bd=16,anchor="w")
labelTotal_Cost.grid(row=4,column=2)
txtTotal_Cost=Entry(f1,font=("aerial",16,"bold"),textvariable=Total,bd=16,insertwidth=4,bg="powder blue",justify='right')
txtTotal_Cost.grid(row=4,column=3)

#===================Buttons==================================================================================

btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=("aerial",16,"bold"),width=10,text="Total",bg="powder blue",command=Ref).grid(row=6,column=1)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=("aerial",16,"bold"),width=10,text="Reset",bg="powder blue",command=Reset).grid(row=6,column=2)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=("aerial",16,"bold"),width=10,text="Exit",bg="powder blue",command=qExit).grid(row=6,column=3)

root.mainloop()

