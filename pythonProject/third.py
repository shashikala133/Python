import array as arr
a=arr.array('d',[1,2,3,4,5,6])
print("popping last element of array",a.pop())
print("printing 3rd element of array",a.pop(2))
print(a[0:3])
a.append(3.4)
print(a)
b=arr.array('d',[3,4,2,5,7,8])
c=arr.array('d',[6,3,8,9,2,6])
d=b+c
print(d)
e=0
while(e<len(a)):
    print(a[e])
    e=e+1
my_dict={'dove':'001','nish':'002','ansh':'003'}
print(my_dict)
print(type(my_dict))
print(my_dict.get('ansh'))
print(my_dict.pop('nish'))
