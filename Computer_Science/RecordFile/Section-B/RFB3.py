def timer(n):
    import time
    time.sleep(n)


def vowel_count(word):
    v_count = 0
    c_count = 0
    for elem in word:
        if elem in ["a", "e", "i", "o", "u"]:
            v_count += 1
        else:
            c_count += 1
    return v_count, c_count


def replacing_vowels(word):
    word = list(word)
    for elem in word:
        if elem in ["a", "e", "i", "o", "u"]:
            word[word.index(elem)] = "*"
        else:
            pass
    result = ""
    for elem in word:
        result += elem
    return result


def digits_string(word):
    digit = ""
    for elem in word:
        if elem.isdigit() == True:
            digit += elem
        else:
            pass
    return digit


while True:

    print()
    print("<<----  STRING_MODIFIER_PROGRAM ---->>")
    print()
    print("Please go through the folowing options given below :")
    print()
    print("To count the number of vowels given in the string --> cv")
    print("To replace the vowels with stars --> rv")
    print("To separate the digits from the string --> ds")
    print("To stop the main program --> 0")
    print()
    opt = input("Please Provide the option --> ")
    opt = opt.lower()
    print()
    if opt in ["cv", "rv", "ds"]:
        word = input("Please mention the string before proceeding --> ")
        print()
        if opt == "cv":
            print()
            v, c = vowel_count(word)
            print(">>>>  The no. of vowels in the given string,", word, "is : ", v)
            print(">>>>  The no. of consonants in the given string,",
                  word, "is : ", c)
            print()
        elif opt == "rv":
            print()
            print(">>>>  The string,", word, "with vowels being replaced is,",
                  replacing_vowels(word))
            print()
        elif opt == "ds":
            print()
            print(">>>>  The string,", word,
                  "with digits being separated from the letters is,", digits_string(word))
            print()
    elif opt == "0":
        timer(1)
        print("Thank you for using the string modifier program.")
        print()
        timer(1)
        print("Hope to see you soon in string modifier program version 1.2.0")
        timer(1.5)
        print()
        print()
        print("Program exited with exit code 0")
        print()
        break
    else:
        print("Invalid Option ......")
