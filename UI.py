from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import tkinter as tk


root=Tk()
root.title("Torrent Download Manager")
root.geometry('700x400+300+200')
root.resizable(False,False)
root.configure(bg="#326273")

def submit():
        tname=Torrentnamevalue.get()
        mlink=MagnetlinkEntry.get(1.0,END)
        #mlink=Magnetlinkvalue.get()

        print(tname)
        print(mlink)

        messagebox.showinfo('info','Download getting started!')
     


def clear():
        Torrentnamevalue.set(' ')
       # Magnetlinkvalue.set(' ')
        MagnetlinkEntry.delete(1.0,END)

def play():
        i+=1
        print(i)
        if i%2==0:
                send
        if i%2!=0:
                send      

#logo
icon_image=PhotoImage(file="CIT_logo.png")
root.iconphoto(False,icon_image)

#heading
Label(root,text="Please Fill out this Entry:",font="arial 13",bg="#326273",fg="#fff").place(x=20,y=20)

#Label
Label(root,text="Download Method:",font=23,bg="#326273",fg="#fff").place(x=50,y=60)
Label(root,text="Torrent File Name:",font=23,bg="#326273",fg="#fff").place(x=50,y=110)
Label(root,text="Magnet Link:",font=23,bg="#326273",fg="#fff").place(x=50,y=180)

#Entry
Torrentnamevalue=StringVar()
#Magnetlinkvalue=StringVar()

#Torrent or Magnet
TM_combobox=Combobox(root,values=['Torrent File','Magnet Link'],font='arial 14',state='r',width=14)
TM_combobox.place(x=250,y=60)

TorrentnameEntry= Entry(root,textvariable=Torrentnamevalue,width=37,bd=2,font=20)
#MagnetlinkEntry= Entry(root,textvariable=Magnetlinkvalue,width=45,bd=2,font=20)
MagnetlinkEntry=Text(root,width=50,height=4,bd=4)



TorrentnameEntry.place(x=250,y=110)
MagnetlinkEntry.place(x=250,y=160)

Button(root,text="Submit",bg="#326273",fg="white",width=15,height=2,command=submit).place(x=200,y=300)
Button(root,text="Clear",bg="#326273",fg="white",width=15,height=2,command=clear).place(x=340,y=300)
Button(root,text="Exit",bg="#326273",fg="white",width=15,height=2,command=lambda:root.destroy()).place(x=480,y=300)
Button(root,text="Pause/Resume",bg="#326273",fg="white",width=15,height=2,command=play).place(x=340,y=350)

root.mainloop()
