print("<<<<----   REPORT CARD MANAGEMENT PROGRAM   ---->>>>")
while 1==1:
    print('''
    Please read the options given below and provide it in the following input field :
    a: add data
    del: delete data
    d: display data
    0: to exit the program
    ''')
    opt = input("--->")
    opt = opt.lower()
    if opt == "a":
        n = int(input("Number of students --> "))
        for i in range(1,n+1):
            gr = input(" GR No. : ")
            name = input('name --> ')
            clas = input("class (grade,division format.)--> ")
            rollno = int(input("Roll No. --> "))

            math = int(input("Marks received for the subject Maths : "))
            phy = int(input("Marks received for the subject Physics: "))
            chem = int(input("Marks received for the subject Chemistry: "))
            eng = int(input("Marks received for the subject English: "))
            comp = int(input("Marks received for the subject Computer Science: "))
            main_dict = {}
            main_dict[gr] = [name,clas,rollno,math,phy,chem,eng,comp]    #  3,4,5,6,7
        print(f"Your {n} number/numbers of student data has been added.")
    elif opt == "del":
        pass
    elif opt == "d":
        from prettytable import PrettyTable
        table = PrettyTable()
        for k in main_dict:
            table.field_names = [k,main_dict[k][2],main_dict[k][1],main_dict[k][0],"Marks scored in Maths","Marks scored in Physics","Marks scored in Chemistry","Marks scored in English","Marks scored in Computer Science"]
            table.add_row([k] + main_dict[k])
        print(table)
    elif opt == "0":
        break