'''name = "banana"
for i in name:
    print(i)'''



print("this is one of the program which identifies names as boy's name and girl's name ")
name = str(input("enter the name of a child:"))
for i in name:
    if name[-1] == 'a':
        print("entered name is girls name")
        break
    else:
        print("entered name is boys name")
        break
