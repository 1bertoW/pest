def primeiro_e_utimo(string:str):
    primeiro = string[0]
    ultimo = string[-1]
    aux = primeiro + ultimo
    return aux

nova_string = primeiro_e_utimo('teste')
print(nova_string)