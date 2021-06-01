def quad_eq(a, b, c):
    d = (b**2) - (4*a*c)
    if d >= 0:
        A, B = (-b + d**(1/2))/2, (-b - d**(1/2))/2
        return A, B
    else:
        return "It has non real roots", "It has non real roots"


def arc_len(a, r):
    l = 2*(22/7)*r*(a/360)
    return l


def timer(n):
    import time
    time.sleep(n)


while True:
    print()
    print("<<----  MATH_PROGRAM  ---->>")
    print()
    print("Please go through the following options:")
    print()
    print("To find the roots of the Quadratic Equation --> eq")
    print("To find the Length of the Arc of a Circle with specified Radius and Angle --> arc")
    print("To stop the main program --> 0")
    print()
    opt = input("Your Option --> ")
    opt = opt.lower()
    print()
    if opt in ["eq", "arc"]:
        if opt == "eq":
            c1, c2, c3 = int(input("Coefficient of x^2 --> ")), int(
                input("Coefficient of x --> ")), int(input("Constant --> "))
            a, b = quad_eq(c1, c2, c3)
            print()
            if a == "It has non real roots" and b == "It has non real roots":
                print("It has non real roots")
            elif a != "It has non real roots" and b != "It has non real roots":
                print("****  The roots of the equation are,", a, "and", b)
            else:
                pass
        elif opt == "arc":
            a, r = int(input("The Angle between the two Radii --> ")
                       ), int(input("The Radius of the Circle --> "))
            print()
            print("****  The legth of the arc is,", arc_len(a, r))
        else:
            print("Invalid Option......")
    elif opt == "0":
        timer(1)
        print("Thank you for using the math program.")
        print()
        timer(1)
        print("Hope to see you soon in math program version 1.2.0")
        timer(1.7)
        print()
        print()
        print("Program exited with exit code 0")
        print()
        break
    else:
        print("Invalid Option......")
