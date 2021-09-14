import pickle as pk
import os,texttable,decimal

def create_file():
    with open("exhibition.dat","wb") as f:
        pk.dump(["a","1"],f)
        pk.dump(["b","2"],f)
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

def table_display(headings,rows,footers):
    d,d1,list_rows = {},{},[]
    for a in range(0,len(rows)):
        d[a] = list(rows[a])
    for i in range(0,len(rows[0])):
        for k in d:
            d1[k] = d[k][i]
            list_rows.append(d1[k])
    new_list_rows,i = [],0
    while i < len(list_rows):
        new_list_rows.append(list_rows[i:i+(len(rows))])
        i+=len(rows)
    rows,list_rows = new_list_rows,[]
    max_lens = []
    for col in rows:
        max_len = 0
        for elem in col:
            if type(elem) == decimal.Decimal or type(elem) == int:
                elem = str(elem)
            if max_len <= len(elem):
                max_len=len(elem)+4
        max_lens.append(max_len)
        str_row=""
        for i in range(0,len(col)):
            if i < len(col)-1:
                str_row+=f"{col[i]}\n"
            elif i == len(col)-1:
                str_row+=f"{col[i]}"
        list_rows.append(str_row)
    max_lens_head,max_len_head = [],0
    for head in headings:
        if max_len_head <= len(head):
            max_len_head = len(head)
        max_lens_head.append(max_len_head)
    col_width = []
    for i in range(len(max_lens)):
        if max_lens_head[i] > max_lens[i]:
            col_width.append(max_lens_head[i])
        else:
            col_width.append(max_lens[i])
    t = texttable.Texttable()
    t.set_cols_width(col_width)
    t.add_rows([
        headings,
        list_rows,
        footers
    ])
    return t.draw()

def add_rec():
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
    l = read_file()
    print(table_display(["StallNo.","Company Name","Contact No","Emirate"],l,["-","-","-","-"]))

def disp_choice():
    l = ["AUD","DXB","SHJ","AJM","UAQ","RAK","FUJ"]
    names = ["Abu Dhabi","Dubai","Sharjah","Ajman","Umm Al Quwain","Ras Al Khaimah","Fujairah"]
    print("\n    EMIRATES :\n")
    for i in range(len(l)):
        print(f"{i+1}.) {names[i]} --> {l[i]}")
    emirate = int(input("\nYour Choice : "))


disp_choice()
# display()
# create_file()
# add_rec()
# l = read_file()
# print(l)
# read_file()