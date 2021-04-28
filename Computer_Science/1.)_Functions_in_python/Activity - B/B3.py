# Lesson 1
#* design python program to find the area of a rectangle provided by the user.

def rectangle(l,b):
    print("Area of the rectangle : ",l*b)
    return l*b

#! MAIN:

l = int(input("Length : "))
b = int(input("Breadth : "))
rectangle(l,b)
