str1 = "hello hii how are you hello how how hii"
list2 = str1.split()
print(list2)
'''element = list2[0]
a = (element)'''
key = str(input("enter the key which you want to search:"))
count = 0

for i in range(0, len(list2)):
    if list2[i] == key:
        count += 1
print("key is repeated",count ,"times")


