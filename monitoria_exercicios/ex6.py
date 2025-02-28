import random
num = random.randint(1,9)
limitador = 5
while True:
    num1 = int(input("digite um numero de 1 a 9:"))
    if limitador == 0:
        break
    elif num1 == num:
        print("parábens seu caba bom você ganho um fusca azul 1.4")
        break
    elif num1 < num:
        print("o seu numero é muito baixo")
    elif num1 > num:
        print("seu numero é muito alto")
    elif limitador == 0:
        break
    limitador -= 1
