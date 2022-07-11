class student:

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()
    def show(self):
        print(self.name,self.rollno)
    class laptop:

        def __init__(self):
            self.brand='hp'
            self.ram=8
            self.con='i5'

s1=student('shashikala',4)
s2=student('krupa',5)
s2.brand='lenova'
s1.show()
lap1=student.laptop()
lap2=student.laptop()
print(lap2.brand)
print(s2.brand)


#method overloading
class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def sum(self,a,b):
        s=a+b
        return s

    def mul(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s

s1=student(45,54)
print(s1.m1)
print(s1.sum(45,40))
print(s1.mul(3))



class a:
    def show(self):
        print("in a show")

class b(a):
    def show(self):
        print("in b show")


a1=b()
a1.show()
