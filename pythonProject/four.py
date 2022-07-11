import random
n=20
to_be_guessed=int(n+random.random())+7
guess=0
while guess!=to_be_guessed:
    guess=int(input("new number: "))
    if guess>0:
        if guess>to_be_guessed:
            print("number too large")
        elif guess<to_be_guessed:
            print("number too small")
    else:
        ("sorry that you are giving up")
        break
else:
    print("CONGRAJULATION that you made it")