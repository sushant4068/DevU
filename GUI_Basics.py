from tkinter import*


##Organizing Layout & Buttons
##root=Tk()
##topFrame=Frame(root)
##topFrame.pack()
##bottomFrame=Frame(root)
##bottomFrame.pack(side=BOTTOM)
##theLabel=Label(root,text="This is too easy")
##theLabel.pack()

##button1=Button(topFrame,text="Button1",fg="red")
##button2=Button(topFrame,text="Button2",fg="blue")
##button3=Button(topFrame,text="Button3",fg="green")
##button4=Button(bottomFrame,text="Button4",fg="purple")
##
##button1.pack(side=LEFT)
##button2.pack(side=LEFT)
##button3.pack(side=LEFT)
##button4.pack()
##root.mainloop()

##Fitting Widgets in Layout
##root=Tk()
##one=Label(root,text="one",bg="red",fg="white")
##one.pack()
##two=Label(root,text="two",bg="green",fg="black")
##two.pack(fill=X)
##three=Label(root,text="three",bg="blue",fg="white")
##three.pack(side=LEFT,fill=Y)
##root.mainloop()

##Grid Layout Name and Password
##root=Tk()
##label_1=Label(root,text="Name")
##label_2=Label(root,text="Password")
##entry_1=Entry(root)
##entry_2=Entry(root)
##
##label_1.grid(row=0,sticky=E)
##label_2.grid(row=1,sticky=E)
##
##entry_1.grid(row=0,column=1)
##entry_2.grid(row=1,column=1)
##
##c=Checkbutton(root,text="Keep me Logged in")
##c.grid(columnspan=2)
##root.mainloop()

##Binding Functions To Layouts (Click button to print the name)
##root=Tk()
##def printName(event):
##    print("Hello my name is Sushant!")
##button_1=Button(root,text="Print my name:")
##button_1.bind("<Button-1>",printName)
##button_1.pack()
##root.mainloop()

##Mouse Clicks
##root=Tk()
##def leftClick(event):
##    print("Left")
##
##def rightClick(event):
##    print("Right")
##
##frame=Frame(root,width=300,height=250)
##frame.bind("<Button-1>",leftClick)
##frame.bind("<Button-3>",rightClick)
##frame.pack()
##root.mainloop()

##Classes 
##class Buttons:
##    def __init__(self,master):
##        frame=Frame(master)
##        frame.pack()
##
##        self.printButton=Button(frame,text="Print Message",command=self.printMessage)
##        self.printButton.pack(side=LEFT)
##
##        self.quitButton=Button(frame,text="Quit",command=frame.quit)
##        self.quitButton.pack(side=LEFT)
##    def printMessage(self):
##        print("This is actually work")
##
##    b=Buttons(root)  ##calling objects 

##Creating drop down menus

##def doNothing():
##    print("OK OK I won't...")
##
##root=Tk()
##menu_1=Menu(root)
##root.config(menu=menu_1)
## #********Main Menu *******
##subMenu=Menu(menu_1)
##menu_1.add_cascade(label="File",menu=subMenu)
##subMenu.add_command(label="New Project..",command=doNothing)
##subMenu.add_command(label="New..",command=doNothing)
##subMenu.add_separator()
##subMenu.add_command(label="Exit",command=doNothing)
##
##editMenu=Menu(menu_1)
##menu_1.add_cascade(label="Edit",menu=editMenu)
##editMenu.add_command(label="Redo",command=doNothing)
##
### ***** Toolbar ************
##
##toolbar=Frame(root,bg="blue")
##insertButton=Button(toolbar,text="Insert Image",command=doNothing)
##insertButton.pack(side=LEFT,padx=2,pady=2)
##printButton=Button(toolbar,text="Print",command=doNothing)
##printButton.pack(side=LEFT,padx=2,pady=2)
##toolbar.pack(side=TOP,fill=X)
##
###**********Status Bar*********
##status=Label(root,text="Preparing to nothing.......",bd=1,relief=SUNKEN,anchor=W)
##status.pack(side=BOTTOM,fill=X)
##root.mainloop()

##MessageBox
##import tkinter.messagebox
##root=Tk()
##tkinter.messagebox.showinfo("Window Title","India is Great")
##answer=tkinter.messagebox.askquestion("Question 1","Why?")
##if answer=='yes':
##    print("Youth is power of nation")
##root.mainloop()

##Shapes and Graphics
##root=Tk()
##canvas=Canvas(root,width=200,height=100)
##canvas.pack()
##blackline=canvas.create_line(0,0,200,50)
##redline=canvas.create_line(0,100,200,50,fill='red')
##greenBox=canvas.create_rectangle(25,25,130,60,fill='green')
##root.mainloop()


#Images and Icons
##import os
##os.chdir("C:/Users/Sushant1/Downloads")
##print(os.getcwd())
##root=Tk()
##photo=PhotoImage(file="download.jpg")
##label=Label(root,image=photo)
##label.pack()
##root.mainloop()
