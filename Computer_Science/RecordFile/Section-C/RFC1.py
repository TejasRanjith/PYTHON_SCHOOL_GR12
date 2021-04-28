def create():
    with open("Emirates.txt", "w") as f:
        for i in range(1, 8):
            data = input(f"{i}. Emirate --> ")
            f.write(data.capitalize()+"\n")

def timer(n):
    import time
    time.sleep(n)

def display():
    with open("Emirates.txt", "r") as f:
        for i in range(1, 8):
            print(f"{i}. "+f.readline())

def create_v():
    with open("File.txt", "w") as f:f.write('''abcdefghijklmnopqrstuvwxyz\nHi my name is Tejas\nI study in class 12-C''')

def v_count():
    c, v = 0, 0
    with open("File.txt", "r") as f:
        para = f.read().lower()
    for elem in para:
            if elem in ["a", "e", "i", "o", "u"]:
                v += 1
            elif elem.isalpha() == True:
                c += 1
            elif elem.isdigit() == True:
                pass
            else:
                pass
    return c, v

def w_count():
    with open("File.txt", "r") as f:
        print(len(f.read().replace("\n", " ").split(sep=" ")))

#! Main
while True:
    print("<<----  MENU  ---->>");print()
    print("1.) To Create a Text file 'Emirates' and enter the names of 7 Emirates --> ce")
    print("2.) To read the file 'Emirates', line by line --> re")
    print("3.) To count the number of vowels and consonants in present in the text file --> cv")
    print("4.) To count the number of the words in the text file --> cw");print();opt = input('Option --> ');opt = opt.lower()
    if opt in ["ce", "re", "cv", "cw"]:
        if opt == "ce":print();create();print("The file has been created......")
        elif opt == "re":display()
        elif opt == "cv":a,b = v_count();print(a,b)
        elif opt == "cw":(w_count())
        else:print("Invalid Option......")
    elif opt == "0":timer(3);print("Program exited with exit code 0");break
    else:print("Invalid Option......")