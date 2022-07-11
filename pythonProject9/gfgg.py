class books:
    def __init__(self):
        self.m1=int(input("enter no of pages of book 1:"))
        self.m2=int(input("enter no of pages of book 2:"))



    def __add__(self):
        s3=self.m1+self.m2
        print(s3)


a1=books()
a1.__add__()

