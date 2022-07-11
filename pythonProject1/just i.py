print("welcome to rock paper scissor game for everybody")
print("enter choice1:1.rock,2.paper,3.scissor")
num = int(input("how many times you wanna play:"))
choice1 = int(input("enter shahsikala's choice:"))
while True:
    if choice1 == 1:
        print("your choice is rock")
        break
    if choice1 == 2:
        print("your choice is paper")
        break
    if choice1 == 3:
        print("your choice is scissor")
        break
    else:
        print("invalid choice")
        break
print("enter your choice2:1.rock,2.paper,3.scissor")
choice2 = int(input("enter prajwal's choice:"))
while True:
    if choice2 == 1:
        print("your choice is rock")
        break
    if choice2 == 2:
        print("your choice is paper")
        break
    if choice2 == 3:
        print("your choice is scissor")
        break
    else:
        print("invalid choice")
        break
if choice1 == 1 and choice2 == 2:
    print("paper wins")

if choice1 == 1 and choice2 == 3:
    print("rock wins")

if choice1 == 2 and choice2 == 1:
    print("paper wins")

if choice1 == 2 and choice2 == 3:
    print("scissor wins")

if choice1 == 3 and choice2 == 1:
    print("rock wins")

if choice1 == 3 and choice2 == 2:
    print("scissor wins")

if choice1 ==  choice2:
    print("the game is tie now")


