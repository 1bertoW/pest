numero = int(input("Digite um numero:"))
contador = 1

while contador <= numero:
    verifica = input("Digite 0 para parar o código: ")
    if verifica == '0':
        break
    if numero % contador == 0:
        print(contador)
    contador += 1
