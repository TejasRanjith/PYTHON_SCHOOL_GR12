def timer(n):
    import time
    time.sleep(n)

def dots():
    with open("poem.txt","r") as f:
        return (f.read().count("."))

def count_I():
    with open("poem.txt","r") as f:
        return f.read().count(" "+"I"+" ")   #! DOUBT-----------------------------------

def lines_tT():
    result = []
    with open("poem.txt","r") as f:
        for sent in f.read().split(sep = "\n"):
            if sent[0] in ["T","t"]:
                result.append(sent)
        return result

def lines():
    with open("poem.txt","r") as f:
        l =  f.read().split(sep = "\n")
        return l[0],l[-1]

def longest():
    with open("poem.txt","r") as f:
        l_sent = f.read().split(sep = "\n")
        l_len = []
        for sent in l_sent:
            l_len.append(len(sent))
            if len(sent) == max(l_len):
                return sent

while True:
    print("\n"+"<<----  MENU  ---->>"+"\n")
    print("1.) To count the number of dots present --> cd")
    print("2.) To count the number of 'I' present --> ci")
    print("3.) To display the lines starting with 'T/t' --> dt")
    print("4.) To display the first and last line --> fl")
    print("5.) To display the longest line --> ll")
    print("6.) To stop the main program --> 0"+"\n")
    opt = input("Option --> ")
    opt = opt.lower()
    if opt in ["cd","ci","dt","fl","ll"]:
        if opt == "cd":
            print("\n"+"****  The number of dots in the poem is,",dots())
        elif opt == "ci":
            print("\n"+"****  The number of times 'I' is repeated is,",count_I())
        elif opt == "dt":
            print("\n"+"****  The following lines are starting with 'T' or 't' :"+"\n")
            for elem in lines_tT():
                print("  "+elem)
        elif opt == "fl":
            a,b = lines()
            print(" ","****  The following lines are the first and last lines of the poem:","",a,b,sep="\n")
        elif opt == "ll":
            print(" ","****  The following line is the longest line :"," ","  "+longest(),sep="\n")
        else:
            print("Invalid Option......")
    elif opt == "0":
        timer(1)
        print("\n"+"Thank you for using the string modifier program."+"\n")
        timer(1)
        print("Hope to see you soon in string modifier program version 1.2.0"+"\n"+"\n")
        timer(1.5)
        print("Program exited with exit code 0"+"\n")
        break
    else:
        print("Invalid Option......")
