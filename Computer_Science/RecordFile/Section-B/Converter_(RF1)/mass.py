def kgtotonne(k):
    return k*0.001


def tonnetokg(t):
    return t*1000


def kgtopound(k):
    return k*2.20462


def poundtokg(p):
    return p*0.453592


def timer(n):
    import time
    time.sleep(n)


def mass_converter():
    while True:
        print()
        print("<<----  MASS CONVERTER  ---->>")
        print('''
        1.) Kg to Tonne ==>> kt
        2.) Tonne to Kg ==>> tk
        3.) Kg to Pound ==>> kp
        4.) Pound to Kg ==>> pk
        5.) To go back to the main converter program ==>> 0
        ''')
        opt = input("Option --> ")
        if opt in ["kt", "tk", "kp", "pk"]:
            try:
                val = int(input("Numeral Value/Magnitude --> "))
            except ValueError:
                print("Please enter a number......")
                print("Taking you back to the main program.....")
                timer(2)
                break
            if val != 0:
                if opt == "kt":
                    result = kgtotonne(val)
                elif opt == "tk":
                    result = tonnetokg(val)
                elif opt == "kp":
                    result = kgtopound(val)
                elif opt == "pk":
                    result = poundtokg(val)
                else:
                    print("Invalid Option......")
                print(result)
            else:
                print("Invalid Option......")
        elif opt == "0":
            print("Taking you back to the main converter program.......")
            timer(2)
            break
        else:
            print("Invalid Option.....")
