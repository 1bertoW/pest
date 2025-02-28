def eh_positivo(numero:int):
   if numero > 0:
    return True
   else:
    return False
   
numero = int(input("digite um numero"))
print(eh_positivo(numero))