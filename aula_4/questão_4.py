n1 = int(input("digite um numero de 3 digitos "))
n2 = int(input("digite um numero de 3 digitos "))
n3 = int(input("digite um numero de 3 digitos "))

soma = n1 + n2 + n3

if n1 == n2 or n2 == n3 or n3 ==n1:
    soma = 0
    print("soma igua a zero")

else:
    print(f"{soma}")