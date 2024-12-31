import random
botNumber=random.randint(1,10)
playerNumber=int(input("Введите число \n"))
while playerNumber !=botNumber:
    if playerNumber>botNumber:
        print("ты не угадал,мое число меньше")
    else:
        print("ты не угадал,мое число больше")
        playerNumber=int(input("Введите новое число \n"))
print("ты угадал мое число:" + str({botNumber}))