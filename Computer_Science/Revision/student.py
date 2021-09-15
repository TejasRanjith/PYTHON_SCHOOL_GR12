# Question
#.y A binary file “STUDENT.DAT” has structure (admission_number, Name, Percentage). Write a
#.y function countrec() in Python that would read contents of the file “STUDENT.DAT” and
#.y display the details of those students whose percentage is above 75. Also display number of
#.y students scoring above 75%.
import pickle as pk

# with open("student.dat","wb") as f:
#     pk.dump(["01","A","75"],f)
#     pk.dump(["02","B","70"],f)
#     pk.dump(["03","C","75"],f)
#     pk.dump(["04","ABC","50"],f)

def count_rec():
    count = 0
    try:
        with open("student.dat","rb") as f:
            while True:
                data = pk.load(f)
                if data[-1] == "75":
                    print(data)
                    count+=1
    except EOFError:
        pass
    return count

print(count_rec())