def sumNum(num):
    previousNum=0
    for i in range(num):
        sum=previousNum+i
        print("previousNum",previousNum,"currentNum",i,"sum= ",sum)
        previousNum=i
sumNum(10)

