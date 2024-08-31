numero = int(input('Insira um número inteiro:'))
is_fibonacci = False
aux1 = 0
aux2 = 1

while aux1 <= numero:
    if aux1 == numero:
        is_fibonacci = True
    aux1, aux2 = aux2, aux1 + aux2

if is_fibonacci == True:
    print(f'O número {numero} se encontra na sequência de Fibonacci.')
else:
    print(f'O número {numero} não se encontra na sequência de Fibonacci.')
