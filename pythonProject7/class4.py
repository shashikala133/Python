#iterator
'''num=[5,4,3,6]
print(num[3])
for i in num:
    print(i)'''
'''it=iter(num)
print(it.__next__())
print(it.__next__())
print(next(it))'''

'''class topten:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            value=self.num
            self.num+=1
            return value
        else:
            raise StopIteration
values=topten()
print(next(values))
print(next(values))
for i in values:
    print(i)'''

#generators
'''def topten():
    i=1
    while i<=10:
        sq=i*i
        yield sq
        i+=1
val=topten()
#print(val)
#print(next(val))

for i in val:
    print(i)'''

#exception handling
def div():
    a = int(input("enter one number:"))
    b = int(input("enter another number:"))
    try:
        c = a/b
        print(c)
    except ZeroDivisionError:
        print("you cannot divide a no by zero")
    finally:
        print("thank you")


div()
