s,S = input("Enter the string: "),[]
for l in s:
    if l in ['a','e','i','o','u']:
        S.append(l)
print("Vowels from the Vstack --> : ",end=" ")
for l in S[::-1]:
    print(l,end=" ")

