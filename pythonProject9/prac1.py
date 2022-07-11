class parent:

    def par(self):
        father = input("enter father's name:")
        mother = input("enter mother's name:")
        child = input("enter child's name:")


class child:
    def marks(self):
            self.m1 = int(input("enter marks:"))
            self.m2 = int(input("enter marks:"))
            self.m3 = int(input("enter marks:"))
            self.m4 = int(input("enter marks:"))
            self.m5 = int(input("enter marks:"))
            self.m6 = int(input("enter marks:"))
            self.avg = (self.m1+self.m2+self.m3+self.m4+self.m5+self.m6)//6
            print("average marks of your child is:",self.avg)
            if self.avg>100:
                print("marks is out of bound..plz enter within 100")
            else:
                print("avearge is successfully calculated!!")

class higher(parent,child):
    def seat(self):
        if self.avg<40:
            print("you'll get seat in tier 4 college..you need to work hard")
        elif self.avg>40 and self.avg<60:
            print("you'll get seat in tier 3 college..congrats!!!")
        elif self.avg>60 and self.avg<80:
            print("you.ll get seat in tier 2 college..congrats!!!")
        elif self.avg<100:
            print("you'll get seat in the college you want..CONGRAJULATION!!!")
        else:
            print("oops!!you've done some mistake while entering your marks")
        print("THANK YOU..FOR YOUR PARTICIPATION")


obj1=higher()
obj1.par()
obj1.marks()
obj1.seat()
