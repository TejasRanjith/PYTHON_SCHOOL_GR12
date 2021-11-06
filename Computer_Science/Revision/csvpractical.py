import csv
def create_file():
    with open("BOOKS.csv","w",newline="") as f:
        w = csv.writer(f)
        w.writerow(["BookNo.","Title","Cost"])

def add():
    with open("BOOKS.csv","a",newline="") as f:
        w = csv.writer(f)
        n = int(input("Number of Books to add : "))
        for i in range(n):
            no = input("Book No. : ")
            title = input("Title : ")
            cost = int(input("Cost : "))
            dat = [no,title,cost]
            w.writerow(dat)
            print("Data Added Succesfully...")

def disp():
    with open("BOOKS.csv","r") as f:
        r = csv.reader(f)
        for row in r:
            print(row[0],"\t\t",row[1],"\t\t",row[2])

def details():
    with open("BOOKS.csv","r") as f:
        r = csv.reader(f)
        no = input("Book No. : ")
        for row in r:
            if row[0] == no:
                print(row[0],"\t\t",row[1],"\t\t",row[2])

# create_file()

while True:
    print("\n<<----  MENU  ---->>\n")
    print("  To add records to the file  --> a")
    print("  To display the entire books --> d")
    print("  To display book details by providing book no. --> n")
    print("  To exit the main program --> 0")
    opt = input("\nYour option --> ").lower()
    if opt == "a":
        add()
    elif opt == "d":
        disp()
    elif opt == "n":
        details()
    elif opt == "0":
        print("Thank you for using the program...")
        break
    else:
        print("Invalid Option...")