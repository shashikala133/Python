class student:

    def __init__(self, name, regno, m1, m2, m3):
        self.name = name
        self.regno = regno
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def getval(self):
        self.name = input("enter your name:")
        self.regno = int(input("enter your regno:"))
        self.m1 = float(input("enter marks m1:"))
        self.m2 = float(input("enter your marks m2:"))
        self.m3 = float(input("enter your mraks m3:"))
        self.avg = (self.m1 + self.m2 + self.m3) // 3
        print("average marks of yours is:", self.avg)

    def disvalue(self):
        self.avg = (self.m1+self.m2+self.m3)//3
        print("average marks of yours is:", self.avg)


class cet(student):
    def getseat(self):
        if self.avg > 85:
            print("you'll get seat in a better college..CONGRAJULATION")
        else:
            print("you need to work hard.BETTER LUCK NEXT TIME")


'''a1=student("shashikala",4252425,65,98,78)
print(a1.name)
print(a1.m1)'''
a2 = cet("shashi", 6453736, 75, 89, 99)
a2.getval()
a2.getseat()
