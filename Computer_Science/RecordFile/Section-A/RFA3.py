def sum_elem(l):
    print(sum(l))

def max_min(l):
    print(max(l),min(l))

def sum_even(l):
    add = 0
    for elem in l:
        if elem % 2 == 0:
            add+=elem
    print(add)

def sum_odd(l):
    add = 0
    for elem in l:
        if elem % 2 != 0:
            add+=elem
    print(add)

while True:
    print("\n<<----    PYTHON PROGRAM FOR SPECIFIC TASKS    ---->>")
    print("Please go through the following options:\n")
    print("To display the sum of all elements in the list.            --> sum")
    print("To display Largest & Smallest Element in the list          --> maxmin")
    print("To display sum of even numbers in the list.                --> even")
    print("To display sum of odd numbers in the list.                 --> odd")
    print("To stop or exit the program                                --> 0\n")
    opt = input("Your Option --> ").lower()
    l = eval(input("\nYour List :"))
    print(l)
    if opt == "sum":
        sum_elem(l)
    elif opt == "maxmin":
        max_min(l)
    elif opt == "even":
        sum_even(l)
    elif opt == "odd":
        sum_odd(l)
    elif opt == "0":
        print("Thank you for using the program...")
        break
    else:
        print("Invalid Option....")

print("Press enter to exit the program ")
input()



#.y RECORD FILE - A.3
#.y Design a menu driven Python program that accepts a list of numbers from the user and
#.y a.      print("Displays the sum of all elements in the list.")
#.y b.      print("Displays Largest & Smallest Element in the list")
#.y c.      print("Displays sum of even numbers in the list.")
#.y d.      print("Displays sum of odd numbers in the list.")