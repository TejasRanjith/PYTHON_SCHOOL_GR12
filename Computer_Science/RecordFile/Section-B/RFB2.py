import random
l = []


def generator():
    num = random.randrange(1, 7)
    l.append(num)
    return num


def border():
    for i in range(0, 14):
        print(" *", end="")
    print()
    return i   # to prevent unused variable error


print()
print("Generate 50 throws of the dice.")
print()
for i in range(0, 10):
    print(generator(), "     ", generator(), "     ",
          generator(), "     ", generator(), "     ", generator())
print()
border()
for i in range(1, 7):
    print(f"No. of times '{i}' appeared :", l.count(i))
border()
print()
