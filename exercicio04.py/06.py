var1 = int(input('Insira o tempo em segundos:'))
info = ('O tempo do intervalo em horas será:')
product = var1 // 3600
segundo_rest = var1 % 3600
minutos = segundo_rest // 60
print(info, product, minutos)
