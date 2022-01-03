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
        for elem in S[::-1]:
            print(elem,end="\t")

while True:
    print("\n<<----MENU---->>\n")
    print("1.Push to the stack --> pu")
    print("2.Pop from the stack --> po")
    print("3.Display the stack --> d")
    print("4.Exit --> 0\n")
    opt = input("Enter your choice: ").lower()
    print("")
    if opt == "pu":
        val = input("Enter the item to be pushed: ")
        Push(S,val)
    elif opt == "po":
        Pop(S)
    elif opt == "d":
        Display(S)
    elif opt == "0":
        break
    else:
        print("Invalid option")