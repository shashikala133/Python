
class TIME:

    def __init__(self):
        self.hour = int(input("Hour:"))
        self.min = int(input("minute:"))
        self.second = int(input("second:"))

    def show(self):
        if self.second>=60 and self.min>=60 :
            self.min += 1
            self.second -= 60
            self.hour += 1
            self.min -= 60
            print("time is:", self.hour, ":", self.min, ":", self.second)

        elif self.second >= 60:
            self.min += 1
            self.second -= 60
            print("time is:", self.hour, ":", self.min, ":", self.second)
        elif self.min >= 60:
            self.hour += 1
            self.min -= 60
            print("time is:", self.hour, ":", self.min, ":", self.second)
        elif self.hour>12 and self.min>=60:
            self.hour -= 12
            self.min += 1
            self.min -=60
            self.second+=1
            print("time  is:", self.hour, ":", self.min, ":", self.second)

        else:
            print("time  is:", self.hour, ":", self.min, ":", self.second)
        if self.hour>12:
            self.hour-=12
            self.min+=1
            print("time  is:", self.hour, ":", self.min, ":", self.second)

    def arithmetic(self,other):

        self.a = self.hour + other.hour
        self.b = self.min + other.min
        self.c = self.second + other.second
        if self.c>=60 and self.b>=60 and self.a>12:
            self.b+=1
            self.c-=60
            self.a+=1
            self.b-=60
            self.a-=12
            self.b+=1
            print("addition1:", self.a, ":", self.b, ":", self.c)
        if self.c>=60:
            self.c-=60
            self.b+=1
            print("addition2:", self.a, ":", self.b, ":", self.c)
        elif self.b>=60 and self.a>12:
            self.b-=60
            self.a+=1
            self.b-=12
            self.b+=1
            print("addition:", self.a, ":", self.b, ":", self.c)

        '''else:
            print("addition3:", self.a, ":", self.b, ":", self.c)'''
        if self.a>12:
            self.a-=12
            self.b+=1
            print("addition4:", self.a, ":", self.b, ":", self.c)

        self.d = self.hour - other.hour
        self.e = self.min - other.min
        self.f = self.second - other.second
        if self.f<0 or self.e<0:
            self.e -= 1
            self.d -= 1
            self.sub1 = (self.second - other.second) + 60
            self.sub2 = (self.min - other.min) + 60
            print("subtraction:", self.d, ":", self.sub2, ":", self.sub1)

        elif self.f<0:
            self.sub=(self.second-other.second)+60

            self.e -=1
            print("subtraction:", self.d, ":", self.e, ":", self.sub)
        elif self.e<0:
            self.sub=(self.min - other.min)+60
            self.d -= 1
            print("subtraction:", self.d, ":", self.e, ":", self.sub)
        elif self.d<0:
            self.sub=(self.hour - other.hour)+60
            self.e +=1
            print("subtraction:", self.d, ":", self.e, ":", self.sub)
        else:

            print("subtraction:", self.d, ":", self.e, ":", self.f)




t1 = TIME()
t2 = TIME()
t1.show()
t2.show()
#t2.show()
t1.arithmetic(t2)


