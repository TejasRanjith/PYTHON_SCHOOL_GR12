import length as l
import mass as m
import time


def timer(n):
    import time
    time.sleep(n)


while True:
    print()
    print("<<----  CONVERTER  ---->>")
    print("""
    1.) To open mass converter program ==>> m
    2.) To open length converter program ==>> l
    3.) To stop the main program ==>> 0
    
    """)
    opt = input("Your option --> ")
    opt = opt.lower()
    if opt == "m":
        m.mass_converter()
    elif opt == "l":
        l.length_converter()
    elif opt == "0":
        timer(1)
        print("Thank you for using the converter program.")
        print()
        timer(1)
        print("Hope to see you soon in converter program version 1.2.0")
        timer(2.5)
        print()
        print()
        print("Program exited with exit code 0")
        print()
        break
    elif opt == "":
        print("Invalid Option.......")
    else:
        print("Invalid Option.......")
