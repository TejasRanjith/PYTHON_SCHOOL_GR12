# Lesson 1
#* Write a python program that accepts an integer from the user & and calls function
#* even(x) to check if the number is Even or Odd.

def even(num):
    if num%2 == 0:
        return(f"{num} is an even number.")
    else:
        return(f"{num} is an odd number.")

#! MAIN:

num = int(input("Number : "))
print(even(num))

# even(5)
# even(74)
# even(36)
# even(123)
# print(even(546))