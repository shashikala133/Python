class a:

    def __init__(self):
        print("in a init")

    def feature1(self):
        print("feature 1 a is woking")

    def feature2(self):
        print("feature 2 is woking")



class b(): #inheritance
    def __init__(self):

        print("in b init")

    def feature1(self):
        print("feature 1 b is woking")

    def feature4(self):
        print("feature 4 is woking")

class c(a,b):
    def __init__(self):
        super().__init__()

        print("in c init")

    def feature5(self):
        print("feature 5 is woking")

    def feature6(self):
        print("feature 6 is woking")
    def fea(self):
        super().feature2()

a1=c()
#b1=b()
#c1=c()
#a1.feature1()
#a1.feature2()
#b1.feature1()
#c1.feature1
a1.feature1()
a1.fea()


from abc import ABC,abstractmethod
class computer(ABC):
    @abstractmethod
    def process(self):
        pass
    def process(self):
        print("it is working")
a=computer()
a.process()






