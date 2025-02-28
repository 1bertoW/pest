def inveter_direita(st):
    meio = len(st) // 2
    return  st[:meio] + st[meio:] [::-1]
print(inveter_direita("progamação"))
