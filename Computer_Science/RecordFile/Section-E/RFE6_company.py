import mysql.connector as ms
from prettytable import PrettyTable

mydb = ms.connect(user = "root",host = "localhost",
password = "Tejas@035611",database = "company")
myc = mydb.cursor()

def display():
    myc.execute("select * from employee;")
    data = myc.fetchall()
    print(myc.rowcount)
    t = PrettyTable()
    t.field_names = ('EMPNO','NAME','DEPT','SALARY')
    for r in data:
       t.add_row(r)
    print(t)

def addrecord():
    empno = input("Employee Number  :")
    name = input("Name             :")
    dept = input("Department       :")
    sal = input("Salary           :")
    try:
        myc.execute(f"insert into employee values({empno},'{name}','{dept}',{sal});")
        print("\nRecord Saved......\n")
        mydb.commit()
    except:
        print("     RECORD NOT SAVED ! \nPlease try again....")
        mydb.rollback()

def empdetails():
    emp = input("Employee Number :")
    myc.execute(f"select * from employee where empno={emp};")
    data = myc.fetchall()
    for row in data:
        if emp not in row:
            print("Employee not found")
        else:
            t = PrettyTable()
            t.field_names = ('EMPNO','NAME','DEPT','SALARY')
            for r in data:
                t.add_row(r)
            print(t) 
    
def changerecord():
    empno = input("Employee Number :")
    myc.execute(f"select * from employee where empno = {empno};")
    data = myc.fetchall()
    t = PrettyTable()
    t.field_names = ('EMPNO','NAME','DEPT','SALARY')
    for r in data:
       t.add_row(r)
    print("Data to be changed: ",t,sep = "\n")
    new_sal = input("New Salary     :")
    myc.execute(f"update employee set salary = '{new_sal}' where empno = '{empno}';")
    mydb.commit()
    print("Record Updated......\nchoose display option to see the updates.")

def delrecord():
    empno = input("Emplyee Number :")
    myc.execute(f"delete from employee where empno = '{empno}';")
    mydb.commit()
    print("Record has been succesfully deleted......")

def timer(n):
    import time
    time.sleep(n)

def opt_0():
    timer(1)
    print('\n'+'Thank you for using the program.'+'\n')
    timer(1)
    print('Hope to see you soon in program version 1.2.0'+'\n'+'\n')
    timer(1.5)
    print('Program exited with exit code 0'+'\n')
    exit()

if not mydb.is_connected():
    print("Connection Failed......\nTry again.....")


l_opt = ['d','a','det','c','del','0']     
l_func = ["display()","addrecord()","empdetails()","changerecord()","delrecord()",'opt_0()']

d_menu = {     
    'd':'To display the entire table                    ',
    'a':'To add an employee with his required details   ',
    'det':'To display details of a specified employee     ',
    'c':'To change the salary of an employee            ',
    'del':'To delete an employee from the table           '
}

# while True:
#     print('<<----  MENU  ---->>\n')
#     for elem in d_menu:
#         print('  '+d_menu[elem] + '  --> ' + elem)
#     print('  To stop the main program                         --> 0\n')
#     opt = input('Your Option -->').lower()
#     print()
#     if opt in l_opt:
#         for elem in l_opt:
#             if opt == elem:
#                 eval(l_func[l_opt.index(elem)])
#     else:
#         print('Invalid Option......')

display()