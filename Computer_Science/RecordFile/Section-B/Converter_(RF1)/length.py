def miletokm(m):
    return m*1.60934


def kmtomile(k):
    return k*0.621371


def feettoinches(f):
    return f*12


def inchestofeet(i):
    return i*0.08333


def timer(n):
    import time
    time.sleep(n)


def length_converter():
    while True:
        print()
        print("<<----  LENGTH CONVERTER  ---->>")
        print('''
        1.) Miles to Km ==>> mk
        2.) Km to Miles ==>> km
        3.) Feet to Inches ==>> fi
        4.) Inches to Feet ==>> if
        5.) To go back to the main converter program ==>> 0
        ''')
        opt = input("Option --> ")
        if opt in ["mk", "km", "fi", "if"]:
            try:
                val = int(input("Numeral Value/Magnitude --> "))
            except ValueError:
                print("Please enter a number......")
                print("Taking you back to the main program.....")
                timer(2)
                break
            if val == 0:
                print("Invalid Option.......")
            else:
                if opt == "mk":
                    result = miletokm(val)
                elif opt == "km":
                    result = kmtomile(val)
                elif opt == "fi":
                    result = feettoinches(val)
                elif opt == "if":
                    result = inchestofeet(val)
                else:
                    print("Invalid Option")
                print(result)
        elif opt == "0":
            print("Taking you back to the main converter program.......")
            timer(2)
            break
        else:
            print("Invalid Option......")
