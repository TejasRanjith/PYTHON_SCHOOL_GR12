import csv,os,prettytable

def append():
    with open("store.csv","a",newline="") as f:
        w = csv.writer(f)
        a = input("Item No. --> ")
        b = input("Item Name --> ")
        c = input("Shelf No. --> ")
        w.writerow([a,b,c])
        print("Your Data has been added succesfully")

def display():
    t = ""
    with open("store.csv","r") as f:
        r,t = csv.reader(f),prettytable.PrettyTable()
        r,t.field_names = list(r),["Item No.","Item Name","Shelf No."]
        if len(r) != 0:
            for row in r:
                t.add_row(row)
            print("",t,sep="\n")
        else:
            print("\nNothing To display...")

def disp_shelf(): # display items of a shelf
    t,l = "",[]
    with open("store.csv","r") as f:
        r,n = csv.reader(f),input("Shelf No. --> ").upper()
        for row in r:
            if row[2] == n:
                l.append(row)
        if len(l) != 0:
            t = prettytable.PrettyTable()
            t.field_names = ["Item No.","Item Name","Shelf No."]
            for row in l:
                t.add_row(row)
            return "\nResult Found",t
        else:
            return "\nResult Not Found",t

def item_shelf(): # display shelf no. of a particular item
    with open("store.csv","r") as f:
        r,i = csv.reader(f),input("Item No. --> ")
        r = list(r)
        if len(r) != 0:
            for row in r:
                if row[0] == i:
                    return "Result found",f"Shelf No. : {row[-1]}"
                else:
                    display = "Result not found"
            return display,""
        else:
            return "\nNothing To display...",""

while True:
    print("\n<<----  MENU  ---->>\n")
    print("To add items to the database  -->  a")
    print("To display all items from the database  -->  d")
    print("To display items on a particular Shelf No.  -->  s")
    print("To display Shelf No of a particular item.  -->  i")
    print("To exit the main program  -->  0")
    opt = input("\nYour Option -->")
    if opt == "a":
        append()
    elif opt == "d":
        display()
    elif opt == "i":
        item = item_shelf()
        print(item[0])
        print(item[1])
    elif opt == "s":
        disp = disp_shelf()
        print(disp[0])
        print(disp[1])
    elif opt == "0":
        print("\nThank you for using the program.\n")
        break
    else:
        print("Invalid Option...")

input("Press enter to exit the program")
