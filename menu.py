from tkinter import *
def show_menu(stall_name,pic,dishlist):
    m=Toplevel(main)
    def show_waiting_time():
        swti = Toplevel(m)
        swti.geometry("500x400")
        paxlabel = Label(swti, text='Pax')
        paxlabel.place(relx=0, rely=0, relwidth=0.5, relheight=0.4)
        paxentry = Entry(swti)
        paxentry.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.4)

        def verify():
            try:
                global pax
                pax_str = paxentry.get()
                pax = int(pax_str)
                waitingtimelabel = Label(swti, text=pax * 2)
                waitingtimelabel.place(relx=0.5, rely=0.4, relwidth=0.5, relheight=0.4)
            except ValueError:
                warningwindow = Toplevel(swti)
                warningtext = Label(warningwindow, text="Please enter a valid time.")
                warningtext.place(relheight=0.5, relwidth=1, relx=0, rely=0)
                warningButton = Button(warningwindow, text="OK", command=warningwindow.destroy)
                warningButton.place(relheight=0.5, relwidth=1, relx=0, rely=0.5)
                warningwindow.mainloop()
        setbutton = Button(swti, text="SET", command=verify)
        setbutton.place(relx=0, rely=0.4, relwidth=0.5, relheight=0.4)
        finishbutton = Button(swti, text="FINISH", command=swti.destroy)
        finishbutton.place(relx=0, rely=0.8, relwidth=1, relheight=0.2)
        swti.mainloop()
    m.geometry("1000x800")
    titlelabel=Label(m,
                    text=stall_name,
                    fg = "yellow",
                    bg = "red",
                    font = "Helvetica 26 bold italic",
                    padx=500,
                    pady=30)
    titlelabel.place(relheight=0.1, relwidth= 1)
    logo = ImageTk.PhotoImage(Image.open(pic))#(file="C:\Users\23535\PycharmProjects\ict\venv\Mcdonalds.png")
    d1=ImageTk.PhotoImage(Image.open(dishlist[1]))
    d2 = ImageTk.PhotoImage(Image.open(dishlist[1]))
    leftlabel=Label(m,image=logo,height=800,width=500)
    leftlabel.place(relheight=0.9,relwidth= 0.5,relx=0,rely=0.1)
    dish1=Label(m,image=d1)
    dish2=Label(m,image=d2)
    dish=[dish1,dish2]
    height=0.3
    width=0.25
    number_of_dishes=4
    x=0
    y=0
    for i in range(3):
        y = i // 2
        x = i % 2
        dish[i].place(relx=0.5+x*width,rely=0.1+y*height,relwidth=width,relheight=height)


    waiting_Time_Button = Button(titlelabel,text="Waiting Time",command=lambda: show_waiting_time())
    waiting_Time_Button.place(relx=0.1,rely=0.15,relwidth=0.1,relheight=0.3)
    operating_Time_Button = Button(titlelabel,text="Operating Time", command=lambda: show_operating_time(stall_name))
    operating_Time_Button.place(relx=0.1, rely= 0.55,relwidth=0.1,relheight=0.3)
    def show_operating_time(stall):
        soti = Toplevel()
        soti.geometry("500x400")
        operatingtime = 0
        for i in opening_hours.keys():
            if i == stall:
                operatingtime = opening_hours[stall]["opening hours"]
                break
        timelabel=Label(soti,text=operatingtime)
        timelabel.place(relx=0, rely= 0,relwidth=1,relheight=0.5)
        okButton=Button(soti,text="Got it!",command=soti.destroy)
        okButton.place(relx=0, rely= 0.5,relwidth=1,relheight=0.5)
        soti.mainloop()






    m.mainloop()
