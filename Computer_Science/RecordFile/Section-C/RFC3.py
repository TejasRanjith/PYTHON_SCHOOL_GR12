def readfile():
    with open("NotesFile.txt","r") as f:
        cont = f.read()
        return(cont)

def writefile(c):
    with open("NotesFile.txt","w") as f:
        f.write(c)

def printfile():
    return len(readfile().split())

def countfile():
    return readfile().count("file") + readfile().count("File")

def replace_i():
    writefile(readfile().replace("i", "*"))
    return readfile()

def deletedata():
    writefile(readfile().replace(" data ", " ").replace("Data ", " "))
    return readfile()

print("\nThe number of words:",printfile(),
"The number of times the word file has repeated:",f"{countfile()-1}",
"The Paragraph with the word 'data' removed:","",deletedata(),"",
"The Paragraph with the letter 'i' replaced by '*':","",replace_i(),"",
sep="\n")