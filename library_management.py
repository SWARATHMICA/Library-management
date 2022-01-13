from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as ms
m=ms.connect('mysql.db')
#print("connected")

c=m.cursor()
#----------------------backend--------------------
#CREATING DATABASE
'''q_1 ='CREATE TABLE books (Sno VARCHAR(30) PRIMARY KEY, Bookname VARCHAR(100), Authorname VARCHAR(100),DateOfPublication DATE,Description VARCHAR(500),NoOfTimesBorrowed VARCHAR(10), NoOfBooksInStock VARCHAR(10));'
q_2='CREATE TABLE users(NameOfUser VARCHAR(30),RegisterNumber VARCHAR(30) PRIMARY KEY, YearOfStudy VARCHAR(1), BookBorrowedDate DATE,Deadline DATE,Bookname VARCHAR(100));'
c.execute(q_1)
m.commit()
c.execute(q_2)
m.commit()'''
#INSERT (OR) READING
    
def insert_books(sno,bookname,authorname,DateOfPublication,description,NoOfTimesBorrowed,NoOfBooksInStock):
    c.execute('insert into books values(?,?,?,?,?,?,?);',(sno,bookname,authorname,DateOfPublication,description,NoOfTimesBorrowed,NoOfBooksInStock))
    m.commit()
    print("inserted in books")
    s='select * from books;'
    c.execute(s)
    '''r=c.fetchall()
    for i in r:
        print(r)'''
#insert_books('5',"radheshyamm","giridhar",'2022-01-08',"bhakthi",'2','20')
def insert_users(NameOfUser,RegisterNumber,YearOfStudy,BookBorrowedDate,Deadline,Bookname):
    c.execute('insert into users values(?,?,?,?,?,?);',(NameOfUser,RegisterNumber,YearOfStudy,BookBorrowedDate,Deadline,Bookname))
    m.commit()
    print("inserted in users")
    s='select * from users;'
    c.execute(s)
    '''r=c.fetchall()
    for i in r:
        print(r)'''
#PRINTING DATA
def fetch_books():
        c.execute("SELECT * from books")
        rows = c.fetchall()
        #print(rows)
        return rows
def fetch_users():
        c.execute("SELECT * from users")
        rows = c.fetchall()
        #print(rows)
        return rows
#DELETING DATA
def remove_books(bookname):
        c.execute("delete from books where bookname=?", (bookname,))
        m.commit()
def remove_users(RegisterNumber):
        c.execute("delete from books where RegisterNumber=?", (RegisterNumber,))
        m.commit()
#UPDATING DATA
def update_books(sno,bookname,authorname,DateOfPublication,description,NoOfTimesBorrowed,NoOfBooksInStock):
    c.execute("update books set authorname=?,dateofpublication=?,description=?,nooftimesborrowed=?,noofbooksinstock=? where sno=? and bookname=?",(authorname,DateOfPublication,description,NoOfTimesBorrowed,NoOfBooksInStock,sno,bookname))
    m.commit()
def update_users(NameOfUser,RegisterNumber,YearOfStudy,BookBorrowedDate,Deadline,Bookname):
    c.execute("update users set NameOfUser=?,YearOfStudy=?,BookBorrowedDate=?,Deadline=?,Bookname=?  where RegisterNumber=?",(NameOfUser,YearOfStudy,BookBorrowedDate,Deadline,Bookname,RegisterNumber))
    m.commit()

#----------------------frontend--------------------
#----------------------books--------------------

def getData_books(event):
    global row,tv
    selected_row = tv.focus()
    data = tv.item(selected_row)
    
    row = data["values"]
    #print(row)
    sno.set(row[0])
    bookname.set(row[1])
    authorname.set(row[2])
    DateOfPublication.set(row[3])
    description.set(row[4])
    NoOfTimesBorrowed.set(row[5])
    NoOfBooksInStock.set(row[6])
    




def add_book():
    global txtsno,txtbookname,txtauthorname,txtDateOfPublication,txtdescription,txtNoOfTimesBorrowed,txtNoOfBooksInStock
    if txtsno.get() == "" or txtbookname.get() == "" or txtauthorname.get() == "" or txtDateOfPublication.get() == "" or txtdescription.get() == "" or txtNoOfTimesBorrowed.get() == "" or txtNoOfBooksInStock.get() == "":
        messagebox.showerror("Error in Input", "Please Fill All the Details")
        return
    insert_books(txtsno.get(),txtbookname.get(), txtauthorname.get() , txtDateOfPublication.get() ,txtdescription.get(), txtNoOfTimesBorrowed.get(), txtNoOfBooksInStock.get())
    messagebox.showinfo("Success", "Record Inserted")
    clearAll_books()
    displayAll_books()



def books_update():
    global txtsno,txtbookname,txtauthorname,txtDateOfPublication,txtdescription,txtNoOfTimesBorrowed,txtNoOfBooksInStock
    if txtsno.get() == "" or txtbookname.get() == "" or txtauthorname.get() == "" or txtDateOfPublication.get() == "" or txtdescription.get() == "" or txtNoOfTimesBorrowed.get() == "" or txtNoOfBooksInStock.get() == "":
        messagebox.showerror("Error in Input", "Please Fill All the Details")
        return
    update_books(txtsno.get(),txtbookname.get(), txtauthorname.get() , txtDateOfPublication.get() ,txtdescription.get(), txtNoOfTimesBorrowed.get(), txtNoOfBooksInStock.get())
    messagebox.showinfo("Success", "Record updated")
    clearAll_books()
    displayAll_books()


def delete_book():
    
    remove_book(row[0])
    clearAll_books()
    displayAll_books()


def clearAll_books():
    sno.set("")
    bookname.set("")
    authorname.set("")
    DateOfPublication.set("")
    description.set("")
    NoOfTimesBorrowed.set("")
    NoOfBooksInStock.set("")

 
def books():
    global txtsno,txtbookname,txtauthorname,txtDateOfPublication,txtdescription,txtNoOfTimesBorrowed,txtNoOfBooksInStock,tv
   
    lblsno = Label(entries_frame, text="sno", font=("Calibri", 16), bg="#535c68", fg="white")
    lblsno.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    txtsno = Entry(entries_frame, textvariable=sno, font=("Calibri", 16), width=30)
    txtsno.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    lblbookname = Label(entries_frame, text="bookname", font=("Calibri", 16), bg="#535c68", fg="white")
    lblbookname.grid(row=1, column=2, padx=10, pady=10, sticky="w")
    txtbookname = Entry(entries_frame, textvariable=bookname, font=("Calibri", 16), width=30)
    txtbookname.grid(row=1, column=3, padx=10, pady=10, sticky="w")

    lblauthorname = Label(entries_frame, text="authorname", font=("Calibri", 16), bg="#535c68", fg="white")
    lblauthorname.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    txtauthorname = Entry(entries_frame, textvariable=authorname, font=("Calibri", 16), width=30)
    txtauthorname.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    lblDateOfPublication = Label(entries_frame, text="Date Of Publication", font=("Calibri", 16), bg="#535c68", fg="white")
    lblDateOfPublication.grid(row=2, column=2, padx=10, pady=10, sticky="w")
    txtDateOfPublication = Entry(entries_frame, textvariable=DateOfPublication, font=("Calibri", 16), width=30)
    txtDateOfPublication.grid(row=2, column=3, padx=10, pady=10, sticky="w")

    lbldescription = Label(entries_frame, text="description", font=("Calibri", 16), bg="#535c68", fg="white")
    lbldescription.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    txtdescription = Entry(entries_frame, textvariable=description,font=("Calibri", 16),bg="#535c68", fg="white" )
    txtdescription.grid(row=3, column=1, padx=10, sticky="w")

    lblNoOfTimesBorrowed = Label(entries_frame, text="No Of Times Borrowed", font=("Calibri", 16), bg="#535c68", fg="white")
    lblNoOfTimesBorrowed.grid(row=3, column=2, padx=10, pady=10, sticky="w")
    txtNoOfTimesBorrowed = Entry(entries_frame, textvariable=NoOfTimesBorrowed, font=("Calibri", 16), width=30)
    txtNoOfTimesBorrowed.grid(row=3, column=3, padx=10, sticky="w")

    lblNoOfBooksInStock = Label(entries_frame, text="No Of Books In Stock", font=("Calibri", 16), bg="#535c68", fg="white")
    lblNoOfBooksInStock.grid(row=4, column=0, padx=10, pady=10, sticky="w")
    txtNoOfBooksInStock = Entry(entries_frame,textvariable=NoOfBooksInStock, width=30, font=("Calibri", 16))
    txtNoOfBooksInStock.grid(row=4, column=1,  padx=10, sticky="w")

    btnAdd = Button(btn_frame, command=add_book, text="Add", width=15, font=("Calibri", 16, "bold"), fg="white",
                bg="#16a085", bd=0).grid(row=0, column=0)
    btnEdit = Button(btn_frame, command=books_update, text="Update", width=15, font=("Calibri", 16, "bold"),
                 fg="white", bg="#2980b9",
                 bd=0).grid(row=0, column=1, padx=10)
    btnDelete = Button(btn_frame,command=delete_book, text="Delete", width=15, font=("Calibri", 16, "bold"),
                   fg="white", bg="#c0392b",
                   bd=0).grid(row=0, column=2, padx=10)
    
    
    displayAll_books()
def displayAll_books():
    global tv
    tree_frame = Frame(root, bg="#ecf0f1")
    tree_frame.place(x=0, y=480, width=1980, height=520)
    style = ttk.Style()
    style.configure("mystyle.Treeview", font=('Calibri', 18),
                rowheight=50)  # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
    tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7), style="mystyle.Treeview")
    tv.heading("1", text="Sno")
    tv.column("1", width=5)
    tv.heading("2", text="bookame")
    tv.heading("3", text="authorname")
    tv.column("3", width=5)
    tv.heading("4", text="date of publication")
    tv.column("4", width=10)
    tv.heading("5", text="description")
    tv.heading("6", text="no of times borrowed")
    tv.column("6", width=10)
    tv.heading("7", text="no of books in stock")
    tv['show'] = 'headings'
    tv.bind("<ButtonRelease-1>", getData_books)
    tv.pack(fill=X)
    tv.delete(*tv.get_children())
    for row in fetch_books():
        tv.insert("", END, values=row)

#----------------------users--------------------
        #NameOfUser,RegisterNumber,YearOfStudy,BookBorrowedDate,Deadline,Bookname
def getData_users(event):
    global row_1,tv_1
    selected_row = tv_1.focus()
    data = tv_1.item(selected_row)
    
    row_1 = data["values"]
    #print(row)
    NameOfUser.set(row_1[0])
    RegisterNumber.set(row_1[1])
    YearOfStudy.set(row_1[2])
    BookBorrowedDate.set(row_1[3])
    Deadline.set(row_1[4])
    Bookname.set(row_1[5])

def add_users():
    global txtNameOfUser,txtRegisterNumber,txtYearOfStudy,txtBookBorrowedDate,txtDeadline,txtBookname
    if txtNameOfUser.get() == "" or txtRegisterNumber.get() == "" or txtYearOfStudy.get() == "" or txtBookBorrowedDate.get() == "" or txtDeadline.get() == "" or txtBookname.get() == "":
        messagebox.showerror("Error in Input", "Please Fill All the Details")
        return
    insert_users(txtNameOfUser.get(),txtRegisterNumber.get(), txtYearOfStudy.get() , txtBookBorrowedDate.get() ,txtDeadline.get(), txtBookname.get())
    messagebox.showinfo("Success", "Record Inserted")
    clearAll_users()
    displayAll_users()

#NameOfUser,RegisterNumber,YearOfStudy,BookBorrowedDate,Deadline,Bookname
def users_update():
    global txtNameOfUser,txtRegisterNumber,txtYearOfStudy,txtBookBorrowedDate,txtDeadline,txtBookname
    if txtNameOfUser.get() == "" or txtRegisterNumber.get() == "" or txtYearOfStudy.get() == "" or txtBookBorrowedDate.get() == "" or txtDeadline.get() == "" or txtBookname.get() == "":
        messagebox.showerror("Error in Input", "Please Fill All the Details")
        return
    update_users(txtNameOfUser.get(),txtRegisterNumber.get(), txtYearOfStudy.get() , txtBookBorrowedDate.get() ,txtDeadline.get(), txtBookname.get())
    messagebox.showinfo("Success", "Record Inserted")
    clearAll_users()
    displayAll_users()

def delete_users():
    
    remove_users(row_1[0])
    clearAll_users()
    displayAll_users()


def clearAll_users():
    NameOfUser.set("")
    RegisterNumber.set("")
    YearOfStudy.set("")
    BookBorrowedDate.set("")
    Deadline.set("")
    Bookname.set("")

def displayAll_users():
    global tv_1
    tree_frame_1 = Frame(root, bg="#ecf0f1")
    tree_frame_1.place(x=0, y=480, width=1980, height=520)
    style = ttk.Style()
    style.configure("mystyle.Treeview", font=('Calibri', 18),
                rowheight=50)  # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
    tv_1 = ttk.Treeview(tree_frame_1, columns=(1, 2, 3, 4, 5, 6), style="mystyle.Treeview")
    #NameOfUser,RegisterNumber,YearOfStudy,BookBorrowedDate,Deadline,Bookname
    tv_1.heading("1", text="NameOfUser")
    tv_1.column("1", width=5)
    tv_1.heading("2", text="RegisterNumber")
    tv_1.column("2", width=5)
    tv_1.heading("3", text="YearOfStudy")
    tv_1.column("3", width=5)
    tv_1.heading("4", text="BookBorrowedDate")
    tv_1.column("4", width=10)
    tv_1.heading("5", text="Deadline")
    tv_1.heading("6", text="Bookname")
    tv_1.column("6", width=10)
    tv_1['show'] = 'headings'
    tv_1.bind("<ButtonRelease-1>", getData_users)
    tv_1.pack(fill=X)
    tv_1.delete(*tv_1.get_children())
    for row_1 in fetch_users():
        tv_1.insert("", END, values=row_1)
    
def users():
    #print("sri radhe")
    global txtNameOfUser,txtRegisterNumber,txtYearOfStudy,txtBookBorrowedDate,txtDeadline,txtBookname,tv_1
    lblNameOfUser = Label(entries_frame, text="NameOfUser", font=("Calibri", 16), bg="#535c68", fg="white")
    lblNameOfUser.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    txtNameOfUser = Entry(entries_frame, textvariable=NameOfUser, font=("Calibri", 16), width=30)
    txtNameOfUser.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    lblRegisterNumber = Label(entries_frame, text="RegisterNumber", font=("Calibri", 16), bg="#535c68", fg="white")
    lblRegisterNumber.grid(row=1, column=2, padx=10, pady=10, sticky="w")
    txtRegisterNumber = Entry(entries_frame, textvariable=RegisterNumber, font=("Calibri", 16), width=30)
    txtRegisterNumber.grid(row=1, column=3, padx=10, pady=10, sticky="w")

    lblYearOfStudy = Label(entries_frame, text="YearOfStudy", font=("Calibri", 16), bg="#535c68", fg="white")
    lblYearOfStudy.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    txtYearOfStudy = Entry(entries_frame, textvariable=YearOfStudy, font=("Calibri", 16), width=30)
    txtYearOfStudy.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    lblBookBorrowedDate = Label(entries_frame, text="BookBorrowedDate", font=("Calibri", 16), bg="#535c68", fg="white")
    lblBookBorrowedDate.grid(row=2, column=2, padx=10, pady=10, sticky="w")
    txtBookBorrowedDate = Entry(entries_frame, textvariable=BookBorrowedDate, font=("Calibri", 16), width=30)
    txtBookBorrowedDate.grid(row=2, column=3, padx=10, pady=10, sticky="w")

    lblDeadline = Label(entries_frame, text="Deadline", font=("Calibri", 16), bg="#535c68", fg="white")
    lblDeadline.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    txtDeadline = Entry(entries_frame, textvariable=Deadline,font=("Calibri", 16),bg="#535c68", fg="white" )
    txtDeadline.grid(row=3, column=1, padx=10, sticky="w")

    lblBookname = Label(entries_frame, text="Bookname", font=("Calibri", 16), bg="#535c68", fg="white")
    lblBookname.grid(row=3, column=2, padx=10, pady=10, sticky="w")
    txtBookname = Entry(entries_frame, textvariable=Bookname, font=("Calibri", 16), width=30)
    txtBookname.grid(row=3, column=3, padx=10, sticky="w")

    
    btnAdd = Button(btn_frame, command=add_users, text="Add", width=15, font=("Calibri", 16, "bold"), fg="white",
                bg="#16a085", bd=0).grid(row=0, column=0)
    btnEdit = Button(btn_frame, command=users_update, text="Update", width=15, font=("Calibri", 16, "bold"),
                 fg="white", bg="#2980b9",
                 bd=0).grid(row=0, column=1, padx=10)
    btnDelete = Button(btn_frame,command=delete_users, text="Delete", width=15, font=("Calibri", 16, "bold"),
                   fg="white", bg="#c0392b",
                   bd=0).grid(row=0, column=2, padx=10)
    
    
    displayAll_users()
#print(fetch_books(),'\n',fetch_users())
#insert_users("HAREKRISHNA","125156119","1",'2022-01-01','2022-01-05',"Radhe")
#insert_books("1125","HAREKRISHNA","radhe",'2022-01-01',"bhakthi","1000","10000")
#update_books("1125","harekrishna","sriradhe",'2022-01-08',"prem","2000","100000")
#remove_books("HAREKRISHNA")
#print(fetch_books())


#------------------main screen----------------
root = Tk()
root.title("Library Management System")
root.geometry("1920x1080+0+0")
root.config(bg="#2c3e50")
root.state("zoomed")

sno,bookname,authorname,DateOfPublication,description,NoOfTimesBorrowed,NoOfBooksInStock=StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
NameOfUser,RegisterNumber,YearOfStudy,BookBorrowedDate,Deadline,Bookname=StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()

entries_frame = Frame(root, bg="#535c68")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="Library Management System", font=("Calibri", 18, "bold"), bg="#535c68", fg="white")
title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")
btn_frame = Frame(entries_frame, bg="#535c68")
btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")
b_books = Button(btn_frame, command=books, text="books", width=100, font=("Calibri", 16, "bold"),
                   fg="white", bg="#c0392b",
                   bd=0).grid(row=200, column=100, padx=10)
b_user = Button(btn_frame, command=users, text="users", width=100, font=("Calibri", 16, "bold"), fg="white",
                  bg="#f39c12",
                  bd=0).grid(row=250, column=100, padx=10)
#displayAll_books()
#m.flush()


    
