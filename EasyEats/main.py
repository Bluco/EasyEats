from tkinter import *

restaurantData = [["McDonald's", "Low Mask Usage", "Medium Crowd", "555-6789"],
            ["Chipotle", "Medium Mask Usage", "Low crowd", "123-7777"],
            ["Heng's Fancy Eatings", "High Mask Usage", "High crowd", "420-1313"]]

index = 0
clicked = False

root = Tk()
def browse():
    global photo1, photo2, photo3
    root1 = Toplevel()
    t1 = Button(root1, text="McDonalds", command=details0).pack()
    photo1 = PhotoImage(file="mcdonalds.png")
    label = Label(root1, image=photo1).pack()
    t2 = Button(root1, text="Chipotle", command=details1).pack()
    photo2 = PhotoImage(file="chipotle.png")
    label2 = Label(root1, image=photo2).pack()
    t3 = Button(root1, text="Heng's Fancy Eatings", command=details2).pack()
    photo3 = PhotoImage(file="heng.png")
    label3 = Label(root1, image=photo3).pack()

def details0():
    global index
    index = 0
    details()

def details1():
    global index
    index = 1
    details()

def details2():
    global index
    index = 2
    details()

def details():
    root2 = Toplevel()
    t1 = Label(root2, text=restaurantData[index][0]).pack()
    t2 = Label(root2, text=restaurantData[index][1]).pack()
    t3 = Label(root2, text=restaurantData[index][2]).pack()
    t4 = Label(root2, text=restaurantData[index][3]).pack()
    #backButton = Button(root2, text="Back to Restaurants", command=browse).pack()

def login():
    global clicked
    if clicked == False:
        logt = Label(topFrame, text="Login not available at this time").pack(side=TOP)
        clicked = True

topFrame = Frame(root)
topFrame.pack()
bottomFrame1 = Frame(root)
bottomFrame1.pack()

button1 = Button(bottomFrame1, text="Log in", fg="red", command=login)
button2 = Button(bottomFrame1, text="Browse Restaurants", fg="blue", command=browse)

title = Label(topFrame, text="EasyEats")
title.pack()

button1.grid(row=1, column=0)
button2.grid(row=1, column=1)

photo = PhotoImage(file="food.png")
label = Label(root, image=photo).pack()

root.mainloop()