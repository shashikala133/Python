

while True:
    num = print("imagine 1 no in your mind")
    user = input("lets continue the game y/n:")
    if user == 'y':
        print("double the number")
    else:
        print("thank you for the participation")
        break
    num1 = int(input("no which you want to give"))
    '''if num1 % 2 == 0:
        print("your entry is right")
    else:
        print("please enter a valid no")
        break'''
    user = input("lets continue the game y/n:")
    if user == 'y':
        print("add given number to previous no")
    else:
        print("thank you for the participation")
        break
    user = input("lets continue the game y/n:")
    if user == 'y':
        print("divide that number by 2")
    else:
        print("thank you for the participation")
        break
    user = input("lets continue the game y/n:")
    if user == 'y':
        print("subtract the current number from the number you imagined first")
    else:
        print("thank you for the participation")
        break
    user = input("lets continue the game y/n: ")
    if user == 'y':
        print("the number you imagined is :",num1/2)
        break


print("thank you")
