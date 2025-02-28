
def eh_primo(num : int):
    primo = 0
    for i in range(num):
        i += 1
        if num % i == 0:
            primo += 1
    if primo == 2:
        return True
    else:
        return False

    
n = int(input("digite um numero:"))

resul = eh_primo(n)

print(resul)