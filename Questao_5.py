frase = str(input('Insira uma string: ')) #Usuário insire uma string para ser invertida e a grava na variável "frase"

frase_inv = [frase[i] for i in range(len(frase) - 1, -1, -1)] #Lista que grava inversamente cada caractere na string "frase"
print(''.join(frase_inv)) #A função join reúne todos os itens da lista, a transformando em uma string, que será impressa