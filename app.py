from tkinter import *
from tkinter import messagebox
import math as mth
from PIL import Image, ImageTk

root = Tk()
root.geometry('300x500')
root.resizable(False, False)
root.title('BMI Calculator')
root.iconbitmap("bmi.ico")
root.configure(bg='#0c1234')


# ----calculate function-----
def calculate():
    try:
        w = weight.get()
        h = height.get()
        bmi = int(w) / mth.pow((int(h) / 100), 2)
        if float(bmi) < 18.5:
            result.config(bg="yellow")
            result['text'] = "Underweight"
        elif 18.5 <= float(bmi) < 25:
            result.config(bg="green")
            result['text'] = "Normal"
        elif 25 <= float(bmi) < 30:
            result.config(bg="orange")
            result['text'] = "Overweight"
        elif float(bmi) >= 30:
            result.config(bg="red")
            result['text'] = "Obese"
    except (ValueError, ZeroDivisionError):
        messagebox.showerror('Error', 'An error occurred pls check ur inputs and try again')


def clear():
    weight_ent.set("")
    height_ent.set("")


# text variables
weight_ent = StringVar()
height_ent = StringVar()

# -----frame one for header-----
frame1 = Frame(root)
frame1.pack(fill=X)

# -----title section-----
title = Label(frame1, text="BMI CALCULATOR", bg="#12153b", fg='white', font=('Arial', 16, 'bold'))
title.pack(fill=X)

# -----body frame-----
frame2 = Frame(root, borderwidth=5, bg="#0c1234", height=300, width=300, bd=3, )
frame2.place(x=0, y=30)

# -----entries labels-----
text1 = Label(frame2, bg="#0c1234", fg='white', text='Weight', font=('Arial', 13, 'bold'))
text1.place(x=5, y=60)
text2 = Label(frame2, bg="#0c1234", fg='white', text='Height', font=('Arial', 13, 'bold'))
text2.place(x=5, y=125)

# -----entries------
weight = Entry(frame2, width=15, bg='white', fg='black', bd=2, relief=SUNKEN,
               font=('Arial', 12, 'bold'), textvariable=height_ent)
weight.place(x=80, y=60)
height = Entry(frame2, width=15, bg='white', fg='black', bd=2, relief=SUNKEN,
               font=('Arial', 12, 'bold'), textvariable=weight_ent)
height.place(x=80, y=120)

# ------buttons------
button = Button(frame2, text='Calculate', width=30, bg='#ff0067', bd=3,
                relief=RAISED, command=calculate, fg="white")
button.place(x=35, y=200, bordermode=OUTSIDE)

clr = Button(frame2, text='Clear', width=10, bg='blue', bd=3,
             relief=RAISED, command=clear, fg="white")
clr.place(x=105, y=250, bordermode=OUTSIDE)

# -----result section-----
result = Label(root, text="", height=6, fg='white', width=20, font=('Arial', 15, 'bold'), )
result.place(x=30, y=337)

# -----creating a photo image-----
imageIcon = Image.open('icon_hd.png')
pos = ImageTk.PhotoImage(imageIcon)
resized = imageIcon.resize((45, 45))
newImage = ImageTk.PhotoImage(resized)
imageLabel = Label(image=newImage, background='#0c1234')
imageLabel.place(x=120, y=40)

root.mainloop()
