class TIME:

    def __init__(self):
        self.hour = int(input("Hour:"))
        self.min = int(input("minute:"))
        self.second = int(input("second:"))


    def show(self):
        print("time is:", self.hour, ":", self.min, ":", self.second)


    def arithmetic(self, other):
        self.a = self.hour + other.hour
        self.b = self.min + other.min
        self.c = self.second + other.second
        print("addition is:",self.a,":",self.b,":",self.c)
        self.d = self.hour - other.hour
        self.e = self.min - other.min
        self.f = self.second - other.second
        print("subtraction:", self.d, ":", self.e, ":", self.f)



t1 = TIME()
t2 = TIME()
t1.show()
t2.show()
t1.arithmetic(t2)
