str1 = input("digite uma palavra/frase:")
str2 = input("digite uma palavra/frase:")

t1 = len(str1)
t2 = len(str2)

if t1 > t2:
    print(f"a palavra {str1} de tamanho {t1} é maior que a palavra {str2} de tamanho {t2}")
elif t1 < t2:
    print(f"a palavra {str2} de tamanho {t2} é maior que a palavra {str2} de tamanho {t2}")
else:
    print(f"{str1}")