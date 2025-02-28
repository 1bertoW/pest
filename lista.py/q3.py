#Escreva uma função chamada reverter que aceite uma string como entrada e retorne a string
#invertida.

def reverter(string:str):
    string_invertida = ""
    
    for indice in range(-1,-len(string)-1,-1):
        print(string[indice])
        string_invertida = string_invertida + string[indice]
    return string_invertida
    


inv = reverter("thiago")
print(inv)