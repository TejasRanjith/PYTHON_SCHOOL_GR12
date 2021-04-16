def factorial(n):
    tot = 1
    for num in range(n,0,-1):
        tot = tot*num
    return tot

def fib(n):
    a,b,i,l = 0,1,0,[]
    while i<n:
        s = a+b
        a,b,s,i = s,a,b,i+1
        l.append(b)
    return l

def prime(n):
    l = []
    for num in range(0,n+1):
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            l.append(num)
    return l

#! Main

while 1==1:
    print()
    print("<<<<----    PYTHON PROGRAM FOR SPECIFIC TASKS    ---->>>>")
    print("Please go through the following options:")
    print()
    print("     Insert a number to find the factorial of the number ==>> fn")
    print("     Insert a number to display n prime numbers ==>> pn")
    print("     Insert a number to display Fibonacci Series up to n numbers ==>> fs")
    print("     Insert the given number to stop or exit the program   ==>>  0")
    print()
    opt = input("Option --> ")
    opt = opt.lower()
    if opt == "0":
        print("Thank you for using the program.  :) ")
        break
    else:
        print()
        num = int(input("The number --> "))
        print()
        if opt == "fn":
            print(factorial(num),"is the Factorial of the number provided.")
        elif opt == "pn":
            print("The list of prime numbers till",num,"is given below:")
            print(prime(num))
        elif opt == "fs":
            print("The list of Fibonacci Series up to 'n' numbers is given below:")
            print(fib(num))
        else:
            print("Invalid Option. Please try again ........")
print()
print()
print("Press enter to exit    ")
input()