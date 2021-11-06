#035611
def num_chars():
    with open("Rhyme.txt","r") as f:
        contents = f.read()
    print("\nNumber of Characters: ", len(contents))
    print("\nNumber of Words: ",len(contents.split()))
    print("\nNumber of Lines: ",len(contents.split(sep="\n")))

def line_T():
    count = 0
    with open("Rhyme.txt","r") as f:
        contents = f.readlines()
        for line in contents:
            if line[0] == "T":
                count+=1
    print("\nNumber of lines starting with 'T' :",count)

def no_v():
    count = 0
    with open("Rhyme.txt","r") as f:
        contents = f.read()
        for letter in contents:
            if letter in "AEIOUaeiou":
                count+=1
    print("\nNumber of vowels in the text file :",count)

def no_words():
    count = 0
    with open("rhyme.txt","r") as f:
        contents = f.readlines()
        for line in contents:
            count += len(line.split())
    print("\nNumber of words in each line :",count)

def no_star():
    with open("rhyme.txt","r") as f:
        print("\nNumber of words in each line :",f.read().count("STAR"))

while True:
    print("\n<<----  MENU  ---->>\n")
    print("  Display the numbers of characters, words and lines.  --> n")
    print("  Displays no of lines starting with T.                --> t")
    print("  Displays the no of occurrence of vowels.             --> v")
    print("  Displays the no of words in each line.               --> w")
    print("  Displays the no of occurrence of the word 'star'.    --> s")
    print("")
    opt = input("Your option --> ").lower()
    if opt == "n":
        num_chars()
    elif opt == "t":
        line_T()
    elif opt == "v":
        no_v()
    elif opt == "w":
        no_words()
    elif opt == "s":
        no_star()
    elif opt == "0":
        print("Thank you for using the program...")
        break
    else:
        print("Invalid Option...")
# OUPUT
# <<----  MENU  ---->>

#   Display the numbers of characters, words and lines.  --> n
#   Displays no of lines starting with T.                --> t
#   Displays the no of occurrence of vowels.             --> v
#   Displays the no of words in each line.               --> w
#   Displays the no of occurrence of the word 'star'.    --> s

# Your option --> n

# Number of Characters:  161

# Number of Words:  32

# Number of Lines:  6

# <<----  MENU  ---->>

#   Display the numbers of characters, words and lines.  --> n
#   Displays no of lines starting with T.                --> t
#   Displays the no of occurrence of vowels.             --> v
#   Displays the no of words in each line.               --> w
#   Displays the no of occurrence of the word 'star'.    --> s

# Your option --> t

# Number of lines starting with 'T' : 2

# <<----  MENU  ---->>

#   Display the numbers of characters, words and lines.  --> n
#   Displays no of lines starting with T.                --> t
#   Displays the no of occurrence of vowels.             --> v
#   Displays the no of words in each line.               --> w
#   Displays the no of occurrence of the word 'star'.    --> s

# Your option --> v

# Number of vowels in the text file : 48

# <<----  MENU  ---->>

#   Display the numbers of characters, words and lines.  --> n
#   Displays no of lines starting with T.                --> t
#   Displays the no of occurrence of vowels.             --> v
#   Displays the no of words in each line.               --> w
#   Displays the no of occurrence of the word 'star'.    --> s

# Your option --> w

# Number of words in each line : 32

# <<----  MENU  ---->>

#   Display the numbers of characters, words and lines.  --> n
#   Displays no of lines starting with T.                --> t
#   Displays the no of occurrence of vowels.             --> v
#   Displays the no of words in each line.               --> w
#   Displays the no of occurrence of the word 'star'.    --> s

# Your option --> s

# Number of words in each line : 2