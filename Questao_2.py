numero = int(input('Insira um número inteiro:')) #Permite que o usuário insira o número que será analizado
is_fibonacci = False #Variável que sinaliza se o número está ou não na sequência de Fibonacci
aux1 = 0 #Primeira variável auxiliar
aux2 = 1 #Segunda variável auxiliar

while aux1 <= numero: #Condição que limita a análise até o número inserido ou até o número mais alto mais próximo na sequência de Fibonacci
    if aux1 == numero:
        is_fibonacci = True #Se durante o loop for verificado que o valor da primeira variável auxiliar é igual ao número inserido pelo usuário, então é sinalizado que esse número está na sequência de Fibonacci
    aux1, aux2 = aux2, aux1 + aux2 #Cálculo do próximo item na sequência de Fibonacci

if is_fibonacci == True:
    print(f'O número {numero} se encontra na sequência de Fibonacci.') #Saída caso o número esteja na sequência
else:
    print(f'O número {numero} não se encontra na sequência de Fibonacci.')#Saída caso o número não esteja na sequência
