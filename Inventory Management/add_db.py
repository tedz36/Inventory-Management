from tkinter import *
import tkinter.messagebox
import sqlite3
import tkinter.ttk as ttk

conn=sqlite3.connect("/home/bokerns/Desktop/Inventory Management/Database/data.db")
c=conn.cursor()
result=c.execute("SELECT MAX(id)from inventory")
for r in result:
    id=r[0]

class Database():
    def __init__(self,master,*args,**kwargs):
        self.master=master
        self.heading=Label(master, text="Add to the database",font=('arial 40 bold'),fg=('steelblue'))
        self.heading.place(x=400,y=0)
        
        self.name_l=Label(master,text="Enter Product Name",font=('arial 18 bold'))
        self.name_l.place(x=0,y=70)

        self.stock_l=Label(master,text="Enter Stocks",font=('arial 18 bold'))
        self.stock_l.place(x=0,y=120)

        self.cp_l=Label(master,text="Enter Cost Price",font=('arial 18 bold'))
        self.cp_l.place(x=0,y=170)

        self.sp_l=Label(master,text="Enter Sale Price",font=('arial 18 bold'))
        self.sp_l.place(x=0,y=220)

        self.vendor_l=Label(master,text="Enter Vendor Name",font=('arial 18 bold'))
        self.vendor_l.place(x=0,y=270)

        self.vendor_phone_l=Label(master,text="Enter Vendor Phone Number",font=('arial 18 bold'))
        self.vendor_phone_l.place(x=0,y=320)

        


        self.name_e=Entry(master,width=25,font=('arial 18 bold'))
        self.name_e.place(x=380,y=70)

        self.stock_e=Entry(master,width=25,font=('arial 18 bold'))
        self.stock_e.place(x=380,y=120)

        self.cp_e=Entry(master,width=25,font=('arial 18 bold'))
        self.cp_e.place(x=380,y=170)

        self.sp_e=Entry(master,width=25,font=('arial 18 bold'))
        self.sp_e.place(x=380,y=220)

        self.vendor_e=Entry(master,width=25,font=('arial 18 bold'))
        self.vendor_e.place(x=380,y=270)

        self.vendor_phone_e=Entry(master,width=25,font=('arial 18 bold'))
        self.vendor_phone_e.place(x=380,y=320)



        self.btn_add=Button(master,text="Add to Database",width=25,height=2,bg='steelblue',fg='white',command=self.get_items)
        self.btn_add.place(x=520,y=370)

        self.btn_clear=Button(master,text="Clear Entry",width=25,height=2,bg='lightpink',fg='white',command=self.clear_all)
        self.btn_clear.place(x=350,y=370)

        self.btn_clearl=Button(master,text="Clear Log",width=25,height=2,bg='lightgreen',fg='white',command=self.clear_log)
        self.btn_clearl.place(x=750,y=370)


        

        self.tbox=Text(master,width=68,height=18)
        self.tbox.place(x=750,y=70)
        self.tbox.insert(END,"Log \n\nID has reached up to:"+ str(id))

        #self.master.bind('<Return>',self.get_items)
        #self.master.bind('Up',self.clear_all)


    def get_items(self,*args,**kwargs):
        self.name=self.name_e.get()
        self.stock=self.stock_e.get()
        self.cp=self.cp_e.get()
        self.sp=self.sp_e.get()
        self.vendor=self.vendor_e.get()
        self.vendor_phone=self.vendor_phone_e.get()
        
        if self.name=="" or self.stock=="" or self.cp=="" or self.sp=="":
            tkinter.messagebox.showinfo("Error","Please fill all entries")
        else:
            self.totalcp=float(self.cp)* float(self.stock)
            self.totalsp=float(self.sp)* float(self.stock)
            self.assumed_profit=float(self.totalsp - self.totalcp)
            0
            sql= "INSERT INTO inventory(name,stock,cp,sp,totalcp,totalsp,assumed_profit,vendor,vendor_phoneno)VALUES(?,?,?,?,?,?,?,?,?)"
            c.execute(sql,(self.name,self.stock,self.cp,self.sp,self.totalcp,self.totalsp,self.assumed_profit,self.vendor,self.vendor_phone))
            conn.commit()
            self.tbox.insert(END,"\n\nInserted"+" "+ str(self.name)+" "+"into the database.")
            self.name_e.delete(0,END)

      
    def clear_all(self,*args,**kwargs):
        self.name_e.delete(0,END)
        self.stock_e.delete(0,END)
        self.cp_e.delete(0,END)
        self.sp_e.delete(0,END)
        self.vendor_e.delete(0,END)
        self.vendor_phone_e.delete(0,END)

    def clear_log(self,*args,**kwargs):
        self.tbox.delete(1.0,END)

        
        














root=Tk()
b=Database(root)

width = 1366
height = 768
root.geometry("%dx%d" % (width, height))
root.resizable(0, 0)
root.title(" Add to the database")
root.mainloop()
