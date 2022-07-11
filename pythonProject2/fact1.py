
def Fact(num):
    if num == 1:
        print(num)
    else:
        print(num * float(Fact(num-1)))
print(Fact(5))








