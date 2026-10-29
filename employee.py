from tkinter import *
from tkinter import ttk
from tkinter import simpledialog,messagebox
import mysql.connector
#database connection
connection = mysql.connector.connect(host='localhost',user='root',passwd='',database='rythm')
cursor=connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Employee_details(
    ID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Designation VARCHAR(150) NOT NULL,
    Department VARCHAR(150) NOT NULL,
    Salary FLOAT
)
''')
connection.commit

#function to insert data 
def create():
    try:
        Id=eid.get()
        Name=ename.get()
        des=designation.get()
        dep=department.get()
        Salary=salary.get()
        
        if not Id or not Name or not des or not dep or not salary:
            status_label.config(text="all fields are required",fg="red")
            return
            
        Id=int(Id)
        try:
            Salary=float(Salary)
        except:
            status_label.config(text="invalid salary",fg="red")
            return
            
        sql="insert into Employee_details (ID,Name,Designation,Department,Salary) values(%s,%s,%s,%s,%s)"
        val=(Id,Name,des,dep,Salary)
        cursor.execute(sql,val)
        connection.commit()
        status_label.config(text="employee added sucessfully",fg = "red")
            
        eid.delete(0,END)
        ename.delete(0,END)
        designation.delete(0,END)
        department.delete(0,END)
        salary.delete(0,END)
                            
    except Exception as e:
        if "duplicate" in str(e):
            status_label.config(text="id already exist",fg="red")
        else:
            status_label.config(text=f"Error:{e}",fg="red")
def display():
    cursor.execute("select * from Employee_details")
    result=cursor.fetchall()
    if not result:
        status_label.config(text="employee not found",fg='red')
    else:
        text=""
        for i in result:
            text += f"Id={i[0]} name={i[1]} designation = {i[2]} department = {i[3]} salary = {i[4]}\n"
        status_label.config(text=text,fg='red')
def search_by(event):
    choice=combo_box.get()
    if choice=="Search by id":
        value=simpledialog.askstring("Fahhhh","enter id = ")
        column="ID"
    elif choice=="Search by name":
        value=simpledialog.askstring("Fahhhh","enter name = ")
        column="Name"
    elif choice=="Search by Designation":
        value=simpledialog.askstring("Fahhhh","enter designation = ")
        column="Designation"
    elif choice=="Search by Department":
        value=simpledialog.askstring("Fahhhh","enter department = ")
        column="Department"
    elif choice=="Search by Salary":
        value=simpledialog.askstring("Fahhhh","enter salary = ")
        column="Salary"
    else : 
        return
    if value is None:
        return

    query = f"select * from Employee_details where {column} = %s"
    val=(value,)
    cursor.execute(query,val)
    rows=cursor.fetchall()
    if not rows:
        status_label.config(text=f"{column} not found",fg="red")
    else:
        text =""
        for i in rows:
            text += f"Id={i[0]} name={i[1]}"
        status_label.config(text=text,fg='red')
def delete():
    emp_id=simpledialog.askstring("delete","enter id you want to delete")
    sql="delete from Employee_details where ID=%s"
    val=(emp_id,)
    cursor.execute(sql,val)
    connection.commit()
    if cursor.rowcount>0:
        status_label.config(text="employee delete sucesfully",fg="red")
    else:
        status_label.config(text="no employee found with that id",fg="red")
def update():
    emp_detail=simpledialog.askstring("update","enter value")
    if emp_detail is None:
        return
    column = simpledialog.askstring("update","details belong to which column")
    if column is None:
        return 
    if column not in ["ID","Name","Designation","Department","Salary"] :
        status_label.config(text="invalid search column",fg="red")
        return
    field=simpledialog.askstring("update","which column to update")
    if field is None:
        return 
    if field not in ["ID","Name","Designation","Department","Salary"] :
        status_label.config(text="invalid field",fg="red")
        return
    new_value=simpledialog.askstring("update",f"enter new{field}")
    if new_value is None:
        return
    sql = f"update Employee_details set {field}=%s where {column} = %s"
    val = (new_value,emp_detail)
    cursor.execute(sql,val)
    connection.commit()
    if cursor.rowcount==0:
        status_label.config(text="record not found",fg="red")
    else:
        status_label.config(text=f"{field} updates sucessfully",fg="red")
def on_closing():
    cursor.close()
    connection.close()
    root.destroy()
#GUI
root=Tk()
root.geometry("400x400")
root.title("Employee Management system")
root.config(bg="black")

Label(root, text="Employee ID : ", bg="black", fg="white").grid(row=0, column=0, pady=5)
Label(root, text="Employee Name : ", bg="black", fg="white").grid(row=1, column=0, pady=5)
Label(root, text="Designation : ", bg="black", fg="white").grid(row=2, column=0, pady=5)
Label(root, text="Department : ", bg="black", fg="white").grid(row=3, column=0, pady=5)
Label(root, text="Salary : ", bg="black", fg="white").grid(row=4, column=0, pady=5)

eid=Entry(root)
eid.grid(row=0,column=1)
ename=Entry(root)
ename.grid(row=1,column=1)
designation=Entry(root)
designation.grid(row=2,column=1)
department=Entry(root)
department.grid(row=3,column=1)
salary=Entry(root)
salary.grid(row=4,column=1)

button1=Button(root,text="add employee",width=25,activebackground="blue",activeforeground="white",command=create)
button1.grid(row=6,column=0,columnspan=2,pady=10)

button2=Button(root,text="display",width=25,activebackground="blue",activeforeground="white",command = display)
button2.grid(row=7,column=0,columnspan=2,pady=10)

combo_box=ttk.Combobox(root,values=["Search by id","Search by name","Search by designation","Search by Department","Search by Salary"],state="read only",width=28)
combo_box.grid(row=9,column=0,columnspan=3)
combo_box.set("Search by id")
combo_box.bind("<<ComboboxSelected>>",search_by)

button3=Button(root,text="update",width=25,activebackground="blue",activeforeground="white",command=update)
button3.grid(row=10,column=0,columnspan=2,pady=10)

button4=Button(root,text="delete",width=25,activebackground="blue",activeforeground="white",command=delete)
button4.grid(row=11,column=0,columnspan=2,pady=10)

status_label=Label(root,text="",fg="red",bg="pink",wraplength=350)
status_label.grid(row=14,column=0,columnspan=2)
root.protocol("WM_DELETE_WINDOW",on_closing)
root.mainloop()