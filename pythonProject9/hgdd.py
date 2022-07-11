class student:
    def __init__(self):
        self.m1=int(input("first mse mark:"))
        self.m2=int(input("second mse mark:"))
        self.m3=int(input("third mse mark:"))

    def avg(self):
        self.avg=(self.m1+self.m2+self.m3)//3
        print(self.avg)

    def highest(self):
        if self.m1>self.m2 and self.m1>self.m3:
            print("mse 1 has highest mark")
        elif self.m2>self.m1 and self.m2>self.m3:
            print("mse 2 has highet mark")
        else:
            print("mse 3 has hihest mark")

b1=student()
b1.avg()
b1.highest()