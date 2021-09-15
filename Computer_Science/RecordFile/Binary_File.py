import pickle as pk
import os,decimal
from prettytable import PrettyTable

def create_file():
    with open("exhibition.dat","wb") as f:
        pk.dump('',f)
        # pk.dump(["a","1"],f)
        # pk.dump(["b","2"],f)
        # pk.dump(["c","3"],f)

def read_file():
    l = []
    with open("exhibition.dat","rb") as f:
        try:
            while True:
                data = pk.load(f)
                l.append(data)
        except EOFError:
            pass
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
            ch = input("\n Y/N ? --> ")
            if ch not in "Yy":
                break

def display():
    l,t = read_file(),PrettyTable()
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
        print(f"No books found belonging to the emirate, {names[i-1]}")
    else:

        t = PrettyTable()
        t.field_names = ["StallNo.","Company Name","Contact No","Emirate"]
        t.add_rows(display)
        print(t)

def update():
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
    print("<<---- MENU ---->>")
    opt = input("Your Choice : ")
    
