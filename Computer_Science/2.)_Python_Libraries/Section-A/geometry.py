import circle as c
import rectangle as r


def timer(n):
    import time
    time.sleep(n)


while True:
    print()
    print("<<----  CALCULATOR  ---->>")
    print('''
    1.) To open the rectangle calculator ==>> r
    2.) To open the circle calculator ==>> c
    3.) To stop the main program ==>> 0
    
    ''')
    opt = input("Your Option --> ")
    opt = opt.lower()
    if opt == "r":
        r.rectangle_calculator()
    elif opt == "c":
        c.circle_calculator
    elif opt == "0":
        timer(1)
        print("Thank you for using the calculator program.")
        print()
        timer(1)
        print("Hope to see you soon in calculator program version 1.2.0")
        timer(2.5)
        print()
        print()
        print("Program exited with exit code 0")
        print()
        break
    else:
        print("Invalid Option......")
