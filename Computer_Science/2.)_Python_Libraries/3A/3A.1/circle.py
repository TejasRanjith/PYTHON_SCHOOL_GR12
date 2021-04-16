def area(r):
    return (22/7)*(r**2)


def cir(r):
    return 2*(22/7)*r


def timer(n):
    import time
    time.sleep(n)


def circle_calculator():
    while True:
        print()
        print("<<----  CIRCLE CALCULATOR  ---->>")
        print('''
        1.) To calculate the area of the circle ==>> ar
        2.) To calculate the circumference of the circle ==>> cir
        3.) To go back to the main calculator program ==>> 0
        ''')
        opt = input("Option --> ")
        opt = opt.lower()
        if opt in ["ar", "cir"]:
            try:
                r = int(input("Radius of the circle --> "))
            except ValueError:
                print("Please enter a number......")
                print("Taking you back to the main program.....")
                timer(2)
                break
            if opt == "ar":
                print("The area of the circle is", area(r))
            elif opt == "cir":
                print("The circumference of the circle is", cir(r))
            else:
                print("Invalid Option......")
        elif opt == "0":
            print("Taking you back to the main converter program.......")
            timer(2)
            break
        else:
            print("Invalid Option......")
