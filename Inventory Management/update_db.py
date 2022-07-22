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
        self.heading=Label(master, text="Update database",font=('arial 40 bold'),fg=('steelblue'))
        self.heading.place(x=400,y=0)
        
        self.name_l=Label(master,text="Product Name",font=('arial 18 bold'))
        self.name_l.place(x=0,y=70)

        self.stock_l=Label(master,text="Stocks",font=('arial 18 bold'))
        self.stock_l.place(x=0,y=120)

        self.cp_l=Label(master,text="Cost Price",font=('arial 18 bold'))
        self.cp_l.place(x=0,y=170)

        self.sp_l=Label(master,text="Sale Price",font=('arial 18 bold'))
        self.sp_l.place(x=0,y=220)

        self.vendor_l=Label(master,text="Vendor Name",font=('arial 18 bold'))
        self.vendor_l.place(x=0,y=270)

        self.vendor_phone_l=Label(master,text="Vendor Phone Number",font=('arial 18 bold'))
        self.vendor_phone_l.place(x=0,y=320)

        self.totalcp_l=Label(master,text="Total Cost Price",font=('arial 18 bold'))
        self.totalcp_l.place(x=0,y=370)
        
        self.totalsp_l=Label(master,text="Total Sale Price",font=('arial 18 bold'))
        self.totalsp_l.place(x=0,y=420)

        self.id_le=Label(master,text="Enter ID",font=('arial 18 bold'))
        self.id_le.place(x=0,y=500)

        


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
        
        self.id_leb=Entry(master,width=25,font=('arial 18 bold'))
        self.id_leb.place(x=380,y=500)

        self.totalcp_e=Entry(master,width=25,font=('arial 18 bold'),state='disabled')
        self.totalcp_e.place(x=380,y=370)
        
        self.totalsp_e=Entry(master,width=25,font=('arial 18 bold'),state='disabled')
        self.totalsp_e.place(x=380,y=420)



        self.btn_add=Button(master,text="Update Database",width=25,height=2,bg='steelblue',fg='white',command=self.update)
        self.btn_add.place(x=520,y=600)

        self.btn_search=Button(master,text="Search",width=25,height=2,bg='lightgreen',fg='white',command=self.search)
        self.btn_search.place(x=750,y=500)

    def search(self,*args,**kwargs):
        sql="SELECT * FROM inventory WHERE id=?"
        result=c.execute(sql,(self.id_leb.get(),))
        for r in result:
            self.n1=r[1]#name
            self.n2=r[2]#stock
            self.n3=r[3]#cp
            self.n4=r[4]#sp
            self.n5=r[5]
            self.n6=r[6]
            self.n7=r[7]
            self.n8=r[8]
            self.n9=r[9]
        conn.commit()
        self.name_e.delete(0,END)
        self.name_e.insert(0,str(self.n1))
        self.stock_e.delete(0,END)
        self.stock_e.insert(0,str(self.n2))
        self.cp_e.delete(0,END)
        self.cp_e.insert(0,str(self.n3))
        self.sp_e.delete(0,END)
        self.sp_e.insert(0,str(self.n4))
        self.totalcp_e.delete(0,END)
        self.totalcp_e.config(state='normal')
        self.totalcp_e.insert(0,str(self.n5))
        self.totalcp_e.config(state='disabled')
        self.totalsp_e.delete(0,END)
        self.totalsp_e.config(state='normal')
        self.totalsp_e.insert(0,str(self.n6))
        self.totalsp_e.config(state='disabled')
        self.vendor_e.delete(0,END)
        self.vendor_e.insert(0,str(self.n8))
        self.vendor_phone_e.delete(0,END)
        self.vendor_phone_e.insert(0,str(self.n9))

    def update(self,*args,**kwargs):
        self.u1=self.name_e.get()
        self.u2=self.stock_e.get()
        self.u3=self.cp_e.get()
        self.u4=self.sp_e.get()
        self.u5=self.vendor_e.get()
        self.u6=self.vendor_phone_e.get()

        query= "UPDATE inventory SET name=?, stock=?, cp=?, sp=?, vendor=?, vendor_phoneno=? WHERE id=?"
        c.execute(query,(self.u1,self.u2,self.u3,self.u4,self.u5,self.u6,self.id_leb.get()))
        conn.commit
        tkinter.messagebox.showinfo("Success","Database Updated")

    


root=Tk()
b=Database(root)

width = 1366
height = 768
root.geometry("%dx%d" % (width, height))
root.resizable(0, 0)
root.title("Update database")
root.mainloop()
