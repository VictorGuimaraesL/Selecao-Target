frase = str(input('Insira uma string: '))

frase_inv = [frase[i] for i in range(len(frase) - 1, -1, -1)]
print(''.join(frase_inv))