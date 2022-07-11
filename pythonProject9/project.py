import random
print("WELCOME")

if choice==y:
    uppercase=['A','B','C','D','E','F','G','H']
    lowercase=['a','b','c','d','e','f','g']
    number=['1','2','3','4','5','6','7']
    special=['@','#','*','$','!']
    password=random.choice(uppercase)+random.choice(lowercase)+random.choice(number)+random.choice(special)
    new_pass=password+password
    print(new_pass)
else:
    print("THANK YOU")



