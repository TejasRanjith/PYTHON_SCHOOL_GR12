import mysql.connector  as ms
from prettytable import PrettyTable
mydb = ms.connect(user = "root",host = "localhost",
password = "Tejas@035611",database = "assignment")
myc = mydb.cursor()
def add():
    myc.execute("select * from Student;")
    t = PrettyTable()
    t.field_names = ("RollNo","Name","Percentage","Section","Assignment")
    for r in myc.fetchall():
       t.add_row(r)
    print(t)
    rollno = input("Roll No.      :")
    name = input("Name          :")
    per = input("Percentage    :")
    sect = input("Section       :")
    a = input("Assignment    :")
    try:
        myc.execute(f'''insert into Student values
        ({rollno},'{name}','{per}','{sect}','{a}');''')
        mydb.commit()
        print("Record Saved....")
    except:
        mydb.rollback()
        print("     RECORD NOT SAVED ! \nPlease try again....")

def display_by():
    status = input("Status to be displayed (Pending,Submitted,Evaluated) :")
    myc.execute(f"select RollNo,Name,Section from Student where Assignment = '{status}';")
    t = PrettyTable()
    t.field_names = ("RollNo","Name","Section")
    for r in myc.fetchall():
       t.add_row(r)
    print(t)

def update():
    rollno = input("Roll no. of student to be updated                   :")
    status = input("Status to be updated (Pending,Submitted,Evaluated)  :")
    myc.execute(f"update Student set Assignment = '{status}' where RollNo = {rollno};")
    mydb.commit()
    print("\n   Select display option to see the changes....")

def delete():
    rollno = input("Roll no. of student to be deleted :")
    myc.execute(f"delete from Student where RollNo = {rollno};")
    mydb.commit()
    print("Record Succesfully deleted....")

def display_all():
    myc.execute("select * from Student;")
    t = PrettyTable()
    t.field_names = ("RollNo","Name","Percentage","Section","Assignment")
    for r in myc.fetchall():
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

l_func = ["add()","display_by()","update()","delete()","display_all()",'opt_0()']     
l_opt = ["a","dby","u","del","dall",'0']    
d_menu = {     
    'a'     :"To add a record to the table with the required information    ",
    "dby"   :"To display by the status of the assignment                    ",
    "u"     :"To update the status of the assignment                        ",
    "del"   :"To delete a record from the table                             ",
    "dall"  :"To display the entire table                                   "
}
while True:
    print('<<----  MENU  ---->>\n')
    for elem in d_menu:
        print('  '+d_menu[elem] + '  --> ' + elem)
    print('  To stop the main program                                        --> 0\n')
    opt = input('Your Option -->').lower()
    print()
    if opt in l_opt:
        for elem in l_opt:
            if opt == elem:
                eval(l_func[l_opt.index(elem)])
    else:
        print('Invalid Option......')