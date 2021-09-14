def factorial(n):
    tot = 1
    for num in range(n,0,-1):
        tot = tot*num
    return tot

def fib(n):
    a,b,i,l = 0,1,0,[]
    for i in range(n):
        s = a+b
        a,b,s = s,a,b
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
    l.remove(1)
    l.remove(0)
    return l
#! Main
while True:
    print("\n<<----    PYTHON PROGRAM FOR SPECIFIC TASKS    ---->>")
    print("Please go through the following options:\n")
    print("     Insert a number to find the factorial of the number --> fn")
    print("     Insert a number to display n prime numbers --> pn")
    print("     Insert a number to display Fibonacci Series up to n numbers --> fs")
    print("     Insert the given number to stop or exit the program   -->  0")
    num = int(input("\nThe number --> "))
    opt = input("Option --> ").lower()
    if opt == "0":
        print("Thank you for using the program.  :) ")
        break
    else:
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
print("Press enter to exit    ")
input()