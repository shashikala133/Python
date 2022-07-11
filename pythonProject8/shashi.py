f=open('m1.py','r')
'''print(f.readline(),end="")
print(f.readline())
print(f.readline())'''

f1=open('abc','w')
for data in f:
    f1.write(data)
'''f2=open("2019-04-10-10-37-47-366.jpg",'wb')

f2.write('2019-04-10-10-37-47-366')'''

f3=open("2019-04-10-10-37-47-366.jpg",'rb')
f4=open('mypic.jpg','wb')
for i in f3:
    f4.write(f3)


