numero = int(input("digite um numero:"))
primo = 0

for i in range(numero):
    i += 1
    if numero % i == 0:
        primo += 1


if primo == 2:
    print("esse numero é primo")
else:
    print("o numero não é primo")
        
