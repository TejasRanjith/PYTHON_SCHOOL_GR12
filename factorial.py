while 1 == 1:
    opt = input("Option --> ")
    opt = opt.lower()
    if opt == "f":
        n = int(input('Number --> '))
        f=1
        for l in range(1,n+1):
            f=f*l
        print("The factorial of",n,"is",f)
    elif opt == "pr":
        nums = []
        n = int(input("Number --> "))
        for num in range(0,n+1):
            nums.append(num)
            if num in range(0,n+1,2):
                nums.remove(num)
            elif num in range(0,n+1,3):
                nums.remove(num)
            elif num in range(0,n+1,5):
                nums.remove(num)
            elif num in range(0,n+1,7):
                nums.remove(num)
            else:
                pass
        nums.remove(1)
        nums.append(2)
        nums.append(3)
        nums.append(5)
        nums.append(7)
        nums.sort()
        print(nums)
    elif opt == "pa":
        num = input("Number --> ")
        if num == num[::-1]:
            print("It is a palindrome number.")
        else:
            print("It is not a plaindrome number.")
    elif opt == "0":
        break