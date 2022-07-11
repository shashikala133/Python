password = input("enter a password of your choice:")

'''if len(password) < 8:
    print("password must contain atleast 8 characters")'''


for i in password:
    spl = 0
    num = 0
    if len(password) < 8:
        print("password must contain atleast 8 characters")
        break
    elif (i == '!' or i == '@' or i == '#' or i == '&' or i == '*' or i == '%' or i == '$' or i == '^'):
        spl += 1

    elif (i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9' or i == '0'):
        num += 1  # if(i.isdigit())

if spl>=1 and num>=1:
    print("your password is valid")

else:
    print("invalid password")



