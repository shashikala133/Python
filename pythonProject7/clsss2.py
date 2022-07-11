



'''class car:
    wheel = 4      #class variable
    def __init__(self):
        self.mil = 65   #instance variable
        self.com = 'bmw'
    def compare(self, other):
        if self. mil == other.mil:
            return True
        else:
            return False


c1 = car()
c2 = car()
c2.mil = 45
if c1.compare(c2):
    print("both are good")
elif c2.mil > c1.mil:
    print("c2 is better than c1")
else:
    print("c1 is better than c2")

car.wheel = 6
print(c1.com)
print(car.wheel)'''

#duck typing
class pycharm:
    def execute(self):
        print("running")
        print("compiling")


class myeditor:
    def execute(self):
        print("spell check")
        print("comiling")
        print("running")

class laptop:
    def code(self,ide):
        ide.execute()

#ide=pycharm()
ide=myeditor()
lap1=laptop()
lap1.code(ide)


















