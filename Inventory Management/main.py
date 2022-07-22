from tkinter import *
import tkinter.messagebox
import sqlite3
import tkinter.ttk as ttk
import datetime
import math
conn=sqlite3.connect("/home/bokerns/Desktop/Inventory Management/Database/data.db")
c=conn.cursor()

product_name=[]
product_quantity=[]
product_amount=[]
product_id=[]
label_lists=[]
date=datetime.datetime.now().date()
class Application:
    def __init__(self,master,*args,**kwargs):

        self.master=master

        self.left=Frame(master,width=800,height=768,bg='lightgray')
        self.left.pack(side=LEFT)

        self.right=Frame(master,width=566,height=768,bg='cadet blue')
        self.right.pack(side=RIGHT)

        self.heading=Label(self.left,text="Customer Window",font=('arial 40 bold'),bg='white')
        self.heading.place(x=0,y=0)

        self.date_l=Label(self.right,text="Today is"+" "+str(date),font=('arial 15 bold'),bg='white')
        self.date_l.place(x=0,y=0)


        self.tproduct=Label(self.right,text="Products",font=('arial 15 bold'),bg='lightblue',fg='white')
        self.tproduct.place(x=0,y=60)

        self.tquantity=Label(self.right,text="Quantity",font=('arial 15 bold'),bg='lightblue',fg='white')
        self.tquantity.place(x=250,y=60)

        self.tamount=Label(self.right,text="Amount",font=('arial 15 bold'),bg='lightblue',fg='white')
        self.tamount.place(x=430,y=60)

        self.enterid=Label(self.left,text="Enter Product's ID",font=('arial 18 bold'),bg='white')
        self.enterid.place(x=0,y=80)

        self.enteride=Entry(self.left,width=25,bg='white',font=('arial 18 bold'))
        self.enteride.place(x=230,y=80)

        self.search_b=Button(master,text="Search",width=20,height=2,bg='orange',fg='white',command=self.result)
        self.search_b.place(x=370,y=120)

        self.productname=Label(self.left,text="",font=('arial 27 bold'),bg='white',fg="cadet blue")
        self.productname.place(x=0,y=250)
        
        self.pprice=Label(self.left,text="",font=('arial 27 bold'),bg='white',fg="cadet blue")
        self.pprice.place(x=0,y=290)
        
        self.total_l=Label(self.right,text="",font=('arial 40 bold'),bg='lightblue',fg='white')
        self.total_l.place(x=0,y=600)
    def result(self,*args,**kwargs):
        self.get_id=self.enteride.get()
        query= "SELECT * FROM inventory WHERE id=?"
        result=c.execute(query,(self.get_id,))
        for self.r in result:
            self.get_id=self.r[0]
            self.get_name=self.r[1]
            self.get_price=self.r[4]
            self.get_stock=self.r[2]
        self.productname.config(text="Product: "+""+str(self.get_name))
        self.pprice.config(text="Price"+" ₱ "+str(self.get_price))

        self.quantity_lq=Label(self.left,text="Enter Quantity",font=('arial 18 bold'),bg='white',fg="black")
        self.quantity_lq.place(x=0,y=370)

        self.quantity_lqe=Entry(self.left,width=25,font=('arial 18 bold'),bg='white',fg="black")
        self.quantity_lqe.place(x=190,y=370)

        self.quantity_led=Label(self.left,text="Enter Discount",font=('arial 18 bold'),bg='white',fg="black")
        self.quantity_led.place(x=0,y=410)


        self.quantity_lede=Entry(self.left,width=25,font=('arial 18 bold'),bg='white',fg="black")
        self.quantity_lede.place(x=190,y=410)
        self.quantity_lede.insert(END,0)

        self.add_btn=Button(self.left,text="Add to Cart",width=20,height=2,bg='green',fg='white',command=self.add_to_cart)
        self.add_btn.place(x=360,y=450)

        self.given_l=Label(self.left,text="Given Amount",font=('arial 18 bold'),bg='white',fg='black',)
        self.given_l.place(x=0,y=550)

        self.given_e=Entry(self.left,width=25,font=('arial 18 bold'),bg='white',fg="black")
        self.given_e.place(x=190,y=550)
        
        self.given_btn=Button(self.left,text="Calculate",font=('arial 15 bold'),bg='green',fg='white',command=self.change_f)
        self.given_btn.place(x=450,y=590)

        self.invoice_btn=Button(self.left,text="Create Invoice",font=('arial 18 bold'),bg='Orange',fg='white',command=self.generate_bill)
        self.invoice_btn.place(x=200,y=640)



    def add_to_cart(self,*args,**kwargs):
        self.quantity_value = int(self.quantity_lqe.get())
        if self.quantity_value > int(self.get_stock):
            tkinter.messagebox.showinfo("Error","Not sufficent Stocks")
        else:
            self.final_price=float(self.quantity_value)*float(self.get_price)-float(self.quantity_lede.get())
            product_name.append(self.get_name)
            product_amount.append(self.final_price)
            product_quantity.append(self.quantity_value)
            product_id.append(self.get_id)


            self.x_index=0
            self.y_index=100
            self.counter=0
            for self.p in product_name:
                self.tempname=Label(self.right,text=str(product_name[self.counter]),font=('arial 18 bold'),bg='lightblue',fg='white')
                self.tempname.place(x=0,y=self.y_index)
                label_lists.append(self.tempname)

                self.tempqt=Label(self.right,text=str(product_quantity[self.counter]),font=('arial 18 bold'),bg='lightblue',fg='white')
                self.tempqt.place(x=300,y=self.y_index)
                label_lists.append(self.tempqt)

                self.tempprice=Label(self.right,text=str(product_amount[self.counter]),font=('arial 18 bold'),bg='lightblue',fg='white')
                self.tempprice.place(x=450,y=self.y_index)
                label_lists.append(self.tempprice)

                self.y_index+=40
                self.counter+=1


                self.total_l.config(text="Total:₱"+str(sum(product_amount)))

                self.quantity_lq.place_forget()
                self.quantity_lqe.place_forget()
                self.quantity_lede.place_forget()
                self.quantity_led.place_forget()
                self.add_btn.place_forget()
                self.enteride.delete(0,END)



    def change_f(self,*args,**kwargs):
        self.amount_given= float(self.given_e.get())
        self.our_total=float(sum(product_amount))

        self.to_give=self.amount_given - self.our_total

        self.c_amount=Label(self.left,text="Change:₱"+str(self.to_give),font=('arial 18 bold'),fg='red',bg='cadet blue')
        self.c_amount.place(x=550,y=550)


    def generate_bill(self,*args,**kwargs):
        self.x=0
        intial="SELECT * FROM inventory WHERE id=?"
        result=c.execute(intial, (product_id[self.x], ))
        for i in product_name:
            for r in result:
                self.old_stock=r[2] 
            self.new_stock=int(self.old_stock)-int(product_quantity[self.x])

            sql="UPDATE inventory SET stock=? WHERE id=?"
            c.execute(sql,(self.new_stock,product_id[self.x]))
            conn.commit()

            #sql_2="INSERT INTO transactions (product_namel, quantity, amount, date) VALUES (?,?,?,?)"
            #c.execute(sql_2(product_name[self.x],product_quantity[self.x],product_amount[self.x],date))
            conn.commit()
            print("Decreased")
            self.x+=1

        for a in label_lists:
            a.destroy()
        del(product_name[:])
        del(product_quantity[:])
        del(product_quantity[:])
        del(product_amount[:])

        self.total_l.config(text="")
        self.c_amount.config(text="")
        self.given_e.delete(0,END)
        self.enteride.delete(0,END)
        tkinter.messagebox.showinfo("Sucess","Transaction Complete")

        


root=Tk()
root.title(" INVENTORY MANAGEMENT")
b=Application(root)
root.geometry("1366x768")
root.mainloop()
