from tkinter import *
from prettytable import PrettyTable
import os
from fpdf import *

root = Tk()
root.title('Shakti General Store')
#root.iconbitmap('c:/icon.png')
root.geometry("800x600")

global n
n=1
class code :
    
    def __init__(self,master):
        self.Total_list = []
        self.Quantity_list = []
        self.Name_list = []
        self.Price_list = []
        self.Total_price_list = []
        self.label1 = Label(master, text="Item Quantity")
        self.label2 = Label(master, text="Item Name")
        self.label3 = Label(master, text="Item Price")
        self.label4 = Label(master, text="Total Price")
        self.label1.grid(row=0, column=0)
        self.label2.grid(row=0, column=1)
        self.label3.grid(row=0, column=3)
        self.label4.grid(row=0, column=4)
        self.button_total = Button(master, text="",padx=5, command=self.compute)
        self.button_total.grid(row=1, column=5) 
        self.button_exit = Button(master, text="Print", padx=35, command=self.file_write)
        self.button_exit.grid(row=3, column=6)
        self.button_exit = Button(master, text="Total", padx=35, command=self.total)
        self.button_exit.grid(row=4, column=6)
        master.bind('<Return>', self.compute)
        self.entry()
    def entry(self):
        global n
        self.entry1 = Entry(root,width=10,borderwidth=2)
        self.entry2 = Entry(root,width=30,borderwidth=2)
        self.entry3 = Entry(root,width=10,borderwidth=2)
        self.entry4 = Entry(root,width=10,borderwidth=2)
        self.entry1.grid(row=n, column=0)
        self.entry2.grid(row=n, column=1)
        self.entry3.grid(row=n, column=3)
        self.entry4.grid(row=n, column=4)
        n+=1
        
    def compute(self,event=None):
        global num, num1
        #Total_list = []
        num = self.entry1.get()
        num1 = self.entry3.get()
        self.entry4.delete(0, END)
        Total = int(num) * int(num1)
        self.entry4.insert(0, Total)
        self.Total_list.append(Total)

        Quantity = self.entry1.get()
        Name = self.entry2.get()
        Price = self.entry3.get()
        Total_price = self.entry4.get()
        self.Quantity_list.append(Quantity)
        self.Name_list.append(Name)
        self.Price_list.append(Price)
        self.Total_price_list.append(Total_price)

        self.entry()   

    def total(self):
        global sum
        sum=0
        for i in self.Total_list:
            sum+=int(i)
        self.entry5 = Entry(root,width=15,borderwidth=2)
        self.entry5.grid(row=5, column=6)
        self.entry5.delete(0, END)
        self.entry5.insert(0,sum)

    def file_write(self):
        # pdf = FPDF(format='letter')
        # pdf.add_page()
        # pdf.set_font("Arial", size=12)
        # pdf.write(5,"{:<12} {:<10} {:<8} {:<10}\n".format('Quantity','Name','Price','Total'))
        # for i in range(len(self.Quantity_list)):
        #     pdf.write(5,"{:<15} {:<15} {:<10} {:<15}".format(self.Quantity_list[i],self.Name_list[i],self.Price_list[i],self.Total_price_list[i]))
        #     pdf.ln()
        # pdf.write(5,"\nTotal Amount = {:<12}".format(str(sum)))
        # pdf.output("Bill.pdf")

        f=open("Bill.txt",'w')
        length = len(self.Quantity_list)
        f.write("{:<15} {:15} {:<10} {:<10}".format('Item_Quantity','Item_Name','Item_Price','Total_Price'))
        for i in range(length):
            f.write("\n{:<15} {:<15} {:<10} {:<10}".format(self.Quantity_list[i],self.Name_list[i],self.Price_list[i],self.Total_price_list[i]))
        f.write("\n\nTotal = \t%s"% str(sum))
        f.close() 
        
myclass = code(root)
root.mainloop()