from tkinter import *
from tkinter.messagebox import showinfo
Window = Tk()
Window.title("W1")
Window.geometry("670x700")
Window["bg"] = "lightblue"

perem1a = IntVar()
perem2a = IntVar()
perem3a = IntVar()

prapor11 = IntVar()
prapor12 = IntVar()
prapor13 = IntVar()
prapor14 = IntVar()

prapor21 = IntVar()
prapor22 = IntVar()
prapor23 = IntVar()
prapor24 = IntVar()

perem11a = IntVar()

lbl10 = Label(Window, text="", fg="red", font="12")
btn1 = Button(Window, text="Count", font="12", width=10)
btn2 = Button(Window, text="Order", font="12", width=10,)

a = 0
b = 0
c = 0
d = 0
f = 0

prm11a = Radiobutton(Window, text="Solid Black, $1,500", variable=perem11a, value=1)
prm12a = Radiobutton(Window, text="Midnight Silver Mettalic, $1,500", variable=perem11a, value=2, fg="darkgrey")
prm13a = Radiobutton(Window, text="Deep Blue Mettalic, $1,500", variable=perem11a, value=3, fg="blue")
prm14a = Radiobutton(Window, text="Red Multi-Coat, $2,500", variable=perem11a, value=4, fg="red")

prap11 = Checkbutton(Window, text="Additional colors", variable=prapor11, onvalue=1, offvalue=0)
prap12 = Checkbutton(Window, text="", variable=prapor12, onvalue=1, offvalue=0)
prap13 = Checkbutton(Window, text="", variable=prapor13, onvalue=1, offvalue=0)
prap14 = Checkbutton(Window, text="Full Self-Driving, $12,000", variable=prapor14, onvalue=1, offvalue=0)

def select():
    global a
    global b
    global c
    global d
    a = 0
    b = 0
    c = 0
    d = 0
    prapor11.set(0)
    prapor12.set(0)
    prapor13.set(0)
    prapor14.set(0)
    perem11a.set(0)
    lbl2.place(x=50, y=95)

    if perem.get() == 3:
        lbl3.place_forget()
        prm11a.place_forget()
        prm12a.place_forget()
        prm13a.place_forget()
        prm14a.place_forget()
        lbl3["text"] = ""
        lbl2["text"] = "Model Y is an electric compact crossover. \nIt came in production in 2020. Powered by AWD Dual Motor. \nWell-known for ability to carry 7 passengers, including 2,2 cubic metres of their cargo."
        perem31 = Radiobutton(Window, text="Model Y Performance", variable=perem3a, value=1, bg="lightblue", fg="black", font="Times 12", command=select3)
        perem31.place(x=100, y=180)
        perem32=Radiobutton(Window, text="Model Y Long Range", variable=perem3a, value=2, bg="lightblue", fg="black", font="Times 12", command=select3)
        perem32.place(x=300, y=180)
        perem3a.set(0)
        prap11.configure(fg="black")
        prap12.configure(fg="black", text="Wheels \n20\" Induction Wheels, $2,000")
        prap13.configure(fg="black", text="Interior \nBlack and White, $1,000")
        prap14.configure(fg="black")
        prap11.place_forget()
        prap12.place_forget()
        prap13.place_forget()
        prap14.place_forget()
        lbl4.place_forget()
        lbl5.place_forget()
        lbl6.place_forget()
        lbl7.place_forget()
        lbl8.place_forget()
        lbl9.place_forget()

        lbl4.configure(fg="black")
        lbl5.configure(fg="black")
        lbl6.configure(fg="black")
        lbl7.configure(fg="black")
        lbl8.configure(fg="black")
        lbl9.configure(fg="black")

    if perem.get() == 1:
        lbl3.place_forget()
        prm11a.place_forget()
        prm12a.place_forget()
        prm13a.place_forget()
        prm14a.place_forget()
        lbl3["text"] = ""
        lbl2["text"] = "Model S is an electric liftback car. \nIt came in production in 2012. Specifically, Model S Plaid has the \nquickest acceleration of any vehicle in production. The lowest drag car on the planet." 
        perem11 = Radiobutton(Window, text="Model S", variable=perem1a, value=1, bg="lightblue", fg="red", font="Arial 12", width=25, command=select1)
        perem11.place(x=100, y=180)
        perem12 = Radiobutton(Window, text="Model S Plaid", variable=perem1a, value=2, bg="lightblue", fg="red", font="Arial 12", width=19, command=select1)
        perem12.place(x=300, y=180)
        perem1a.set(0)
        prap11.configure(fg="red")
        prap12.configure(fg="red", text="Wheels \n21\" Arachnid Wheels, $4,500")
        prap13.configure(fg="red", text="Interior \n     Cream, $2,000            ")
        prap14.configure(fg="red")
        prap11.place_forget()
        prap12.place_forget()
        prap13.place_forget()
        prap14.place_forget()
        lbl4.place_forget()
        lbl5.place_forget()
        lbl6.place_forget()
        lbl7.place_forget()
        lbl8.place_forget()
        lbl9.place_forget()
        lbl10.place_forget()        
        lbl4.configure(fg="red")
        lbl5.configure(fg="red")
        lbl6.configure(fg="red")
        lbl7.configure(fg="red")
        lbl8.configure(fg="red")
        lbl9.configure(fg="red") 

    if perem.get() == 2:
        lbl3.place_forget()
        prm11a.place_forget()
        prm12a.place_forget()
        prm13a.place_forget()
        prm14a.place_forget()
        lbl3["text"] = ""
        lbl2["text"] = "Model X is an elecric luxury full-sized (jeep) SUV. It can ride on/off-road. \nIt came in production in 2015. The vehicle is notable for its falcon-wing doors. \nHas 2,5 cubic metres of cargo space. The lowest drag SUV on Earth."
        perem21 = Radiobutton(Window, text="Model X", variable=perem2a, value=1, bg="lightblue", fg="blue", font="Calibri 12", width=25, command=select2)
        perem21.place(x=100, y=180)
        perem22 = Radiobutton(Window, text="Model X Plaid", variable=perem2a, value=2, bg="lightblue", fg="blue", font="Calibri 12", width=19, command=select2)
        perem22.place(x=300, y=180)
        perem2a.set(0)
        prap11.configure(fg="blue")
        prap12.configure(fg="blue", text="Wheels \n22\" Turbine Wheels, $5,500 ")
        prap13.configure(fg="blue", text="Interior \nBlack and White, $2,000")
        prap14.configure(fg="blue")
        prap11.place_forget()
        prap12.place_forget()        
        prap13.place_forget()
        prap14.place_forget()
        lbl4.place_forget()
        lbl5.place_forget()
        lbl6.place_forget()
        lbl7.place_forget()
        lbl8.place_forget()
        lbl9.place_forget()
        lbl10.place_forget()    
        lbl4.configure(fg="blue")
        lbl5.configure(fg="blue")
        lbl6.configure(fg="blue")
        lbl7.configure(fg="blue")
        lbl8.configure(fg="blue")
        lbl9.configure(fg="blue")

def select1():
    global f
    btn1.place(x=70, y=635)
    lbl3.place(x=280, y=220)
    prap11.place(x=60, y=220)
    prap12.place(x=450, y=380)
    prap13.place(x=60, y=380)
    prap14.place(x=260, y=380)
    lbl4.place(x=260, y=410)
    lbl5.place(x=260, y=440)
    lbl6.place(x=260, y=470)
    lbl7.place(x=260, y=500)
    lbl8.place(x=260, y=530)
    lbl9.place(x=260, y=560)
    def prap11a():
        if prapor11.get() == 1:
            prm11a.place(x=60, y=250)
            prm12a.place(x=60, y=280)
            prm13a.place(x=60, y=310)
            prm14a.place(x=60, y=340)

        if prapor11.get() == 0:         
            perem11a.set(0)
            prm11a.place_forget()
            prm12a.place_forget()
            prm13a.place_forget()
            prm14a.place_forget()

        def update_c():
            c = 0
            if prapor11.get() == 1:
                if perem11a.get() == 1 or perem11a.get() == 2 or perem11a.get() == 3:
                    c += 1500
                if perem11a.get() == 4:
                    c += 2500      
            return c

        def on_change(*args):
            global c
            c = update_c()

        perem11a.trace_add("write", on_change)

    def prap12a():
        global b
        if prapor12.get() == 1:
            b = 0
            b += 4500
        if prapor12.get() == 0:
            b = 0   
                
    def prap13a():
        global a
        if prapor13.get() == 1:
            a = 0
            a += 2000
        if prapor13.get() == 0:
            a = 0
            
            
    def prap14a():
        global d      
        if prapor14.get() == 1:
            d = 0
            d += 12000
        if prapor14.get() == 0:
            d = 0

    prap11.configure(fg="red", command=prap11a)
    prap12.configure(fg="red", command=prap12a)
    prap13.configure(fg="red", command=prap13a)
    prap14.configure(fg="red", command=prap14a)
         
    if perem1a.get() == 1:
        f = 0
        f += 96840
        lbl3["text"] = "Price: $96,840. \nRange: 650 km. \nSeating up to 5 seats. \nTop speed: 250 km/h. \nAcceleration 0-100 km/h: 3.1 sec. \nA default color: Pearl White Multi-Coat (included in the cost). \nDefault wheels: 19\" Tempest Wheels (included in the cost). \nInitial interior is All Black (included in the cost)."
    if perem1a.get() == 2:
        f = 0
        f += 132560
        lbl3["text"] = "Price: $132,560. \nRange: 640 km. \nSeating up to 5 seats. \nTop speed: 320 km/h. \nAcceleration 0-100 km/h: 1.99 sec. \nA default color: Pearl White Multi-Coat (included in the cost). \nDefault wheels: 19\" Tempest Wheels (included in the cost). \nInitial interior is All Black (included in the cost)."

    def change1(event):
        lbl10["text"] = "Total price: $" + str(a + b + c + d + f)
        lbl10.place(x=250, y=640)
        btn2.place(x=490, y=635)
    btn1.bind("<Button-1>", change1)    

def select2():
    global f
    btn1.place(x=70, y=635)
    lbl3.place(x=280, y=220)
    prap11.place(x=60, y=220)
    prap12.place(x=450, y=380)
    prap13.place(x=60, y=380)
    prap14.place(x=260, y=380)
    lbl4.place(x=260, y=410)
    lbl5.place(x=260, y=440)
    lbl6.place(x=260, y=470)
    lbl7.place(x=260, y=500)
    lbl8.place(x=260, y=530)
    lbl9.place(x=260, y=560)
    def prap11a():
        if prapor11.get() == 1:
            prm11a.place(x=60, y=250)
            prm12a.place(x=60, y=280)
            prm13a.place(x=60, y=310)
            prm14a.place(x=60, y=340)

        if prapor11.get() == 0:         
            perem11a.set(0)
            prm11a.place_forget()
            prm12a.place_forget()
            prm13a.place_forget()
            prm14a.place_forget()

        def update_c():
            c = 0
            if prapor11.get() == 1:
                if perem11a.get() == 1 or perem11a.get() == 2 or perem11a.get() == 3:
                    c += 1500
                if perem11a.get() == 4:
                    c += 2500      
            return c

        def on_change(*args):
            global c
            c = update_c()

        perem11a.trace_add("write", on_change)

    def prap12a():
        global b
        if prapor12.get() == 1:
            b = 0
            b += 5500
        if prapor12.get() == 0:
            b = 0

    def prap13a():
        global a
        if prapor13.get() == 1:
            a = 0
            a += 2000
        if prapor13.get() == 0:
            a = 0
                    
    def prap14a():
        global d     
        if prapor14.get() == 1:
            d = 0
            d += 12000
        if prapor14.get() == 0:
            d = 0     

    prap11.configure(fg="blue", command=prap11a)
    prap12.configure(fg="blue", command=prap12a)
    prap13.configure(fg="blue", command=prap13a)
    prap14.configure(fg="blue", command=prap14a)    
        
    if perem2a.get() == 1:
        f = 0
        f += 111990
        lbl3["text"] = "Price: $111,990. \nRange: 560 km. \nSeating up to 7 seats. \nTop speed: 240 km/h. \nAcceleration 0-100 km/h: 3.8 sec. \nA default color: Pearl White Multi-Coat (included in the cost). \nDefault wheels: 20\" Cyberstream Wheels (included in the cost). \nInitial interior is All Black (included in the cost)."
    if perem2a.get() == 2:
        f = 0
        f += 135990
        lbl3["text"] = "Price: $135,990. \nRange: 540 km. \nSeating up to 6 seats. \nTop speed: 240 km/h. \nAcceleration 0-100 km/h: 2.5 sec. \nA default color: Pearl White Multi-Coat (included in the cost). \nDefault wheels: 20\" Cyberstream Wheels (included in the cost). \nInitial interior is All Black (included in the cost)."
        
    def change1(event):
        lbl10["text"] = "Total price: $" + str(a + b + c + d + f)
        lbl10.place(x=250, y=640)
        btn2.place(x=490, y=635)
    btn1.bind("<Button-1>", change1)

def select3():
    global f
    btn1.place(x=70, y=635)
    lbl3.place(x=280, y=220)
    prap11.place(x=60, y=220)
    prap12.place(x=450, y=380)
    prap13.place(x=60, y=380)
    prap14.place(x=260, y=380)
    lbl4.place(x=260, y=410)
    lbl5.place(x=260, y=440)
    lbl6.place(x=260, y=470)
    lbl7.place(x=260, y=500)
    lbl8.place(x=260, y=530)
    lbl9.place(x=260, y=560)
    def prap11a():
        if prapor11.get() == 1:
            prm11a.place(x=60, y=250)
            prm13a.place(x=60, y=280)
            prm14a.place(x=60, y=310)

        if prapor11.get() == 0:         
            perem11a.set(0)
            prm11a.place_forget()
            prm13a.place_forget()
            prm14a.place_forget()

        def update_c():
            c = 0
            if prapor11.get() == 1:
                if perem11a.get() == 1 or perem11a.get() == 3:
                    c += 1500
                if perem11a.get() == 4:
                    c += 2500      
            return c

        def on_change(*args):
            global c
            c = update_c()

        perem11a.trace_add("write", on_change)

    def prap12a():
        global b
        if prapor12.get() == 1:
            b = 0
            b += 2000
        if prapor12.get() == 0:
            b = 0

    def prap13a():
        global a
        if prapor13.get() == 1:
            a = 0
            a += 1000
        if prapor13.get() == 0:
            a = 0
                        
    def prap14a():
        global d
        if prapor14.get() == 1:
            d = 0
            d += 12000
        if prapor14.get() == 0:
            d = 0 

    prap11.configure(fg="black", command=prap11a)
    prap12.configure(fg="black", command=prap12a)
    prap13.configure(fg="black", command=prap13a)
    prap14.configure(fg="black", command=prap14a)

    if perem3a.get() == 1:
        f = 0
        f += 65590
        lbl3["text"] = "Price: $65,590.\nRange: 490 km.\nSeating up to 5 seats. \nTop speed: 250 km/h. \nAcceleration 0-100 km/h: 3.5 sec. \nA default color: Pearl White Multi-Coat (included in the cost). \nDefault wheels: 19\" Gemini Wheels (included in the cost). \nInitial interior is All Black (included in the cost)."
    if perem3a.get() == 2:
        f = 0
        f += 60990
        lbl3["text"] = "Price: $60,990. \nRange: 530 km. \nSeating up to 7 seats. \nTop speed: 220 km/h. \nAcceleration 0-100 km/h: 4.8 sec. \nA default color: Pearl White Multi-Coat (included in the cost). \nDefault wheels: 19\" Gemini Wheels (included in the cost). \nInitial interior is All Black (included in the cost)."

    def change1(event):
        lbl10["text"] = "Total price: $" + str(a + b + c + d + f)
        lbl10.place(x=250, y=640)
        btn2.place(x=490, y=635)
    btn1.bind("<Button-1>", change1)

def change2(event):
    s = showinfo("Order", "Payment succesful. Your car's arrival date is going to be told soon.", parent=Window)
btn2.bind("<Button-1>", change2)

lbl4 = Label(Window, text="- Navigate on Autopilot", bg="white")
lbl5 = Label(Window, text="- Auto Lane Change", bg="white")
lbl6 = Label(Window, text="- Autopark", bg="white")
lbl7 = Label(Window, text="- Summon", bg="white")
lbl8 = Label(Window, text="- Full Self-Driving Computer", bg="white")
lbl9 = Label(Window, text="- Traffic Light and Stop Sign Control", bg="white")
lbl3 = Label(Window, text=" ", bg="white")
lbl1 = Label(Window, text="Choose a car", bg="lightblue", fg="green", font="11")
lbl1.place(x=240, y=10)
lbl2 = Label(Window, text="", bg="white", fg="black", font="Times 12")
perem=IntVar()
perem1 = Radiobutton(Window, text="Tesla Model S", variable=perem, value=1, bg="lightblue", fg="red", font="Arial 12", command=select)
perem1.place(x=70, y=50)
perem2=Radiobutton(Window, text="Tesla Model X", variable=perem, value=2, bg="lightblue", fg="blue", font="Calibri 12", command=select)
perem2.place(x=260, y=50)
perem3=Radiobutton(Window, text="Tesla Model Y", variable=perem, value=3, bg="lightblue", fg="black", font="Times 12", command=select)
perem3.place(x=450, y=50)
#розмір перемикачів залишив таким же, щоб було красиво

Window.mainloop()