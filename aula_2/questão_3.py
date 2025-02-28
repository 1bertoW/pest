
hora = int(input('Escolha uma hora: '))
alarme = int(input('Escolha um horario para o alarme: '))


hora_final = (hora + alarme)%24

print(f"o alarme tocará as {hora_final} horas")


