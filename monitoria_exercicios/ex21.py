#Desenvolva uma função chamada conta_digitos que receba um número inteiro como parâmetro e retorne a quantidade de dígitos no número. 
# No programa principal, solicite um número ao usuário e exiba o resultado.

def contar_dig(n):
    contador = 0
    while n > 0:
        n = n // 10
        contador += 1
    return contador

n = int(input("digite um numero:"))
res = contar_dig(n)
print(res)







