from tkinter import Tk,Label,Button,Entry,Frame,Text,CENTER, Toplevel
from tkinter import messagebox
from PIL import Image,ImageTk

root = Tk()
root.title('Denomination Counter')
root.configure(bg='light green')
root.geometry('650x400')

upload = Image.open("app_img.jpg")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg = 'light green')
label.place(x=180, y=20)

label1 = Label(root,text = "Hey user! Welcome to denominator Counter App.lication,"bg = 'light green')
label1.place(relx=0.5, y = 340, anchor=CENTER)
def msg():
    MsgBox = messagebox.showinfo("Alert", "Do you want do calculate the denomination count?")
    if MsgBox == 'ok':
        topwin()

button1= Button(root, text = "Let's get started!, command=msg, bg = orange",fg = "white" )
button1.place(x=260, y=360)
def topwin():
    top =  Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg='light grey')
    top.geometry("600x300+50+50")

    label = Label((top, text="Enter total amount", bg = 'light grey'))
    entry = Entry(top)
    lbl = Label(top, text="Here are number of notes for each denomination", bg='light grey')

    l1 = Label(top, text="2000", bg = 'light grey')
    l2 = Label(top, text="500", bg = 'light grey')
    l3 = Label(top, text="100", bg = 'light grey')

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
def calculator():
    try:
        global amount
        amount = int(entry.get())
        note2000 = amount// 2000
        amount %= 2000
        note500 = amount // 500
        note100 = amount // 100

        t1.delete(0, END)
        t2.delete(0, END)
        t3.delete(0, END)

        t1.insert(END, str(note2000))
        t2.insert(END, str(note500))
        t3.insert(END, str(note100))
    except ValueError:
        messagebox.showerror("Error","Please enter a valid number.")

        btn = Button(top, text= 'Calculate', command=calculator, bg = 'light blue', fg = 'white')
