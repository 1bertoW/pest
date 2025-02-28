# Leia uma string do usuário e escreva na tela essa string caractere-por-caractere (um por linha) do início ao fim e, sem seguida, do fim para o início.
# Ex: "uva"

str = input("digite uma palavra:")


for i in range(len(str)):
    print(str[i])





for indice in range(len(str)-1,-1,-1):
    print(str[indice])