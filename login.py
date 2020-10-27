from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql
import tkinter.messagebox
import random
import time
import datetime


def main():
    root=Tk()
    app = register(root)
    root.mainloop()

class register:
    def __init__(self,root):
        self.root=root
        self.root.title("Train Ticketing System")
        self.root.geometry('1350x700+250+100')
        self.root.config(bg="white")
        self.root.resizable(False,False)
        #------image bg---------
        self.bg=ImageTk.PhotoImage(file="backg.jpg")
        bg=Label(self.root,image=self.bg).place(relwidth=1,relheight=1)
        #-------image----------
        self.left=ImageTk.PhotoImage(file="indian.jpg")
        left=Label(self.root,image=self.left).place(x=100,y=100,width=400,height=500)
        #---------frame--------
        frame1=Frame(self.root,bg="white")
        frame1.place(x=500,y=100,width=700,height=500)

        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)
        title2=Label(self.root,text="Train Ticketing System",font=("times new roman",20,"bold"),bg="lightgrey",fg="blue").place(x=150,y=110)
        title3=Label(self.root,text="Already Registered ? Then Sign In :)",font=("times new roman",13),bg="yellow",fg="purple").place(x=150,y=460)


        f_name=Label(frame1,text="First Name",font=("times new roman",13,"bold"),bg="white",fg="grey").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",13),bg="lightgrey")
        self.txt_fname.place(x=50,y=130,width=250)

        l_name = Label(frame1, text="Last Name", font=("times new roman", 13, "bold"), bg="white", fg="grey").place(
            x=370, y=100)
        self.txt_lname = Entry(frame1, font=("times new roman", 13), bg="lightgrey")
        self.txt_lname.place(x=370, y=130, width=250)

        contact = Label(frame1, text="Contact No", font=("times new roman", 13, "bold"), bg="white", fg="grey").place(
            x=50, y=170)
        self.txt_contact = Entry(frame1, font=("times new roman", 13), bg="lightgrey")
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame1, text="Email", font=("times new roman", 13, "bold"), bg="white", fg="grey").place(
            x=370, y=170)
        self.txt_email = Entry(frame1, font=("times new roman", 13), bg="lightgrey")
        self.txt_email.place(x=370, y=200, width=250)

        security = Label(frame1, text="Security Question", font=("times new roman", 13, "bold"), bg="white", fg="grey").place(
            x=50, y=240)
        self.cmb_box = ttk.Combobox(frame1, font=("times new roman", 13),state="readonly",justify=CENTER)
        self.cmb_box['values']=('Select','Your Nickname','Your birth place','Your first Pet name','Your first school name','Your best friend name')
        self.cmb_box.place(x=50, y=270, width=250)
        self.cmb_box.current(0)

        answer = Label(frame1, text="Answer", font=("times new roman", 13, "bold"), bg="white", fg="grey").place(
            x=370, y=240)
        self.txt_answer = Entry(frame1, font=("times new roman", 13), bg="lightgrey")
        self.txt_answer.place(x=370, y=270, width=250)

        password = Label(frame1, text="Password", font=("times new roman", 13, "bold"), bg="white", fg="grey").place(
            x=50, y=310)
        self.txt_password = Entry(frame1, font=("times new roman", 13), bg="lightgrey",show="*")
        self.txt_password.place(x=50, y=340, width=250)

        cnf_password = Label(frame1, text="Confirm Password", font=("times new roman", 13, "bold"), bg="white", fg="grey").place(
            x=370, y=310)
        self.txt_cnfpassword = Entry(frame1, font=("times new roman", 13), bg="lightgrey",show="*")
        self.txt_cnfpassword.place(x=370, y=340, width=250)

        #------------terms--------------------
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I agree with the terms & conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=('times new roman',12)).place(x=50,y=380)

        btn_register=Button(frame1,text="Register Now",font=("times new roman",13,"bold"),bg="green",fg="white",cursor="hand2",command=self.register_data).place(x=50,y=420,width=200)
        btn_signin = Button(self.root, text="Sign In", font=("times new roman", 13, "bold"), bg="orange", fg="black",cursor="hand2",command=self.new_win).place(
            x=210, y=500,width=200)
    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cnfpassword.delete(0,END)
        self.cmb_box.current(0)
    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_box.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cnfpassword.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        elif self.txt_password.get() != self.txt_cnfpassword.get():
            messagebox.showerror("Error","Password & Confirm Password should be same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please agree to our terms and conditions.",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="train")
                curs=con.cursor()
                curs.execute("select * from registration where email=%s", self.txt_email.get())
                row=curs.fetchone()
                print(row)
                if row!=None:
                    messagebox.showerror("Error","User already exist please try with another email",parent=self.root)
                else:
                    curs.execute("insert into registration (f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",(self.txt_fname.get(),self.txt_lname.get(),self.txt_contact.get(),self.txt_email.get(),self.cmb_box.get(),self.txt_answer.get(),self.txt_password.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Register Successful",parent=self.root)
                    self.clear()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: { str(es)}",parent=self.root)
    def new_win(self):
        self.root.destroy()
        self.newwindow=Tk()
        self.app = login(self.newwindow)


class login(register):

    def register_win(self):
            self.root.destroy()
            self.prevwindow = Tk()
            self.app = register(self.prevwindow)

    def train_win(self):
            self.root.destroy()
            self.train_window = Tk()
            self.app = Train(self.train_window)

    def login_fun(self):
        if self.txt_useremail.get()=="" or self.txt_userpassword.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="train")
                curs=con.cursor()
                curs.execute("select * from registration where email=%s and password=%s",(self.txt_useremail.get(),self.txt_userpassword.get()))
                row=curs.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Email Address or Password!",parent=self.root)
                else:
                    #messagebox.showinfo("welcome","successful")
                    self.train_win()
                con.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)

    def __init__(self,root):
        self.root=root
        self.root.title("Train Ticketing System")
        self.root.geometry('1500x700+180+100')
        self.root.config(bg="black")
        self.root.resizable(False,False)
        #-------image----------
        self.left=ImageTk.PhotoImage(file="loginimg.png")
        left=Label(self.root,image=self.left).place(x=100,y=100,width=540,height=580)
        #-------frame---------
        frame1 = Frame(self.root, bg="light goldenrod")
        frame1.place(x=630,y=100,width=700,height=580)
        title1 = Label(self.root, text="TRAIN  TICKETING  SYSTEM", font=("times new roman", 30, "bold"), bg="lightgreen", fg="green",justify=CENTER).place(
            x=370, y=15,width=800)

        title=Label(frame1,text="LOGIN HERE",font=("times new roman",28,"bold"),bg="white",fg="#08A3D2").place(x=44,y=40,width=600)

        useremail = Label(frame1, text="EMAIL  ADDRESS", font=("Book Antiqua", 15, "bold"),bg="light goldenrod",fg="black").place(x=44, y=170)
        self.txt_useremail=Entry(frame1,font=("times new roman",13),bg="lightgrey")
        self.txt_useremail.place(x=50,y=220,width=400,height=40)

        userpassword = Label(frame1, text="PASSWORD", font=("Book Antiqua", 15, "bold"),bg="light goldenrod",fg="black").place(x=44, y=320)
        self.txt_userpassword = Entry(frame1, font=("times new roman", 13), bg="lightgrey",show="*")
        self.txt_userpassword.place(x=50, y=370, width=400, height=40)

        new_acc = Button(frame1, text="Register new Account?", font=("Book Antiqua", 15, "bold"), bg="light goldenrod",
                          fg="black",borderwidth=0,cursor="hand2",command=self.register_win).place(x=44, y=430)

        btn_login = Button(frame1, text="LOGIN", font=("times new roman", 13, "bold"), bg="orange", fg="black",
                            cursor="hand2",command=self.login_fun).place(x=230, y=500,width=200)



class Train:
    def pay_win(self):
            self.root.destroy()
            self.pay_window = Tk()
            self.app = payment(self.pay_window)

    def __init__(self,root):
        self.root=root
        self.root.title=("Train Ticketing System")
        self.root.geometry("1920x1080+0+0")
        # width = self.root.winfo_screenwidth()
        # height = self.root.winfo_screenheight()
        # print(f"{width}x{height}")
        self.root.configure(background="gainsboro")

        Mainframe=Frame(self.root,bd=10,width=1350,height=1350,bg="black",relief=RIDGE)
        Mainframe.pack(fill=Y,expand=YES)

        Topframe1 = Frame(Mainframe, bd=10, width=1340, height=100, bg="gainsboro", relief=RIDGE)
        Topframe1.grid()
        Topframe2 = Frame(Mainframe, bd=10, width=1300, height=500, bg="gainsboro", relief=RIDGE)
        Topframe2.grid()

        F1 = Frame(Topframe2, bd=5, width=890, height=500, relief=RIDGE)
        F1.grid(row=1,column=0)
        F2 = Frame(Topframe2, bd=5, width=400, height=100,pady=2, relief=RIDGE)
        F2.grid(row=1, column=1)

        Frametopright = Frame(F2, bd=5, width=404, height=420, relief=RIDGE)
        Frametopright.pack(side=TOP)
        Framebottomright = Frame(F2, bd=5, width=408, height=100,pady=15, relief=RIDGE)
        Framebottomright.pack(side=BOTTOM)
        f1a = Frame(F1, bd=5, width=900, height=330, relief=RIDGE)
        f1a.pack(side=TOP)
        f2a = Frame(F1, bd=5, width=900, height=330, relief=RIDGE)
        f2a.pack(side=BOTTOM)

        topleft1 = Frame(f1a, bd=5, width=300, height=200,padx=20,pady=1, relief=RIDGE)
        topleft1.pack(side=LEFT)
        topleft2 = Frame(f1a, bd=5, width=300, height=200, relief=RIDGE)
        topleft2.pack(side=RIGHT)
        topleft3 = Frame(f1a, bd=5, width=300, height=200, pady=5, relief=RIDGE)
        topleft3.pack(side=RIGHT)

        bottomleft1 = Frame(f2a, bd=5, width=450, height=300, pady=12, relief=RIDGE)
        bottomleft1.pack(side=LEFT)
        bottomleft2 = Frame(f2a, bd=5, width=450, height=300, relief=RIDGE)
        bottomleft2.pack(side=RIGHT)

        #-----------------------------------------------------------------------------------------------
        Title= Label(Topframe1,font=('arial',40,'bold'),text="Train Ticketing System",bd=5,width=41,padx=4,justify="center",bg="dark slate gray",fg="white")
        Title.grid(row=0,column=0)
        pay = Label(self.root, font=('times new roman', 20, 'bold'), text="Do you want to proceed for the payment?", bd=5, width=45, padx=4,
                      justify="center", bg="white", fg="blue")
        pay.place(x=300,y=800)
        pay_btn=Button(self.root,font=('times new roman', 17, 'bold'),text="PAY NOW",cursor="hand2",bg="green",fg="white",command=self.pay_win)
        pay_btn.place(x=1300,y=800,width=250)
        #===============================================================================================
        Date1 = StringVar()
        Time1 = StringVar()
        Ticketclass = StringVar()
        Ticketprice = StringVar()
        Child_ticket = StringVar()
        Adult_ticket= StringVar()
        From_destination=StringVar()
        To_destination=StringVar()
        Fee_price=StringVar()
        Route=StringVar()
        Receipt_ref=StringVar()

        text_input=StringVar()
        global operator
        operator=""
        Ticketclass.set("")
        Ticketprice.set("")
        Child_ticket.set("")
        Adult_ticket.set("")
        From_destination.set("")
        To_destination.set("")
        Fee_price.set("")
        Route.set("")
        Receipt_ref.set("")

        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()
        var6 = StringVar()
        var7 = StringVar()
        var8 = StringVar()
        var9 = StringVar()
        var10 = IntVar()
        var11 = IntVar()
        var12 = IntVar()

        Tax = StringVar()
        Subtotal = StringVar()
        Total = StringVar()

        var1.set("0")
        var2.set("0")
        var3.set("0")
        var4.set("0")
        var5.set("0")
        var6.set("0")
        var7.set("0")
        var8.set("0")
        var9.set("0")
        var10.set("0")
        var11.set("0")
        var12.set("0")
        #-------------------------------------------------------------------------------------------------------
        def iExit():
            iExit=tkinter.messagebox.askyesno("Train Ticketing System","Confirm if you want to quit")
            if iExit>0:
                root.destroy()
                return
        def Reset():
            var1.set("0")
            var2.set("0")
            var3.set("0")
            var4.set("0")
            var5.set("0")
            var6.set("0")
            var7.set("0")
            var8.set("0")
            var9.set("0")
            var10.set("0")
            var11.set("0")
            var12.set("0")
            Tax.set("0")
            Subtotal.set("0")
            Total.set("0")
            Ticketclass.set("")
            Ticketprice.set("")
            Child_ticket.set("")
            Adult_ticket.set("")
            From_destination.set("")
            To_destination.set("")
            Fee_price.set("")
            Route.set("")
            Receipt_ref.set("")

        def btnClick(number):
            global operator
            operator = operator + str(number)
            text_input.set(operator)

        def btnClearDisplay():
            global operator
            operator = ""
            text_input.set("")

        def btnequalsinput():
            global operator
            sumup = str(eval(operator))
            text_input.set(sumup)
            operator=""
        def travelcost():
            if (var9.get() == "New Delhi" and var1.get() == 1 and var4.get()==1):
                tcost=float(1030)
                single=float(var12.get())
                adult_tax="Rs",str((tcost*single) * 0.9)
                adult_fees="Rs",str(tcost*single)
                total_cost="Rs",str((tcost*single) + ((tcost*single) * 0.9 ))
                Tax.set(adult_tax)
                Subtotal.set(adult_fees)
                Ticketclass.set("First")
                Ticketprice.set(adult_fees)
                Child_ticket.set("No")
                Adult_ticket.set("Yes")
                From_destination.set("Kanpur")
                To_destination.set("New Delhi")
                Fee_price.set(total_cost)
                Total.set(total_cost)
                Route.set("Direct")

                x=random.randint(10900,50980)
                randomRef= str(x)
                Receipt_ref.set("IR"+randomRef)
            elif (var9.get() == "New Delhi" and var1.get() == 1 and var5.get()==1):
                tcost=float(930)
                single=float(var12.get())
                adult_tax="Rs",str(tcost*single* 0.9 )
                adult_fees="Rs",str(tcost*single)
                total_cost="Rs",str((tcost*single) + ((tcost*single) * 0.9 ))
                Tax.set(adult_tax)
                Subtotal.set(adult_fees)
                Ticketclass.set("First")
                Ticketprice.set(adult_fees)
                Child_ticket.set("Yes")
                Adult_ticket.set("No")
                From_destination.set("Kanpur")
                To_destination.set("New Delhi")
                Fee_price.set(total_cost)
                Total.set(total_cost)
                Route.set("Direct")

                x=random.randint(10900,50980)
                randomRef= str(x)
                Receipt_ref.set("IR"+randomRef)

            elif (var9.get() == "Varanasi" and var1.get() == 1 and var4.get()==1):
                tcost=float(600)
                single=float(var12.get())
                adult_tax="Rs",str(tcost*single * 0.9 )
                adult_fees="Rs",str(tcost*single)
                total_cost="Rs",str((tcost*single) + ((tcost*single) * 0.9 ))
                Tax.set(adult_tax)
                Subtotal.set(adult_fees)
                Total.set(total_cost)
                Ticketclass.set("First")
                Ticketprice.set(adult_fees)
                Child_ticket.set("No")
                Adult_ticket.set("Yes")
                From_destination.set("Kanpur")
                To_destination.set("Varanasi")
                Fee_price.set(total_cost)
                Route.set("Direct")

                x=random.randint(10900,50980)
                randomRef= str(x)
                Receipt_ref.set("IR"+randomRef)
            elif (var9.get() == "Varanasi" and var1.get() == 1 and var5.get() == 1):
                tcost = float(344)
                single = float(var12.get())
                adult_tax = "Rs", str(tcost * single * 0.9)
                adult_fees = "Rs", str(tcost * single)
                total_cost = "Rs", str((tcost * single) + ((tcost * single) * 0.9))
                Tax.set(adult_tax)
                Subtotal.set(adult_fees)
                Total.set(total_cost)
                Ticketclass.set("First")
                Ticketprice.set(adult_fees)
                Child_ticket.set("Yes")
                Adult_ticket.set("No")
                From_destination.set("Kanpur")
                To_destination.set("Varanasi")
                Fee_price.set(total_cost)
                Route.set("Direct")

                x = random.randint(10900, 50980)
                randomRef = str(x)
                Receipt_ref.set("IR" + randomRef)
            elif (var9.get() == "Etawah" and var1.get() == 1 and var4.get() == 1):
                tcost = float(409)
                single = float(var12.get())
                adult_tax = "Rs", str(tcost * single * 0.9)
                adult_fees = "Rs", str(tcost * single)
                total_cost = "Rs", str((tcost * single) + ((tcost * single) * 0.9))
                Tax.set(adult_tax)
                Subtotal.set(adult_fees)
                Total.set(total_cost)
                Ticketclass.set("First")
                Ticketprice.set(adult_fees)
                Child_ticket.set("No")
                Adult_ticket.set("Yes")
                From_destination.set("Kanpur")
                To_destination.set("Etawah")
                Fee_price.set(total_cost)
                Route.set("Direct")

                x = random.randint(10900, 50980)
                randomRef = str(x)
                Receipt_ref.set("IR" + randomRef)
            elif (var9.get() == "Etawah" and var1.get() == 1 and var5.get() == 1):
                tcost = float(409)
                single = float(var12.get())
                adult_tax = "Rs", str(tcost * single * 0.9)
                adult_fees = "Rs", str(tcost * single)
                total_cost = "Rs", str((tcost * single) + ((tcost * single) * 0.9))
                Tax.set(adult_tax)
                Subtotal.set(adult_fees)
                Total.set(total_cost)
                Ticketclass.set("First")
                Ticketprice.set(adult_fees)
                Child_ticket.set("Yes")
                Adult_ticket.set("No")
                From_destination.set("Kanpur")
                To_destination.set("Etawah")
                Fee_price.set(total_cost)
                Route.set("Direct")

                x = random.randint(10900, 50980)
                randomRef = str(x)
                Receipt_ref.set("IR" + randomRef)
            elif (var9.get() == "Gurugram" and var1.get() == 1 and var4.get() == 1):
                tcost = float(409)
                single = float(var12.get())
                adult_tax = "Rs", str(tcost * single * 0.9)
                adult_fees = "Rs", str(tcost * single)
                total_cost = "Rs", str((tcost * single) + ((tcost * single) * 0.9))
                Tax.set(adult_tax)
                Subtotal.set(adult_fees)
                Total.set(total_cost)
                Ticketclass.set("First")
                Ticketprice.set(adult_fees)
                Child_ticket.set("No")
                Adult_ticket.set("Yes")
                From_destination.set("Kanpur")
                To_destination.set("Gurugram")
                Fee_price.set(total_cost)
                Route.set("Direct")

                x = random.randint(10900, 50980)
                randomRef = str(x)
                Receipt_ref.set("IR" + randomRef)
            elif (var9.get() == "Gurugram" and var1.get() == 1 and var5.get() == 1):
                tcost = float(409)
                single = float(var12.get())
                adult_tax = "Rs", str(tcost * single * 0.9)
                adult_fees = "Rs", str(tcost * single)
                total_cost = "Rs", str((tcost * single) + ((tcost * single) * 0.9))
                Tax.set(adult_tax)
                Subtotal.set(adult_fees)
                Total.set(total_cost)
                Ticketclass.set("First")
                Ticketprice.set(adult_fees)
                Child_ticket.set("Yes")
                Adult_ticket.set("No")
                From_destination.set("Kanpur")
                To_destination.set("Gurugram")
                Fee_price.set(total_cost)
                Route.set("Direct")

                x = random.randint(10900, 50980)
                randomRef = str(x)
                Receipt_ref.set("IR" + randomRef)
            elif (var9.get() == "Ludhiana" and var1.get() == 1 and var4.get() == 1):
                tcost = float(2900)
                single = float(var12.get())
                adult_tax = "Rs", str(tcost * single * 0.9)
                adult_fees = "Rs", str(tcost * single)
                total_cost = "Rs", str((tcost * single) + ((tcost * single) * 0.9))
                Tax.set(adult_tax)
                Subtotal.set(adult_fees)
                Total.set(total_cost)
                Ticketclass.set("First")
                Ticketprice.set(adult_fees)
                Child_ticket.set("No")
                Adult_ticket.set("Yes")
                From_destination.set("Kanpur")
                To_destination.set("Ludhiana")
                Fee_price.set(total_cost)
                Route.set("Direct")

                x = random.randint(10900, 50980)
                randomRef = str(x)
                Receipt_ref.set("IR" + randomRef)
            elif (var9.get() == "Ludhiana" and var1.get() == 1 and var5.get() == 1):
                tcost = float(409)
                single = float(var12.get())
                adult_tax = "Rs", str(tcost * single* 0.9)
                adult_fees = "Rs", str(tcost * single)
                total_cost = "Rs", str((tcost * single) + ((tcost * single) * 0.9))
                Tax.set(adult_tax)
                Subtotal.set(adult_fees)
                Total.set(total_cost)
                Ticketclass.set("First")
                Ticketprice.set(adult_fees)
                Child_ticket.set("Yes")
                Adult_ticket.set("No")
                From_destination.set("Kanpur")
                To_destination.set("Ludhiana")
                Fee_price.set(total_cost)
                Route.set("Direct")

                x = random.randint(10900, 50980)
                randomRef = str(x)
                Receipt_ref.set("IR" + randomRef)
            elif (var9.get() == "Ambala" and var1.get() == 1 and var4.get() == 1):
                tcost = float(2409)
                single = float(var12.get())
                adult_tax = "Rs", str(tcost * single * 0.9)
                adult_fees = "Rs", str(tcost * single)
                total_cost = "Rs", str((tcost * single) + ((tcost * single) * 0.9))
                Tax.set(adult_tax)
                Subtotal.set(adult_fees)
                Total.set(total_cost)
                Ticketclass.set("First")
                Ticketprice.set(adult_fees)
                Child_ticket.set("No")
                Adult_ticket.set("Yes")
                From_destination.set("Kanpur")
                To_destination.set("Ambala")
                Fee_price.set(total_cost)
                Route.set("Direct")

                x = random.randint(10900, 50980)
                randomRef = str(x)
                Receipt_ref.set("IR" + randomRef)
            elif (var9.get() == "Ambala" and var1.get() == 1 and var5.get() == 1):
                tcost = float(1899)
                single = float(var12.get())
                adult_tax = "Rs", str(tcost * single* 0.9)
                adult_fees = "Rs", str(tcost * single)
                total_cost = "Rs", str((tcost * single) + ((tcost * single) * 0.9))
                Tax.set(adult_tax)
                Subtotal.set(adult_fees)
                Total.set(total_cost)
                Ticketclass.set("First")
                Ticketprice.set(adult_fees)
                Child_ticket.set("Yes")
                Adult_ticket.set("No")
                From_destination.set("Kanpur")
                To_destination.set("Ambala")
                Fee_price.set(total_cost)
                Route.set("Direct")

                x = random.randint(10900, 50980)
                randomRef = str(x)
                Receipt_ref.set("IR" + randomRef)



            elif (var9.get() == "New Delhi" and var2.get() == 1 and var4.get() == 1):
                tcost = float(830)
                single = float(var12.get())
                adult_tax = "Rs", str(tcost * single * 0.9)
                adult_fees = "Rs", str(tcost * single)
                total_cost = "Rs", str((tcost * single) + ((tcost * single) * 0.9))
                Tax.set(adult_tax)
                Subtotal.set(adult_fees)
                Ticketclass.set("Second")
                Ticketprice.set(adult_fees)
                Child_ticket.set("No")
                Adult_ticket.set("Yes")
                From_destination.set("Kanpur")
                To_destination.set("New Delhi")
                Fee_price.set(total_cost)
                Total.set(total_cost)
                Route.set("Direct")

                x = random.randint(10900, 50980)
                randomRef = str(x)
                Receipt_ref.set("IR" + randomRef)
            elif (var9.get() == "New Delhi" and var2.get() == 1 and var5.get() == 1):
                tcost = float(789)
                single = float(var12.get())
                adult_tax = "Rs", str(tcost * single* 0.9)
                adult_fees = "Rs", str(tcost * single)
                total_cost = "Rs", str((tcost * single) + ((tcost * single) * 0.9))
                Tax.set(adult_tax)
                Subtotal.set(adult_fees)
                Ticketclass.set("Second")
                Ticketprice.set(adult_fees)
                Child_ticket.set("Yes")
                Adult_ticket.set("No")
                From_destination.set("Kanpur")
                To_destination.set("New Delhi")
                Fee_price.set(total_cost)
                Total.set(total_cost)
                Route.set("Direct")

                x = random.randint(10900, 50980)
                randomRef = str(x)
                Receipt_ref.set("IR" + randomRef)

            elif (var9.get() == "Varanasi" and var2.get() == 1 and var4.get() == 1):
                tcost = float(344)
                single = float(var12.get())
                adult_tax = "Rs", str(tcost * single * 0.9)
                adult_fees = "Rs", str(tcost * single)
                total_cost = "Rs", str((tcost * single) + ((tcost * single) * 0.9))
                Tax.set(adult_tax)
                Subtotal.set(adult_fees)
                Total.set(total_cost)
                Ticketclass.set("Second")
                Ticketprice.set(adult_fees)
                Child_ticket.set("No")
                Adult_ticket.set("Yes")
                From_destination.set("Kanpur")
                To_destination.set("Varanasi")
                Fee_price.set(total_cost)
                Route.set("Direct")

                x = random.randint(10900, 50980)
                randomRef = str(x)
                Receipt_ref.set("IR" + randomRef)
            elif (var9.get() == "Varanasi" and var2.get() == 1 and var5.get() == 1):
                tcost = float(309)
                single = float(var12.get())
                adult_tax = "Rs", str(tcost * single * 0.9)
                adult_fees = "Rs", str(tcost * single)
                total_cost = "Rs", str((tcost * single) + ((tcost * single) * 0.9))
                Tax.set(adult_tax)
                Subtotal.set(adult_fees)
                Total.set(total_cost)
                Ticketclass.set("General")
                Ticketprice.set(adult_fees)
                Child_ticket.set("Yes")
                Adult_ticket.set("No")
                From_destination.set("Kanpur")
                To_destination.set("Varanasi")
                Fee_price.set(total_cost)
                Route.set("Direct")

                x = random.randint(10900, 50980)
                randomRef = str(x)
                Receipt_ref.set("IR" + randomRef)
            elif (var9.get() == "Etawah" and var2.get() == 1 and var4.get() == 1):
                tcost = float(299)
                single = float(var12.get())
                adult_tax = "Rs", str(tcost * single* 0.9)
                adult_fees = "Rs", str(tcost * single)
                total_cost = "Rs", str((tcost * single) + ((tcost * single) * 0.9))
                Tax.set(adult_tax)
                Subtotal.set(adult_fees)
                Total.set(total_cost)
                Ticketclass.set("Second")
                Ticketprice.set(adult_fees)
                Child_ticket.set("No")
                Adult_ticket.set("Yes")
                From_destination.set("Kanpur")
                To_destination.set("Etawah")
                Fee_price.set(total_cost)
                Route.set("Direct")

                x = random.randint(10900, 50980)
                randomRef = str(x)
                Receipt_ref.set("IR" + randomRef)
            elif (var9.get() == "Etawah" and var2.get() == 1 and var5.get() == 1):
                tcost = float(323)
                single = float(var12.get())
                adult_tax = "Rs", str(tcost * single * 0.9)
                adult_fees = "Rs", str(tcost * single)
                total_cost = "Rs", str((tcost * single) + ((tcost * single) * 0.9))
                Tax.set(adult_tax)
                Subtotal.set(adult_fees)
                Total.set(total_cost)
                Ticketclass.set("Second")
                Ticketprice.set(adult_fees)
                Child_ticket.set("Yes")
                Adult_ticket.set("No")
                From_destination.set("Kanpur")
                To_destination.set("Etawah")
                Fee_price.set(total_cost)
                Route.set("Direct")

                x = random.randint(10900, 50980)
                randomRef = str(x)
                Receipt_ref.set("IR" + randomRef)
            elif (var9.get() == "Gurugram" and var2.get() == 1 and var4.get() == 1):
                tcost = float(788)
                single = float(var12.get())
                adult_tax = "Rs", str(tcost * single * 0.9)
                adult_fees = "Rs", str (tcost * single)
                total_cost = "Rs", str((tcost * single) + ((tcost * single) * 0.9))
                Tax.set(adult_tax)
                Subtotal.set(adult_fees)
                Total.set(total_cost)
                Ticketclass.set("Second")
                Ticketprice.set(adult_fees)
                Child_ticket.set("No")
                Adult_ticket.set("Yes")
                From_destination.set("Kanpur")
                To_destination.set("Gurugram")
                Fee_price.set(total_cost)
                Route.set("Direct")

                x = random.randint(10900, 50980)
                randomRef = str(x)
                Receipt_ref.set("IR" + randomRef)
            elif (var9.get() == "Gurugram" and var2.get() == 1 and var5.get() == 1):
                tcost = float(678)
                single = float(var12.get())
                adult_tax = "Rs", str(tcost * single * 0.9)
                adult_fees = "Rs", str(tcost * single)
                total_cost = "Rs", str((tcost * single) + ((tcost * single) * 0.9))
                Tax.set(adult_tax)
                Subtotal.set(adult_fees)
                Total.set(total_cost)
                Ticketclass.set("Second")
                Ticketprice.set(adult_fees)
                Child_ticket.set("Yes")
                Adult_ticket.set("No")
                From_destination.set("Kanpur")
                To_destination.set("Gurugram")
                Fee_price.set(total_cost)
                Route.set("Direct")

                x = random.randint(10900, 50980)
                randomRef = str(x)
                Receipt_ref.set("IR" + randomRef)
            elif (var9.get() == "Ludhiana" and var2.get() == 1 and var4.get() == 1):
                tcost = float(2500)
                single = float(var12.get())
                adult_tax = "Rs", str(tcost * single* 0.9)
                adult_fees = "Rs", str(tcost * single)
                total_cost = "Rs", str((tcost * single) + ((tcost * single) * 0.9))
                Tax.set(adult_tax)
                Subtotal.set(adult_fees)
                Total.set(total_cost)
                Ticketclass.set("Second")
                Ticketprice.set(adult_fees)
                Child_ticket.set("No")
                Adult_ticket.set("Yes")
                From_destination.set("Kanpur")
                To_destination.set("Ludhiana")
                Fee_price.set(total_cost)
                Route.set("Direct")

                x = random.randint(10900, 50980)
                randomRef = str(x)
                Receipt_ref.set("IR" + randomRef)
            elif (var9.get() == "Ludhiana" and var2.get() == 1 and var5.get() == 1):
                tcost = float(1234)
                single = float(var12.get())
                adult_tax = "Rs", str(tcost * single * 0.9)
                adult_fees = "Rs", str(tcost * single)
                total_cost = "Rs", str((tcost * single) + ((tcost * single) * 0.9))
                Tax.set(adult_tax)
                Subtotal.set(adult_fees)
                Total.set(total_cost)
                Ticketclass.set("Second")
                Ticketprice.set(adult_fees)
                Child_ticket.set("Yes")
                Adult_ticket.set("No")
                From_destination.set("Kanpur")
                To_destination.set("Ludhiana")
                Fee_price.set(total_cost)
                Route.set("Direct")

                x = random.randint(10900, 50980)
                randomRef = str(x)
                Receipt_ref.set("IR" + randomRef)
            elif (var9.get() == "Ambala" and var2.get() == 1 and var4.get() == 1):
                tcost = float(1999)
                single = float(var12.get())
                adult_tax = "Rs", str(tcost * single * 0.9)
                adult_fees = "Rs", str(tcost * single)
                total_cost = "Rs", str((tcost * single) + ((tcost * single) * 0.9))
                Tax.set(adult_tax)
                Subtotal.set(adult_fees)
                Total.set(total_cost)
                Ticketclass.set("Second")
                Ticketprice.set(adult_fees)
                Child_ticket.set("No")
                Adult_ticket.set("Yes")
                From_destination.set("Kanpur")
                To_destination.set("Ambala")
                Fee_price.set(total_cost)
                Route.set("Direct")

                x = random.randint(10900, 50980)
                randomRef = str(x)
                Receipt_ref.set("IR" + randomRef)
            elif (var9.get() == "Ambala" and var2.get() == 1 and var5.get() == 1):
                tcost = float(1599)
                single = float(var12.get())
                adult_tax = "Rs", str(tcost * single * 0.9)
                adult_fees = "Rs", str(tcost * single)
                total_cost = "Rs", str((tcost * single) + ((tcost * single) * 0.9))
                Tax.set(adult_tax)
                Subtotal.set(adult_fees)
                Total.set(total_cost)
                Ticketclass.set("Second")
                Ticketprice.set(adult_fees)
                Child_ticket.set("Yes")
                Adult_ticket.set("No")
                From_destination.set("Kanpur")
                To_destination.set("Ambala")
                Fee_price.set(total_cost)
                Route.set("Direct")

                x = random.randint(10900, 50980)
                randomRef = str(x)
                Receipt_ref.set("IR" + randomRef)

            elif (var9.get() == "New Delhi" and var3.get() == 1 and var4.get() == 1):
                tcost = float(130)
                single = float(var12.get())
                adult_tax = "Rs", str (tcost * single * 0.9)
                adult_fees = "Rs", str(tcost * single)
                total_cost = "Rs", str((tcost * single) + ((tcost * single) * 0.9))
                Tax.set(adult_tax)
                Subtotal.set(adult_fees)
                Ticketclass.set("General")
                Ticketprice.set(adult_fees)
                Child_ticket.set("No")
                Adult_ticket.set("Yes")
                From_destination.set("Kanpur")
                To_destination.set("New Delhi")
                Fee_price.set(total_cost)
                Total.set(total_cost)
                Route.set("Direct")

                x = random.randint(10900, 50980)
                randomRef = str(x)
                Receipt_ref.set("IR" + randomRef)
            elif (var9.get() == "New Delhi" and var3.get() == 1 and var5.get() == 1):
                tcost = float(189)
                single = float(var12.get())
                adult_tax = "Rs", str(tcost * single* 0.9)
                adult_fees = "Rs", str (tcost * single)
                total_cost = "Rs", str((tcost * single) + ((tcost * single) * 0.9))
                Tax.set(adult_tax)
                Subtotal.set(adult_fees)
                Ticketclass.set("General")
                Ticketprice.set(adult_fees)
                Child_ticket.set("Yes")
                Adult_ticket.set("No")
                From_destination.set("Kanpur")
                To_destination.set("New Delhi")
                Fee_price.set(total_cost)
                Total.set(total_cost)
                Route.set("Direct")

                x = random.randint(10900, 50980)
                randomRef = str(x)
                Receipt_ref.set("IR" + randomRef)

            elif (var9.get() == "Varanasi" and var3.get() == 1 and var4.get() == 1):
                tcost = float(144)
                single = float(var12.get())
                adult_tax = "Rs", str(tcost * single * 0.9)
                adult_fees = "Rs", str(tcost * single)
                total_cost = "Rs", str((tcost * single) + ((tcost * single) * 0.9))
                Tax.set(adult_tax)
                Subtotal.set(adult_fees)
                Total.set(total_cost)
                Ticketclass.set("General")
                Ticketprice.set(adult_fees)
                Child_ticket.set("No")
                Adult_ticket.set("Yes")
                From_destination.set("Kanpur")
                To_destination.set("Varanasi")
                Fee_price.set(total_cost)
                Route.set("Direct")

                x = random.randint(10900, 50980)
                randomRef = str(x)
                Receipt_ref.set("IR" + randomRef)
            elif (var9.get() == "Varanasi" and var3.get() == 1 and var5.get() == 1):
                tcost = float(109)
                single = float(var12.get())
                adult_tax = "Rs", str(tcost * single * 0.9)
                adult_fees = "Rs", str(tcost * single)
                total_cost = "Rs", str((tcost * single) + ((tcost * single) * 0.9))
                Tax.set(adult_tax)
                Subtotal.set(adult_fees)
                Total.set(total_cost)
                Ticketclass.set("General")
                Ticketprice.set(adult_fees)
                Child_ticket.set("Yes")
                Adult_ticket.set("No")
                From_destination.set("Kanpur")
                To_destination.set("Varanasi")
                Fee_price.set(total_cost)
                Route.set("Direct")

                x = random.randint(10900, 50980)
                randomRef = str(x)
                Receipt_ref.set("IR" + randomRef)
            elif (var9.get() == "Etawah" and var3.get() == 1 and var4.get() == 1):
                tcost = float(199)
                single = float(var12.get())
                adult_tax = "Rs", str(tcost * single* 0.9)
                adult_fees = "Rs", str(tcost * single)
                total_cost = "Rs", str((tcost * single) + ((tcost * single) * 0.9))
                Tax.set(adult_tax)
                Subtotal.set(adult_fees)
                Total.set(total_cost)
                Ticketclass.set("General")
                Ticketprice.set(adult_fees)
                Child_ticket.set("No")
                Adult_ticket.set("Yes")
                From_destination.set("Kanpur")
                To_destination.set("Etawah")
                Fee_price.set(total_cost)
                Route.set("Direct")

                x = random.randint(10900, 50980)
                randomRef = str(x)
                Receipt_ref.set("IR" + randomRef)
            elif (var9.get() == "Etawah" and var3.get() == 1 and var5.get() == 1):
                tcost = float(123)
                single = float(var12.get())
                adult_tax = "Rs", str((tcost * single) * 0.9)
                adult_fees = "Rs", str(tcost * single)
                total_cost = "Rs", str((tcost * single) + ((tcost * single) * 0.9))
                Tax.set(adult_tax)
                Subtotal.set(adult_fees)
                Total.set(total_cost)
                Ticketclass.set("General")
                Ticketprice.set(adult_fees)
                Child_ticket.set("Yes")
                Adult_ticket.set("No")
                From_destination.set("Kanpur")
                To_destination.set("Etawah")
                Fee_price.set(total_cost)
                Route.set("Direct")

                x = random.randint(10900, 50980)
                randomRef = str(x)
                Receipt_ref.set("IR" + randomRef)
            elif (var9.get() == "Gurugram" and var3.get() == 1 and var4.get() == 1):
                tcost = float(188)
                single = float(var12.get())
                adult_tax = "Rs", str(tcost * single* 0.9)
                adult_fees = "Rs", str(tcost * single)
                total_cost = "Rs", str((tcost * single) + ((tcost * single) * 0.9))
                Tax.set(adult_tax)
                Subtotal.set(adult_fees)
                Total.set(total_cost)
                Ticketclass.set("General")
                Ticketprice.set(adult_fees)
                Child_ticket.set("No")
                Adult_ticket.set("Yes")
                From_destination.set("Kanpur")
                To_destination.set("Gurugram")
                Fee_price.set(total_cost)
                Route.set("Direct")

                x = random.randint(10900, 50980)
                randomRef = str(x)
                Receipt_ref.set("IR" + randomRef)
            elif (var9.get() == "Gurugram" and var3.get() == 1 and var5.get() == 1):
                tcost = float(178)
                single = float(var12.get())
                adult_tax = "Rs", str(tcost * single * 0.9)
                adult_fees = "Rs", str(tcost * single)
                total_cost = "Rs", str((tcost * single) + ((tcost * single) * 0.9))
                Tax.set(adult_tax)
                Subtotal.set(adult_fees)
                Total.set(total_cost)
                Ticketclass.set("General")
                Ticketprice.set(adult_fees)
                Child_ticket.set("Yes")
                Adult_ticket.set("No")
                From_destination.set("Kanpur")
                To_destination.set("Gurugram")
                Fee_price.set(total_cost)
                Route.set("Direct")

                x = random.randint(10900, 50980)
                randomRef = str(x)
                Receipt_ref.set("IR" + randomRef)
            elif (var9.get() == "Ludhiana" and var3.get() == 1 and var4.get() == 1):
                tcost = float(100)
                single = float(var12.get())
                adult_tax = "Rs", str(tcost * single* 0.9)
                adult_fees = "Rs", str(tcost * single)
                total_cost = "Rs", str((tcost * single) + ((tcost * single) * 0.9))
                Tax.set(adult_tax)
                Subtotal.set(adult_fees)
                Total.set(total_cost)
                Ticketclass.set("General")
                Ticketprice.set(adult_fees)
                Child_ticket.set("No")
                Adult_ticket.set("Yes")
                From_destination.set("Kanpur")
                To_destination.set("Ludhiana")
                Fee_price.set(total_cost)
                Route.set("Direct")

                x = random.randint(10900, 50980)
                randomRef = str(x)
                Receipt_ref.set("IR" + randomRef)
            elif (var9.get() == "Ludhiana" and var3.get() == 1 and var5.get() == 1):
                tcost = float(234)
                single = float(var12.get())
                adult_tax = "Rs", str(tcost * single* 0.9)
                adult_fees = "Rs", str(tcost * single)
                total_cost = "Rs", str((tcost * single) + ((tcost * single) * 0.9))
                Tax.set(adult_tax)
                Subtotal.set(adult_fees)
                Total.set(total_cost)
                Ticketclass.set("General")
                Ticketprice.set(adult_fees)
                Child_ticket.set("Yes")
                Adult_ticket.set("No")
                From_destination.set("Kanpur")
                To_destination.set("Ludhiana")
                Fee_price.set(total_cost)
                Route.set("Direct")

                x = random.randint(10900, 50980)
                randomRef = str(x)
                Receipt_ref.set("IR" + randomRef)
            elif (var9.get() == "Ambala" and var3.get() == 1 and var4.get() == 1):
                tcost = float(199)
                single = float(var12.get())
                adult_tax = "Rs", str(tcost * single* 0.9)
                adult_fees = "Rs", str(tcost * single)
                total_cost = "Rs", str((tcost * single) + ((tcost * single) * 0.9))
                Tax.set(adult_tax)
                Subtotal.set(adult_fees)
                Total.set(total_cost)
                Ticketclass.set("General")
                Ticketprice.set(adult_fees)
                Child_ticket.set("No")
                Adult_ticket.set("Yes")
                From_destination.set("Kanpur")
                To_destination.set("Ambala")
                Fee_price.set(total_cost)
                Route.set("Direct")

                x = random.randint(10900, 50980)
                randomRef = str(x)
                Receipt_ref.set("IR" + randomRef)
            elif (var9.get() == "Ambala" and var3.get() == 1 and var5.get() == 1):
                tcost = float(299)
                single = float(var12.get())
                adult_tax = "Rs", str(tcost * single * 0.9)
                adult_fees = "Rs", str(tcost * single)
                total_cost = "Rs", str((tcost * single) + ((tcost * single) * 0.9))
                Tax.set(adult_tax)
                Subtotal.set(adult_fees)
                Total.set(total_cost)
                Ticketclass.set("General")
                Ticketprice.set(adult_fees)
                Child_ticket.set("Yes")
                Adult_ticket.set("No")
                From_destination.set("Kanpur")
                To_destination.set("Ambala")
                Fee_price.set(total_cost)
                Route.set("Direct")

                x = random.randint(10900, 50980)
                randomRef = str(x)
                Receipt_ref.set("IR" + randomRef)

        def chkSbtn_value():
            if(var10.get()==1):
                var12.set("")
                entersingle.focus()
                entersingle.configure(state='normal')
                var11.set(0)
                enterreturn.configure(state='disabled')
                var6.set("0")
            elif var10.get()==0:
                entersingle.configure(state='disabled')
                var12.set("0")
        def chkRbtn_value():
            if(var11.get()==1):
                var6.set("")
                enterreturn.focus()
                enterreturn.configure(state='normal')
                var10.set(0)
                entersingle.configure(state='disabled')
                var12.set("0")
            elif var11.get()==0:
                enterreturn.configure(state='disabled')
                var6.set("0")

        #---------------------------------------LABEL WIDGET-------------------------------------------------
        lbReceipt=Label(Frametopright,font=('arial',18,'bold'),text="Travelling Ticketing System",bd=5,width=28,pady=10,padx=4,justify="center")
        lbReceipt.grid(row=0,column=0)

        lbClass1 = Label(Framebottomright, font=('arial', 14, 'bold'), text="Class",width=8,justify="center",relief="sunken")
        lbClass1.grid(row=0, column=0)

        lbClass2 = Label(Framebottomright, font=('arial', 14, 'bold'), textvariable=Ticketclass, width=8,justify="center",relief="sunken")
        lbClass2.grid(row=1, column=0)

        lbTicket1 = Label(Framebottomright, font=('arial', 14, 'bold'), text="Ticket", width=8,relief="sunken", justify="center")
        lbTicket1.grid(row=0, column=1)

        lbTicket2 = Label(Framebottomright, font=('arial', 14, 'bold'), textvariable=Ticketprice, width=8,relief="sunken", justify="center")
        lbTicket2.grid(row=1, column=1)

        lbAdult1=Label(Framebottomright,font=('arial',14,'bold'),text="Adult",width=8,relief="sunken",justify="center")
        lbAdult1.grid(row=0,column=2)

        lbAdult2=Label(Framebottomright,font=('arial',14,'bold'),textvariable=Adult_ticket,width=8,relief="sunken",justify="center")
        lbAdult2.grid(row=1,column=2)

        lbChild1 = Label(Framebottomright, font=('arial', 14, 'bold'), text="Child",width=8,relief="sunken", justify="center")
        lbChild1.grid(row=0, column=3)

        lbChild2 = Label(Framebottomright, font=('arial', 14, 'bold'), textvariable=Child_ticket,width=8,relief="sunken",justify="center")
        lbChild2.grid(row=1, column=3)
        #---------------------------------------------------------------------------------------------------------------------------------------
        lbsp = Label(Framebottomright, font=('arial', 14, 'bold'), width=36,height=2,relief="sunken", justify="center",bg="lightgray")
        lbsp.grid(row=2, column=0,columnspan=4)  #space bar
        #---------------------------------------------------------------------------------------------------------------------------------------
        lbFrom1 = Label(Framebottomright, font=('arial', 14, 'bold'), text="From", width=8,relief="sunken", justify="center")
        lbFrom1.grid(row=3, column=1)
        lbFrom2 = Label(Framebottomright, font=('arial', 14, 'bold'), textvariable=From_destination, width=8, relief="sunken",justify="center")
        lbFrom2.grid(row=3, column=2)

        lbTo1= Label(Framebottomright, font=('arial', 14, 'bold'), text="To", width=8, relief="sunken",justify="center")
        lbTo1.grid(row=4, column=1)
        lbTo1 = Label(Framebottomright, font=('arial', 14, 'bold'), textvariable=To_destination, width=8, relief="sunken",justify="center")
        lbTo1.grid(row=4, column=2)

        lbPrice1 = Label(Framebottomright, font=('arial', 14, 'bold'), text="Price", width=8, relief="sunken",justify="center")
        lbPrice1.grid(row=5, column=1)
        lbPrice2 = Label(Framebottomright, font=('arial', 14, 'bold'), textvariable=Fee_price, width=8, relief="sunken",justify="center")
        lbPrice2.grid(row=5, column=2)
                #-----------------------------------------------------------------------------------------------------------------------------------------------
        lbsp2 = Label(Framebottomright, font=('arial', 14, 'bold'), width=36, height=2, relief="sunken",justify="center", bg="lightgray")
        lbsp2.grid(row=6, column=0, columnspan=4)
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        lbRefno1 = Label(Framebottomright, font=('arial', 14, 'bold'), text="Ref No", width=8,relief="sunken", justify="center")
        lbRefno1.grid(row=7, column=0)
        lbRefno2 = Label(Framebottomright, font=('arial', 14, 'bold'), textvariable=Receipt_ref, width=8,relief="sunken", justify="center")
        lbRefno2.grid(row=8, column=0)
        lbTime1 = Label(Framebottomright, font=('arial', 14, 'bold'), text="Time", width=8,relief="sunken", justify="center")
        lbTime1.grid(row=7, column=1)
        lbTime2 = Label(Framebottomright, font=('arial', 14, 'bold'), textvariable=Time1, width=8,relief="sunken", justify="center")
        lbTime2.grid(row=8, column=1)
        lbDate1= Label(Framebottomright, font=('arial', 14, 'bold'), text="Date", width=8,relief="sunken", justify="center")
        lbDate1.grid(row=7, column=2)
        lbDate2 = Label(Framebottomright, font=('arial', 14, 'bold'), textvariable=Date1, width=8,relief="sunken", justify="center")
        lbDate2.grid(row=8, column=2)
        lbRoute1 = Label(Framebottomright, font=('arial', 14, 'bold'), text="Route", width=8,relief="sunken", justify="center")
        lbRoute1.grid(row=7, column=3)
        lbRoute2 = Label(Framebottomright, font=('arial', 14, 'bold'), textvariable=Route, width=8,relief="sunken", justify="center")
        lbRoute2.grid(row=8, column=3)
        # -----------------------------------------------------------------------------------------------------------------------------------------------
        Date1.set(time.strftime("%d/%m/%y"))
        Time1.set(time.strftime("%H:%M:%S"))
        #================================================================================================================================================

        lblClass = Label(topleft1,font=('arial',20,'bold'),text="Class",bd=8).grid(row=0,column=0,sticky=W)

        chkfirstclass = Checkbutton( topleft1,font=('arial',20,'bold'),text="First",variable= var1 ,onvalue = 1, offvalue=0).grid(row=1,column=0,sticky=W)
        chksecondclass = Checkbutton(topleft1, font=('arial', 20, 'bold'), text="Second", variable=var2, onvalue=1,
                                  offvalue=0).grid(row=2, column=0, sticky=W)
        chkgeneral = Checkbutton(topleft1, font=('arial', 20, 'bold'), text="General", variable=var3, onvalue=1,
                                  offvalue=0).grid(row=3, column=0, sticky=W)

        #================================================================================================================================================

        lblselect = Label(topleft3, font=('arial', 20, 'bold'), text="Select Destination", bd=8).grid(row=0, column=0, sticky=W,columnspan=2)

        lbldestination = Label(topleft3, font=('arial', 20, 'bold'), text="Destination", bd=2).grid(row=1, column=0,
                                                                                                      sticky=W)
        codestination= ttk.Combobox(topleft3,textvariable=var9,font=('arial', 20, 'bold'),state="readonly", width=9)
        codestination['value']=(' ','New Delhi','Varanasi','Etawah','Gurugram','Ludhiana','Ambala')
        codestination.current(0)
        codestination.grid(row=1,column=1)
        chkadult = Checkbutton(topleft3, font=('arial', 20, 'bold'), text="Adult", variable=var4, onvalue=1,
                                    offvalue=0).grid(row=2, column=0, sticky=W)
        chkchild = Checkbutton(topleft3, font=('arial', 20, 'bold'), text="Child", variable=var5, onvalue=1,
                                     offvalue=0).grid(row=3, column=0, sticky=W)

        #================================================================================================================================================
        lbticketype = Label(topleft2, font=('arial', 20, 'bold'), text="Ticket Type", bd=8).grid(row=0, column=0, sticky=W)
        chkSingle = Checkbutton(topleft2, font=('arial', 20, 'bold'), text="Single", variable=var10, onvalue=1,offvalue=0,command= chkSbtn_value )
        chkSingle.grid(row=1, column=0, sticky=W)
        entersingle = Entry(topleft2, font=('arial', 20, 'bold'), textvariable=var12, bd=8, width=8)
        entersingle.grid(row=1, column=1,sticky=W)
        chkReturn = Checkbutton(topleft2, font=('arial', 20, 'bold'), text="Return", variable=var11, onvalue=1,
                               offvalue=0,command= chkRbtn_value)
        chkReturn.grid(row=2, column=0, sticky=W)
        enterreturn = Entry(topleft2, font=('arial', 20, 'bold'), textvariable=var6, bd=8, width=8)
        enterreturn.grid(row=2,column=1,sticky=W)

        lb1Comment = Label(topleft2,font=('arial', 20, 'bold'),text="Comment",bd=8).grid(row=3,column=0,sticky=W)
        entComment = Entry(topleft2,font=('arial', 20, 'bold'),textvariable=var7,bd=8,width=8).grid(row=3,column=1,sticky=W)
        #------------------------------------------------------------------------------------------------------------------------------------------------
        btntotal=Button(Framebottomright, font=('arial', 14, 'bold'),text="Total",width=8,height=1,padx=2,pady=16,bd=2,bg="green",command=travelcost,cursor="hand2")
        btntotal.grid(row=10,column=0)
        btnclear = Button(Framebottomright, font=('arial', 14, 'bold'), text="Clear", width=8, height=1, padx=2,pady=16, bd=2,bg="lightblue",command=Reset,cursor="hand2")
        btnclear.grid(row=10, column=1)
        btnreset = Button(Framebottomright, font=('arial', 14, 'bold'), text="Reset", width=8, height=1, padx=2,pady=16, bd=2,bg="yellow",command=Reset,cursor="hand2")
        btnreset.grid(row=10, column=2)
        btnexit = Button(Framebottomright, font=('arial', 14, 'bold'), text="Exit", width=8, height=1, padx=2,pady=16, bd=2,bg="red",command=iExit,cursor="hand2")
        btnexit.grid(row=10, column=3)
        #-------------------------------------------------------------------------------------------------------------------------------------
        lbtax = Label(bottomleft1, font=('arial', 20, 'bold'), text="Tax", bd=8).grid(row=0, column=0,
                                                                                                 sticky=W)
        entertax = Entry(bottomleft1, font=('arial', 20, 'bold'), textvariable=Tax, bd=8, width=28).grid(row=0,
                                                                                                          column=1,
                                                                                                          sticky=W)
        lbsubtotal = Label(bottomleft1, font=('arial', 20, 'bold'), text="Sub Total", bd=8).grid(row=1, column=0,
                                                                                      sticky=W)
        entersub = Entry(bottomleft1, font=('arial', 20, 'bold'), textvariable=Subtotal, bd=8, width=28).grid(row=1,
                                                                                                        column=1,
                                                                                                        sticky=W)
        lbtotal = Label(bottomleft1, font=('arial', 20, 'bold'), text="Total", bd=8).grid(row=2, column=0,
                                                                                      sticky=W)
        entertotal = Entry(bottomleft1, font=('arial', 20, 'bold'), textvariable=Total, bd=8, width=28).grid(row=2,
                                                                                                        column=1,
                                                                                                        sticky=W)

        #----------------------------------------------------------------------------------------------------------------

        self.txtdisplay= Entry(bottomleft2,font=('arial', 19, 'bold'),textvariable=text_input,bd=5,insertwidth=4,justify="right")
        self.txtdisplay.grid(columnspan=4)
        self.btn7 = Button(bottomleft2,padx=6,pady=5, font=('arial', 16, 'bold'),fg="black", text="7", bd=2, width=4,command=lambda: btnClick(7)).grid(row=1,column=0)
        self.btn8 = Button(bottomleft2, padx=6, pady=5, font=('arial', 16, 'bold'), fg="black", text="8", bd=2, width=4,
                           command=lambda: btnClick(8)).grid(row=1, column=1)
        self.btn9 = Button(bottomleft2, padx=6, pady=5, font=('arial', 16, 'bold'), fg="black", text="9", bd=2, width=4,
                          command=lambda: btnClick(9)).grid(row=1, column=2)
        Addition=Button(bottomleft2,padx=6,pady=5,bd=2,fg="black",font=('arial', 16, 'bold'),width=4,text="+",command=lambda:btnClick("+")).grid(row=1,column=3)
        # #==============================================================================================================================================
        self.btn4 = Button(bottomleft2, padx=6, pady=5, font=('arial', 16, 'bold'), fg="black", text="4", bd=2, width=4,
                           command=lambda: btnClick(4)).grid(row=2, column=0)
        self.btn5 = Button(bottomleft2, padx=6, pady=5, font=('arial', 16, 'bold'), fg="black", text="5", bd=2, width=4,
                           command=lambda: btnClick(5)).grid(row=2, column=1)
        self.btn6 = Button(bottomleft2, padx=6, pady=5, font=('arial', 16, 'bold'), fg="black", text="6", bd=2, width=4,
                           command=lambda: btnClick(6)).grid(row=2, column=2)
        subtraction = Button(bottomleft2, padx=6, pady=5, bd=2, fg="black", font=('arial', 16, 'bold'), width=4, text="-",
                          command=lambda: btnClick("=")).grid(row=2, column=3)
        # ==============================================================================================================================================
        self.btn1 = Button(bottomleft2, padx=6, pady=5, font=('arial', 16, 'bold'), fg="black", text="1", bd=2, width=4,
                           command=lambda: btnClick(1)).grid(row=3, column=0)
        self.btn2 = Button(bottomleft2, padx=6, pady=5, font=('arial', 16, 'bold'), fg="black", text="2", bd=2, width=4,
                           command=lambda: btnClick(2)).grid(row=3, column=1)
        self.btn3 = Button(bottomleft2, padx=6, pady=5, font=('arial', 16, 'bold'), fg="black", text="3", bd=2, width=4,
                           command=lambda: btnClick(3)).grid(row=3, column=2)
        multiply = Button(bottomleft2, padx=6, pady=5, bd=2, fg="black", font=('arial', 16, 'bold'), width=4, text="*",
                          command=lambda: btnClick("*")).grid(row=3, column=3)
        # ==============================================================================================================================================
        self.btn0 = Button(bottomleft2, padx=6, pady=5, font=('arial', 16, 'bold'), fg="black", text="0", bd=2, width=4,
                           command=lambda: btnClick(0)).grid(row=4, column=0)
        self.btnclear = Button(bottomleft2, padx=6, pady=5, font=('arial', 16, 'bold'), fg="black", text="C", bd=2, width=4,command=btnClearDisplay).grid(row=4, column=1)
        self.btnEqual = Button(bottomleft2, padx=6, pady=5, font=('arial', 16, 'bold'), fg="black", text="=", bd=2, width=4,command=btnequalsinput).grid(row=4, column=2)
        self.division = Button(bottomleft2, padx=6, pady=5, bd=2, fg="black", font=('arial', 16, 'bold'), width=4, text="/",
                          command=lambda: btnClick("/")).grid(row=4, column=3)
        # ==============================================================================================================================================

class payment:
    def __init__(self,root):
        self.root=root
        self.root.title("Payment Form")
        self.root.geometry('1800x980+50+0')
        self.root.configure(background="powder blue")

        Tops = Frame(root, width=1850, height=50, bd=8, bg="powder blue")
        Tops.pack(side=TOP)

        f1 = Frame(root, width=925, height=600, bd=8, bg="powder blue")
        f1.pack(side=LEFT)
        f2 = Frame(root, width=300, height=700, bd=8, bg="powder blue")
        f2.pack(side=RIGHT)

        fla = Frame(f1, width=925, height=200, bd=8, bg="powder blue")
        fla.pack(side=TOP)
        flb = Frame(f1, width=300, height=600, bd=8, bg="powder blue")
        flb.pack(side=TOP)

        lblinfo = Label(Tops, font=('arial', 45, 'bold'), text="Payment Information ", bd=10, fg="green")
        lblinfo.grid(row=0, column=0)
# =============================== Variables ========================================================
        Name = StringVar()
        Address = StringVar()
        HoursWorked = StringVar()
        wageshour = StringVar()
        Payable = StringVar()
        Taxable = StringVar()
        NetPayable = StringVar()
        GrossPayable = StringVar()
        OverTimeBonus = StringVar()
        Employer = StringVar()
        NINumber = StringVar()
        TimeOfOrder = StringVar()
        DateOfOrder = StringVar()

        DateOfOrder.set(time.strftime("%d/%m/%Y"))

        def exit():
            exit = tkinter.messagebox.askyesno("Employee system", "Do you want to exit the system")
            if exit > 0:
                root.destroy()
                return

        def reset():
            Name.set("")
            Address.set("")
            HoursWorked.set("")
            wageshour.set("")
            Payable.set("")
            Taxable.set("")
            NetPayable.set("")
            GrossPayable.set("")
            OverTimeBonus.set("")
            Employer.set("")
            NINumber.set("")
            txtpayslip.delete("1.0", END)

        def enterinfo():
            txtpayslip.delete("1.0", END)
            txtpayslip.insert(END, "\t\tPay Info.\n\n")
            txtpayslip.insert(END, "Name :\t\t" + Name.get() + "\n\n")
            txtpayslip.insert(END, "Address :\t\t" + Address.get() + "\n\n")
            txtpayslip.insert(END, "gender :\t\t" + Employer.get() + "\n\n")
            txtpayslip.insert(END, "Card Number :\t\t" + NINumber.get() + "\n\n")
            txtpayslip.insert(END, "CVV Number :\t\t" + HoursWorked.get() + "\n\n")

        # ================================ Label Widget =================================================

        lblName = Label(fla, text="Name", font=('arial', 16, 'bold'), bd=20, fg="red", bg="powder blue").grid(row=0, column=0)
        lblAddress = Label(fla, text="Address", font=('arial', 16, 'bold'), bd=20, fg="red", bg="powder blue").grid(row=0,
                                                                                                            column=2)
        lblEmployer = Label(fla, text="Gender", font=('arial', 16, 'bold'), bd=20, fg="red", bg="powder blue").grid(row=1,
                                                                                                            column=0)
        lblNINumber = Label(fla, text="Card Number", font=('arial', 16, 'bold'), bd=20, fg="red", bg="powder blue").grid(row=1,
                                                                                                                 column=2)
        lblHoursWorked = Label(fla, text="CVV Number", font=('arial', 16, 'bold'), bd=20, fg="red", bg="powder blue").grid(
            row=2, column=0)
        lblTax = Label(fla, text="Tax", font=('arial', 16, 'bold'), bd=20, anchor='w', fg="red", bg="powder blue").grid(row=3,
                                                                                                                column=0)
# =============================== Entry Widget =================================================

        etxname = Entry(fla, textvariable=Name, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
        etxname.grid(row=0, column=1)

        etxaddress = Entry(fla, textvariable=Address, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
        etxaddress.grid(row=0, column=3)

        etxemployer = Entry(fla, textvariable=Employer, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
        etxemployer.grid(row=1, column=1)

        etxhoursworked = Entry(fla, textvariable=HoursWorked, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
        etxhoursworked.grid(row=2, column=1)

        etxnin = Entry(fla, textvariable=NINumber, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
        etxnin.grid(row=1, column=3)

        etxtax = Entry(fla, textvariable=Taxable, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
        etxtax.grid(row=3, column=1)

# =============================== Text Widget ============================================================

        payslip = Label(f2, textvariable=DateOfOrder, font=('arial', 21, 'bold'), fg="red", bg="powder blue").grid(row=0,
                                                                                                           column=0)
        txtpayslip = Text(f2, height=22, width=34, bd=16, font=('arial', 13, 'bold'), fg="green", bg="powder blue")
        txtpayslip.grid(row=1, column=0)

# =============================== buttons ===============================================================

        btnreset = Button(flb, text='Reset', padx=16, pady=16, bd=8, font=('arial', 16, 'bold'), width=14, command=reset,
                        fg="red", bg="powder blue").grid(row=0, column=1)

        btnpayslip = Button(flb, text='Pay', padx=16, pady=16, bd=8, font=('arial', 16, 'bold'), width=14, command=enterinfo,
                    fg="red", bg="powder blue").grid(row=0, column=2)

        btnexit = Button(flb, text='Exit System', padx=16, pady=16, bd=8, font=('arial', 16, 'bold'), width=14, command=exit,
                 fg="red", bg="powder blue").grid(row=0, column=3)


if __name__=="__main__":
    main()