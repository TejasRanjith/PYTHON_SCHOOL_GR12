import statistics as st

while True:
    print("\n<<----  MENU  ---->>")
    print("To calculate the mean age of the students -->  mean")
    print("To calculate the median of the age of the students --> med")
    print("To calculate the mode of the age of the students -->  mode")
    print("To exit the main program  --> 0")
    
    opt = input("\nYour Option --> ").lower()
    if opt == "mean":
        l = eval(input("Type your list of age of students   ([15,17,16])  --> "))
        print("\nThe mean age of the students is,",st.mean(l))
    elif opt == "med":
        l = eval(input("Type your list of age of students   ([15,17,16])  --> "))
        print("\nThe median of the age of the students is,",st.median(l))
    elif opt == "mode":
        l = eval(input("Type your list of age of students   ([15,17,16])  --> "))
        print("The mode value of the age of the students is,",st.mode(l))
    elif opt == "0":
        print("Thank you for using the program.")
        exit()
    else:
        print("Invalid Option...")