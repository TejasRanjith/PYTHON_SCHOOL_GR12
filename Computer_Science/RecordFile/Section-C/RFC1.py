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

def v_count():
    c, v = 0, 0
    with open("Emirates.txt", "r") as f:
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
    with open("Emirates.txt", "r") as f:
        return (len(f.read().replace("\n", " ").split(sep=" "))-1)


#! Main
while True:
    print("\n<<----  MENU  ---->>\n")
    print("2.) To read the file 'Emirates', line by line --> re")
    print("3.) To count the number of vowels and consonants in present in the text file --> cv")
    print("4.) To count the number of the words in the text file --> cw")
    print("5.) To stop the main program --> 0\n")
    opt = input('Option --> ')
    opt = opt.lower()
    if opt in ["re", "cv", "cw"]:
        print()
        if opt == "re":
            display()
        elif opt == "cv":
            a,b = v_count()
            print("Number of Vowels: ",b)
            print("Number of Consonants: ",a)
        elif opt == "cw":
            print("The Number of words in the file: ",w_count(),sep = "\n")
        else:
            print("Invalid Option......")
    elif opt == "0":
        timer(1)
        print("\n"+"Thank you for using the string modifier program."+"\n")
        timer(1)
        print("Hope to see you soon in string modifier program version 1.2.0"+"\n"+"\n")
        timer(1.5)
        print("Program exited with exit code 0"+"\n")
        break
    else:
        print("Invalid Option......")