'''list=[]
num=int(input("enter number of element:"))

for i in range(0,num):
    i=int(input())
    list.append(i)
print(list)
list.sort()
print("sorted list:",list)
length=len(list)
print("largest element is:",list[length-1])
print("smallest element is:",list[0])
print("second largest element is:",list[length-2])
print("second smallest element is:",list[1])'''

'''list=[2,4,3]
new_list=[]
for i in list:
    j=i*i
    new_list.append(j)
print("given list is:",list)
print("square of number of given list:",new_list)'''

list=[3,7,8]
key=int(input("enter a key value to be searched:"))
for i in list:
    #print((i))
    if i==key:
        print("key found")
        break
else:
    print("key not found")


