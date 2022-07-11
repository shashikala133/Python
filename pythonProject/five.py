print("welcoMe to iron bank of bravous ATM")
restart=('y')
chances=3
balance=67.23
while chances>=0:
    pin=int(input("please enter your 4 digit number: "))
    if pin==1234:
        print('you entered your pin correctly\n')
        while restart not in ('n','no','N','NO'):
            print("please enter 1 for your balance\n ")
            print("please enter 2 for make withdrawal\n")
            print("please enter 3 for to pay in\n")
            print("please enter 4 for return\n")
            option=int(input("what would you like to choose\n"))
            if option==1:
                print("your balance is rs:",balance)
                restart=input("would you like to go back\n")
                if restart in('n','no','N','NO'):
                    print("thank you")
                    break
            elif option==2:
                withdrawal=float(input("how much would you like to withdraw?:"))
                balance=balance-withdrawal
                print("your balance is rs:",balance)
                restart=input("would you like to go back\n")
                if restart in('n','no','N','NO'):
                    print("thank you")
                    break
            elif option == 3:
                pay_in = float(input("how much would you like to pay_in:"))
                balance=balance*pay_in
                print("your available balance is rs: ",balance)
                restart = input("would you like to go back\n")
                if restart in('n', 'n', 'N', 'NO'):
                    print("thank you")
                    break

            elif option == 4:
                print("please wait whilst your card is returned\n")
                print("thank you for your service\n")
                break
            else:
                print("please enter a correct number\n")
                restart = ('y')
    elif pin != 1234:
        print("incorrect password\n")
        chances = chances-1
        if chances == 0:
            print("\nNo more tries")
            break