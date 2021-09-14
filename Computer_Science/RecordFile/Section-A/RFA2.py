def palindrome(string):
    string = string.lower()
    if string == string[::-1]:
        print("The given word is a palindrome.")
    else:
        print("The given word is not a palindrome")

def count(string):
    alpha,spec,digi = 0,0,0
    for letter in string:
        if letter.isalpha():
            alpha+=1
        elif letter.isdigit():
            digi+=1
        elif letter.isspace():
            pass
        else:
            spec+=1
    print(alpha,spec,digi)

def remove_vowel(string):
    new_string = ""
    for letter in string:
        if letter.lower() not in "aeiou":
            new_string+=letter
    print(new_string)

def replace_consonant(string):
    new_string = ""
    for letter in string:
        if letter.lower() not in "aeiou":
            new_string+="*"
        else:
            new_string+=letter
    print(new_string)

while True:
    print("\n<<----    PYTHON PROGRAM FOR SPECIFIC TASKS    ---->>")
    print("Please go through the following options:\n")
    print("To check if a given string is a Palindrome.                                 --> p")
    print("To count the number of alphabets, special characters, digits in a string.   --> c")
    print("To remove all vowels from a string.                                         --> v")
    print("To replaces every consonant by  ‘*’                                         --> r")
    print("To stop or exit the program                                                 --> 0\n")
    opt = input("Your Option --> ").lower()
    s = input("\nYour String :")
    if opt == "p":
        palindrome(s)
    elif opt == "c":
        count(s)
    elif opt == "v":
        remove_vowel(s)
    elif opt == "r":
        replace_consonant(s)
    elif opt == "0":
        print("Thank you for using the program...")
        break
    else:
        print("Invalid Option....")

print("Press enter to exit the program ")
input()


# def replace():
#     str1 = input("Enter String : ")
#     for i in str1:
#         if i.isalpha() == True:
#             if i not in "AEIOUaeiou":
#                 str1 = str1.replace(i,"*")
#     print("new string is: ",str1)

# replace()