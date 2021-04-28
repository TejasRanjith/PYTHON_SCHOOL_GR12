def area(l, b):
    return l*b


def per(l, b):
    return 2*(l+b)


def timer(n):
    import time
    time.sleep(n)


def rectangle_calculator():
    while True:
        print()
        print("<<----  RECTANGLE CALCULATOR  ---->>")
        print('''
        1.) To calculate the area of the rectangle ==>> ar
        2.) To calculate the perimeter of the rectangle ==>> per
        3.) To go back to the main calculator program ==>> 0

        ''')
        opt = input("Option --> ")
        opt = opt.lower()
        if opt in ["ar", "per"]:
            try:
                l = int(input("Length --> "))
                b = int(input("Breadth --> "))
            except ValueError:
                print("Invalid Numbers provided......")
                print("Taking you back to the main program.....")
                timer(2)
                break
            if opt == "ar":
                print("The area of the rectangle is", area(l, b))
            elif opt == "per":
                print("The perimeter of the rectangle is", per(l, b))
            else:
                print("Invalid Option......")
        elif opt == "0":
            print("Taking you back to the main program.....")
            timer(2)
            break
        else:
            print("Invalid Option......")
