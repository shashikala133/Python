count=0
sum=0
for i in range(10,50):
    if i>range:
        print("no is invalid")
    else:
        num = int(input('enter a number:'))
        count=count+1
        sum=sum+num
print("sum:",sum,"count:",count,"average=",sum/count)