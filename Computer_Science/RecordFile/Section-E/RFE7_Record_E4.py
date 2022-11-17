import mysql.connector as ms
from prettytable import PrettyTable
import os

mydb = ms.connect(user = "root",host = "localhost",
password = "Tejas@035611",database = "record_e4")
myc = mydb.cursor()

def add():
    roll = input("New Roll No. :")
    name = input("New Name     :")
    percent = input("New Percentage  :")
    sec = input("New Section  :")
    assign = input("New Assignment  :")
    try:
        myc.execute(f"insert into student values({roll},'{name}',{percent},'{sec}','{assign}');")
        print("\nRecord Saved......\n")
        mydb.commit()
    except:
        print("     RECORD NOT SAVED ! \nPlease try again....")
        mydb.rollback()

def display_by():
    myc.execute("select * from student order by assignment;")
    data = myc.fetchall()
    t = PrettyTable()
    t.field_names = ('Roll No.','Name','Percentage','Section','Assignment')
    for r in data:
        t.add_row(r)
    print(t)

def update_assign():
    roll = input("Roll No. : ")
    assign = input("New Assignment Status : ")
    myc.execute(f"update student set assignment = '{assign}' where rollno = {roll};")
    mydb.commit()
    print("Record Updated......\nchoose display option to see the updates.")

def delete():
    roll = input("Roll No. : ")
    myc.execute(f"delete from student where rollno = {roll};")
    mydb.commit()
    print("Record Deleted......\nchoose display option to see the updates.")

def display_all():
    myc.execute("select * from student;")
    data = myc.fetchall()
    t = PrettyTable()
    t.field_names = ('Roll No.','Name','Percentage','Section','Assignment')
    for r in data:
        t.add_row(r)
    print(t)

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

l_opt = ['a','dby','u','del','dall','cls','0']     
l_func = ["add()","display_by()","update_assign()","delete()","display_all()","os.system('cls')","opt_0()"]

d_menu = {
    'a':   'To Add an Student Record                        ',
    'dby': 'To Display by Assignment Status                 ',
    'u':   'To Update Assignment Status                     ',
    'del': 'To Delete a Student Record                      ',
    'dall':'To Display all Records in the form of a table   ',
}

while True:
    print('<<----  MENU  ---->>\n')
    for elem in d_menu:
        print('  '+d_menu[elem] + '  --> ' + elem)
    print('  To stop the main program                          --> 0\n')
    opt = input('Your Option -->').lower()
    print()
    if opt in l_opt:
        for elem in l_opt:
            if opt == elem:
                eval(l_func[l_opt.index(elem)])
    else:
        print('Invalid Option......')