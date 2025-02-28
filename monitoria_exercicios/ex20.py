#Escreva um programa que contenha uma função chamada classificar_nota que receba uma nota (de 0 a 10) 
# como parâmetro e retorne “Aprovado” para notas maiores ou iguais a 6, “Reprovado” para notas menores que 6 e “Nota inválida” para valores fora do intervalo.
#  Solicite ao usuário uma nota e exiba a classificação.

def classificar_nota(n):
    if n > 10 or n < 0:
        return("nota invalida")
    elif n >= 6:
        return("aprovado")
    elif n < 6:
        return("reprovado")



n = int(input("digite um numero:"))
print(classificar_nota(n))

