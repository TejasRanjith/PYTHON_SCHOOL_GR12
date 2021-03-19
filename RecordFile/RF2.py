def palindrome(n):
    r,val = 0,n
    while n > 0:
        a = n % 10
        r = r*10 + a
        n = n // 10
    if r == val:
        return True
    else:
        return False

def sumation(n):
    add = palindrome(n)+n
    return add

def armstr(n):
    a,i,l,num = n,0,[],len(str(n))
    while i < num:
        d = n - (n//10)*(10)
        l.append(d)
        n,i = n//10,i+1
    add = 0
    for elem in l:
        add = add+(elem**3)
    if add == a:
        return True
    else:
        return False

#! MAIN

while 1==1:
    print()
    print("<<<<----    PYTHON PROGRAM FOR SPECIFIC TASKS    ---->>>>")
    print("Please go through the following options:")
    print()
    print("     Insert a number to check if it is a Palindrome or not   ==>> pa")
    print("     Insert a number to display the Sum of original number and reversed number    ==>> or")
    print("     Insert a number to check if it is an Armstrong Number   ==>>  an")
    print("     Insert the given number to stop or exit the program   ==>>  0")
    print()
    opt = input("Option --> ")
    opt = opt.lower()
    if opt == "0":
        print("Thank you for using the program.  :) ")
        break
    else:
        num = int(input("The number --> "))
        print()
        if opt == "pa":
            if palindrome(num) == True:
                print("It is a Palindrome.")
            else:
                print("It is not a Palindrome.") 
        elif opt == "or":
            print(sumation(num),"is your required number.")
        elif opt == "an":
            if armstr(num) == True:
                print("It is an Armstrong number.")
            else:
                print("It is not an Armstrong number.")
        else:
            print("Invalid option. Please try again........")
print()
print()
print("Press enter to exit   ")
input()