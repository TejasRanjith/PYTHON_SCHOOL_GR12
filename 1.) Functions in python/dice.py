print("Press enter to continously roll the dice or type 0 to stop the program:")
while 1 == 1:
    print()
    a = input()
    if a == "":
        import random
        num = random.randrange(1,7)
        print("output:  ",num)
    elif a == "0":
        break
    else:
        pass
