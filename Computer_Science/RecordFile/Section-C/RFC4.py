import pickle,os

def timer(n):
    import time
    time.sleep(n)

def app():
    print("Taking you to ADD EMPLOYEE program......")
    timer(1.5)
    print("\n<<----  ADD EMPLOYEE  ---->>\n")
    with open("Employees.dat","ab") as f:
        while True:
            print("Employee Info\n")
            a = input("Employee ID Number   : ")
            b = input("Name                 : ")
            c = input("Designation          : ")
            d = int(input("Salary               : "))
            rec = [a,b,c,d]
            pickle.dump(rec,f)
            ch = input("\nDo you want to add any more employees? Y/N ? --> ")
            if ch not in "Yy":
                break

def display():
    f=open('Employees.dat','rb')
    print("The whole list of Employees with their information......\n")
    try:
        while True:
            data = pickle.load(f)
            print(data)
    except EOFError:
        pass
    f.close()

def search():
    f=open('Employees.dat','rb')
    no = input("ID Number of the Employee --> ")
    try:
        while True:
            data = pickle.load(f)
            if no == data[0]:
                print("",f"The information of employee, {no}:",data,sep="\n")
    except EOFError:
        pass
    f.close()

def update():
    f=open('Employees.dat','rb')
    n=open("new.dat","ab")
    no = input("ID Number of the Employee --> ")
    sal = int(input("\nUpdated Salary --> "))
    try:
        while True:
            data = pickle.load(f)
            if no == data[0]:
                data[-1] = sal
            pickle.dump(data,n)
    except EOFError:
        pass
    f.close()
    n.close()
    print("\nSalary Updated. Please select display option to see the changes.")
    os.remove("Employees.dat")
    os.rename("new.dat","Employees.dat")

def opt_0():
    timer(1)
    print("\n"+"Thank you for using the program."+"\n")
    timer(1)
    print("Hope to see you soon in program version 1.2.0"+"\n"+"\n")
    timer(1.5)
    print("Program exited with exit code 0"+"\n")
    exit()

l_opt,l_func = ["a","d","s","u","cmd","cls","stop","0"],["app()","display()","search()","update()","os.system(input('CMD ❯'))","os.system('cls')","exit()","opt_0()"]
while True:
    print("<<----  MENU  ---->>\n")
    # print("1.) To create the file or overwrite the file       --> c")
    print("  To add an Employee                                 --> a")
    print("  To display the entire list                         --> d")
    print("  To search for an Employee                          --> s")
    print("  To update the salary of a specified Employee       --> u")
    print("  To stop the main program                           --> 0\n")
    opt = input("Your Option --> ").lower()
    if opt in l_opt:
        for elem in l_opt:
            if opt == elem:
                print()
                eval(l_func[l_opt.index(elem)])
                print()
    else:
        print("Invalid Option......")
