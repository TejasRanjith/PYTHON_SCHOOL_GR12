import pickle as pk
import os,decimal
from prettytable import PrettyTable

def create_file():
    with open("exhibition.dat","wb") as f:
        pk.dump('abcdefghijklmnopqrstuvwxyz',f)

def read_file():
    l = []
    with open("exhibition.dat","rb") as f:
        try:
            while True:
                data = pk.load(f)
                l.append(data)
        except EOFError:
            pass
        # l.pop(0)
        return l

def del_file():
    with open("exhibition.dat","wb") as f:
        os.remove(f)        

def add_rec():
    print("\n<-- ADD_RECORD -->\n")
    with open("exhibition.dat","ab") as f:
        while True:
            stall = input("Stall No. : ")
            comp = input("Company Name : ")
            cont = input("Contact No. : ")
            emirate = input("Emirate : ")
            rec = [stall,comp,cont,emirate]
            pk.dump(rec,f)
            ch = input("\n Do you want to add any more records ? (Y/N) --> ")
            if ch not in "Yy":
                break

def display():
    l,t = read_file(),PrettyTable()
    if len(l) == 0:
        print("No Details found to display. Please try adding records to the file.")
    else:
        t.field_names = ["StallNo.","Company Name","Contact No","Emirate"]
        t.add_rows(l)
        print(t)

def disp_choice():
    display = []
    l = ["AUD","DXB","SHJ","AJM","UAQ","RAK","FUJ"]
    names = ["Abu Dhabi","Dubai","Sharjah","Ajman","Umm Al Quwain","Ras Al Khaimah","Fujairah"]
    print("\n    EMIRATES :\n")
    for i in range(len(l)):
        print(f"{i+1}.) {names[i]} --> {l[i]}")
    i = int(input("\nYour Choice : "))
    data = read_file()
    for elem in data:
        if elem[-1] == l[i-1]:
            display.append(elem)
    if len(display) == 0:
        print(f"No books found belonging to the emirate, {names[i-1]}.")
    else:

        t = PrettyTable()
        t.field_names = ["StallNo.","Company Name","Contact No","Emirate"]
        t.add_rows(display)
        print(t)

def update_rec():
    l = read_file()
    display()
    no = input("\nPlease mention the stall no. of which you want to update the contact number : ")
    for elem in l:
        if elem[0] == no:
            print("\nPrevious contact number :",elem[2])
            contact = input("\nYou new contact number : ")
            elem[2] = contact
    with open("exhibition.dat","wb") as f:
        for rec in l:
            pk.dump(rec,f)

while True:
    print("\n<<---- MENU ---->>\n")
    print("Please go through the following options : \n")
    print("To Append records to file                                --> a")
    print("To Display all details                                   --> d")
    print("To Display book details by Emirate of user’s choice      --> e")
    print("To Update the Contact number.                            --> u")
    print("To exit the program                                      --> 0")
    opt = input("\nYour Choice : ").lower()
    if opt == "a":
        add_rec()
    elif opt == "d":
        display()
    elif opt == "e":
        disp_choice()
    elif opt == "u":
        update_rec()
    elif opt == "0":
        print("Thank you for using the program.")
        break
    else:
        print("Invalid option...")
