#Crie uma função chamada palindromo_simples que verifique se uma string é igual à sua
#eversa. Retorne True ou False.

def palindromo_simples(string):
    return string == string[::-1]


resul = palindromo_simples("arara")
print(resul)