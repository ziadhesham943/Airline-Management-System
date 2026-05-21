import tkinter as tk
import pymysql
from tkinter import messagebox

class airline():
    def __init__(self,root):
        self.root = root
        self.root.title("Airlines Management")

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()

        self.root.geometry(f"{self.width}x{self.height}+0+0")

        titleLabel= tk.Label(self.root,text="Airlines Management System",bg="light green",bd=3,relief="groove", font=("Arial", 50,"bold"))
        titleLabel.pack(side="top", fill="x")

        mainFrame = tk.Frame(self.root, bg="sky blue", bd=4, relief="ridge")
        mainFrame.place(x=80, y=100, width=self.width/3, height=self.height-180)

        fNoLbl= tk.Label(mainFrame,text="Flight No:",bg="sky blue", font=("Arial",15))
        fNoLbl.grid(row=0,column=0,padx=10,pady=30)
        self.fNoIn = tk.Entry(mainFrame,bd=2, width=18,font=("Arial",15))
        self.fNoIn.grid(row=0,column=1, padx=10, pady=30)

        nameLbl = tk.Label(mainFrame,text="Your Name:",bg="sky blue", font=("Arial",15))
        nameLbl.grid(row=1, column=0,padx=10, pady=30)
        self.nameIn = tk.Entry(mainFrame,bd=2, width=18,font=("Arial",15))
        self.nameIn.grid(row=1,column=1, padx=10, pady=30)

        idLbl = tk.Label(mainFrame,text="Passport No:",bg="sky blue", font=("Arial",15))
        idLbl.grid(row=2, column=0, padx=10, pady=30)
        self.idIn = tk.Entry(mainFrame,bd=2, width=18,font=("Arial",15))
        self.idIn.grid(row=2,column=1, padx=10,pady=30)

        okBtn = tk.Button(mainFrame, text="OK",command=self.reserve, bg="gray", bd=2, font=("Arial",20,"bold"),width=20)
        okBtn.grid(row=3, column=0, padx=25, pady=50,columnspan=2)

        # list frame

        listFrame = tk.Frame(self.root, bg="light gray", bd=3, relief="ridge")
        listFrame.place(width=self.width/2, height=self.height-180,x=self.width/3+110,y=100)

        listLbl =tk.Label(listFrame, text="Available Flights",bg="light gray", font=("Arial",30,"bold"))
        listLbl.grid(row=0, column=0,padx=20, pady=20)
        self.list = tk.Listbox(listFrame,font=("Arial",20,"bold"),fg="white", width=39, height=12,bg="gray",bd=3, relief="sunken")
        self.list.grid(row=1,column=0, padx=20, pady=30)
        self.showFlight()

    def showFlight(self):
        con = pymysql.connect(host="localhost", user="root", passwd="12345678", database="db")
        cur = con.cursor()
        cur.execute("select * from airline")
        data = cur.fetchall()
        self.list.delete(0,tk.END)

        for i in data:
            self.list.insert(tk.END,i)
        cur.close()
        con.close()

    def reserve(self):
        f = int(self.fNoIn.get())
        name = self.nameIn.get()
        pNo = self.idIn.get()

        try:
            con = pymysql.connect(host="localhost", user="root", password="12345678", database="db", port=3306)
            cur = con.cursor()
            query= f"select amount,seats from airline where flightNo={f}"
            cur.execute(query)
            row = cur.fetchone()
            if row[1] >0:
                update = row[1]-1
                query2= f"update airline set seats={update} where flightNo={f}"
                cur.execute(query2)
                con.commit()

                line =f"Seat Reserved for {row[0]} in Flight No: {f}\n for Mr/Mrs.{name} with passport No: {pNo}"
                tk.messagebox.showinfo("Success",line)

                cur.execute("select * from airline")
                rows = cur.fetchall()
                self.list.delete(0,tk.END)
                
                for j in rows:
                    self.list.insert(tk.END,j)

                cur.close()
                con.close()
            else:
                tk.messagebox.showerror("Error","All seats are reserved")

        except Exception as e:
            tk.messagebox.showerror("Error",f"Error: {e}")


root = tk.Tk()
obj = airline(root)
root.mainloop()