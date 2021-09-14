def ChangeLine():
    with open("poem.txt","r") as f:
        data = f.readlines()
        for elem in data:
            if elem[0] == "T":
                print(elem.replace("T","#"))
                continue
            print(elem)

def ConvertCase():
    with open("poem.txt","r") as f:
        data = f.readlines()
        for elem in data:
            print(elem.swapcase())

def Replaceword():
    with open("poem.txt","r") as f:
        data = f.readlines()
        for elem in data:
            print(elem.replace("is","are"))

print("\n<<---- MENU ---->>\n")
print("To read above file and display all lines by replacing lines starting with T with #        --> rt")
print("To read above file and display lowercase with uppercase and vice-versa.                  --> sc")
print("To read above file and display by replacing all is with are .                            --> re")
print("")
while True:
    opt = input("\nYour option : ")
    print()
    if opt == "rt":
        ChangeLine()
    elif opt == "sc":
        ConvertCase()
    elif opt == "re":
        Replaceword()
    elif opt == "0":
        print("Thank you for using the program.\n")
        break
    else:
        print("Invalid Option....")