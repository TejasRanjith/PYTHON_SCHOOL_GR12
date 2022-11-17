import time
S = []

def Push(S,item):
    S.append(item)

def Pop(S):
    if len(S) == 0:
        print("Stack is empty")
    else:
        print(S.pop())

def Display(S):
    if len(S) == 0:
        print("Stack is empty")
    else:
        for tup in S[::-1]:
            for elem in tup:
                print(elem,end="\t")
            print("")

while True:
    print("\n<<---- ITEM DETAILS ---->>\n")
    print("1.Push to the stack --> pu")
    print("2.Pop from the stack --> po")
    print("3.Display the stack --> d")
    print("4.Exit --> 0\n")
    opt = input("Enter your choice: ").lower()
    print()
    if opt == "pu":
        ino = int(input("Enter the item number: "))
        iname = input("Enter the item name: ")
        cost = float(input("Enter the cost of the item: "))
        item = [ino,iname.title(),cost]
        Push(S,item)
    elif opt == "po":
        Pop(S)
    elif opt == "d":
        Display(S)
    elif opt == "0":
        print("Thank you for using the Item Details program")
        print("Exiting the program...")
        time.sleep(3)
        break
    else:
        print("Invalid option") 