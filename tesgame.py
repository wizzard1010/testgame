import secrets
import sys
secureNumber=secrets.SystemRandom()

while True:
    print("____Whelcome to my game/created by Thuta___")
    press1 = int(input("Press 1 to read rules or Press 2 to play game\n"))
    if press1 == 1:
        print(">Age must be more than 18")
        print(">Show money must be more than 5000")
        print(">You must use more than 1000 each time")
        print("Names cannot be contain numbers")
    if press1 == 2:
        while True: 
            uName = input("Please enter your name\n")
            if uName.isdigit():
                print("Name cannot be contain numbers")
                break
            else:
                uAge = int(input("Please enter your age\n"))

                if uAge < 17:
                    print("you need to be over 18")
                    break
                else:
                    print("You can play game now")
                    print("Welcome",uName)

                    while True:
                        sMoney = int(input("Please enter your show money\n"))
                        while sMoney > 4999:
                            while True:
                                print("This is your money $",sMoney)
                                inputMoney=int(input("Please enter money to play\n"))
                                luckyNumber = int(input("Please enter your lucky number\n"))
                                systemNumber=secureNumber.randint(10,99)
                                if luckyNumber == systemNumber:
                                    print("You win")
                                    sMoney = (inputMoney*10)+(sMoney-inputMoney)
                                    print("This is your prize money",sMoney)
                                    toQuit=int(input("Press 0 to play again\n"))
                                    if toQuit != 0:
                                        sys.exit("Bye Bye")
                                    else:
                                        continue
                           
                                print("try again.... Lucky number is",systemNumber)
                                sMoney = sMoney - inputMoney
                                if sMoney<1000:
                                    print("you have not enough money",sMoney)
                                break
                        print("Your show money has to be more than 5000")
                        print("Please add more money")
        
           
        print("please read the rules again")    
