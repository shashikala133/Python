#instance method
#static method
#class method

class student:

    school='telusko'

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    def get_m1(self):
        return self.m1
    def set_m1(self,value):
        self.m1=value
        #if u r working with instance use self and for static use class variable
    '''def info(self):
        self.name='telusko'
        return self.name'''
    @classmethod #decorater
    def get_school(cls):
        return cls.school
    @staticmethod
    def info(): #static keep it blank
        print("this is static method")


s1=student(34,5,66)
s2=student(65,33,77)
print(s1.avg())
print(s2.avg())

print(student.info())


#operator overloading



'''a=5
b='hello'
print(a+b)'''#all are predefined(synthetic sugar)
print(int.__add__(3,4))

class int:
    def __iadd__(self,a,b):

        print(a+b)
a=int()
a.__iadd__(3,5)
print(str.__add__('hello','hii'))



class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=student(m1,m2)
        return s3
    def __gt__(self, other):
        r1=self.m1+self.m2
        r2=other.m1+other.m2
        if r1>r2:
            return True
        else:
            return False

    def __sub__(self, other):
        m1=self.m1-self.m2
        m2=other.m1+other.m2
        s4=student(m1,m2)
        return s4
    def __str__(self):
        #return self.m1+self.m2
        #return set.m1,self.m2
        return '{} {}'.format(self.m1,self.m2)

s1=student(54,66)
s2=student(43,55)
s3=s1+s2
print(s3.m1)
if s1>s2:
    print("s1 wins")
else:
    print("s2 wins")
s4=s1-s2
print(s4.m1)
a=4
print(a.__str__())
print(s1.__str__())
print(s1)
print(s2)






