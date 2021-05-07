import pickle,time,os
from prettytable import PrettyTable

def timer(n):
    time.sleep(n)

def append():
    print("Taking you to ADD STUDENT program......")
    timer(1.5)
    print("\n<<----  ADD STUDENT  ---->>")
    with open("Students.dat","ab") as f:
        while True:
            print("\nStudent Info\n")
            a = input("Student Roll Number      :")
            b = input("Name of the Student      :")
            c = int(input("Marks Obtained           :"))
            rec = [a,b,c]
            pickle.dump(rec,f)
            ch = input("Do you want to add any more Students? Y/N ?")
            if ch not in "Yy":
                break

def display():
    t = PrettyTable()
    t.field_names = ["Roll Number","Name","Marks"]
    with open("Students.dat","rb") as f:
        try:
            while True:
                data = pickle.load(f)
                t.add_row(data)
        except EOFError:
            pass
    print(t,"",sep="\n")

def marks_75():
    t = PrettyTable()
    t.field_names = ["Roll Number","Name","Marks"]
    f = open("Students.dat","rb")
    try:
        while True:
            data = pickle.load(f)
            if data[-1] > 75:
                t.add_row(data)
    except EOFError:
        pass
    f.close()
    print(t,"",sep="\n")

def update():
    f,n = open("Students.dat","rb"),open("new.dat","ab")
    r = input("Roll Number of the Student --> ")
    name,marks = input("\nUpdated Name --> "),int(input("\nUpdated Marks --> "))
    try:
        while True:
            data = pickle.load(f)
            if r == data[0]:
                data[-1],data[1] = marks,name
            pickle.dump(data,n)
    except EOFError:
        pass
    f.close()
    n.close()
    print("\nName and Marks Updated. Please select display option to see the changes")
    os.remove("Students.dat")
    os.rename("new.dat","Students.dat")

def delete():
    f,n = open("Students.dat","rb"),open("new.dat","wb")
    r = input("Roll Number of the Student --> ")
    try:
        while True:
            data = pickle.load(f)
            if r == data[0]:
                print("Student has been deleted")
            else:
                pickle.dump(data,n)
    except EOFError:
        pass
    f.close()
    n.close()
    os.remove("Students.dat")
    os.rename("new.dat","Students.dat")

def opt_0():
    timer(1)
    print("\n"+"Thank you for using the program."+"\n")
    timer(1)
    print("Hope to see you soon in program version 1.2.0"+"\n"+"\n")
    timer(1.5)
    print("Program exited with exit code 0"+"\n")
    exit()

l_opt= ["a","d","m","u","del","cmd","cls","stop","0"]
l_func= ["append()","display()","marks_75()","update()","delete()",
"os.system(input('CMD ❯'))","os.system('cls')","exit()","opt_0()"]
while True:
    print("<<----  MENU  ---->>\n")
    print("   To add a Student's details                               -->  a")
    print("   To display all the Students with their information       -->  d")
    print("   To display the Student's details whose mark is above 75  -->  m ")
    print("   To update the name and marks of a specified student      -->  u")
    print("   To delete a particular student info.                     -->  del")
    print("   To stop the main program                                 -->  0\n")
    opt = input("Your Option --> ").lower()
    print()
    if opt in l_opt:
        for elem in l_opt:
            if opt == elem:
                eval(l_func[l_opt.index(elem)])
    else:
        print("Invalid Option......")
