from report_card import main_dict

f = open("report_card.txt","a+")
f.write(str(main_dict)+"\n")
f.close()

f = open("report_card.txt","r+")
contents = f.read()
f.close()

for k in contents.split(sep = "\n"):
    main_dict.update(eval(k))

print(main_dict)