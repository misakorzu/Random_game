import random
botNumber=random.randint(1,10)
playerNumber=int(input("Введите число"))
while playerNumber !=botNumber:
    if playerNumber>botNumber:
        print("ты не угадал,мое число меньше")
    else:
        print("ты не угадал,мое число больше")
        playerNumber=int(input("Введите число"))
print("ты угадал мое число:" + str({botNumber}))