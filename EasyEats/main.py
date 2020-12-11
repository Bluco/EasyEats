from tkinter import *

restaurantData = [["McDonald's", "Low Mask Usage", "Medium Crowd", "555-6789"],
            ["Chipotle", "Medium Mask Usage", "Low crowd", "123-7777"],
            ["Heng's Fancy Eatings", "High Mask Usage", "High crowd", "420-1313"]]
maskCrowdData = [[1, 0, 0, 0, 1, 0], [0, 1, 0, 1, 0, 0], [0, 0, 1, 0, 0, 1]]

index = 0
clicked = False
mask = -1
crowd = -1

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
    global photo4, mask, crowd, root2
    root2 = Toplevel()
    mask=IntVar()
    crowd=IntVar()
    Label(root2, text = restaurantData[index][0]).pack()
    if index == 0:
        photo4 = PhotoImage(file="mcdonaldsmenu.png")
        Label(root2, image=photo4).pack()
    elif index == 1:
        photo4 = PhotoImage(file="chipotlemenu.png")
        Label(root2, image=photo4).pack()
    elif index == 2:
        photo4 = PhotoImage(file="heng.png")
        Label(root2, image=photo4).pack()
    Label(root2, text="Low mask usage reported").pack()
    Label(root2, text=maskCrowdData[index][0]).pack()
    Label(root2, text="Medium mask usage reported").pack()
    Label(root2, text=maskCrowdData[index][1]).pack()
    Label(root2, text="High mask usage reported").pack()
    Label(root2, text=maskCrowdData[index][2]).pack()
    Radiobutton(root2, text="Low", variable=mask, value=0, command=mask.set("0")).pack()
    Radiobutton(root2, text="Medium", variable=mask, value=1).pack()
    Radiobutton(root2, text="High", variable=mask, value=2).pack()
    Label(root2, text="Low crowd level reported").pack()
    Label(root2, text=maskCrowdData[index][3]).pack()
    Label(root2, text="Medium crowd level reported").pack()
    Label(root2, text=maskCrowdData[index][4]).pack()
    Label(root2, text="High crowd level reported").pack()
    Label(root2, text=maskCrowdData[index][5]).pack()
    Radiobutton(root2, text="Low", variable=crowd, value=0, command=crowd.set("0")).pack()
    Radiobutton(root2, text="Medium", variable=crowd, value=1).pack()
    Radiobutton(root2, text="High", variable=crowd, value=2).pack()
    t4 = Label(root2, text=restaurantData[index][3], fg="red").pack()
    submitButton = Button(root2, text="Submit Scores", command=submit).pack()

def submit():
    if mask != -1 or crowd != -1:
        if mask == 0:
            maskCrowdData[index][0] = maskCrowdData[index][0] + 1

    else:
        Label(root2, text=crowd, fg="red").pack()

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