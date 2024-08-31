def calculo_percent(dados): #Função que recebe um dicionário de dados como argumento e retorna seus percentuais de representação
    total = sum(dados.values()) #Cálculo do valor total de faturamento
    percentuais = {}
    for estado, valor in dados.items(): #Loop que percorre cada item no dicionário
        percentuais[estado] = (valor / total) * 100 #Cálculo dos percentuais de representação de cada item no dicionário e grava no novo dicionário chamado "percentuais"
    return percentuais #Retorna o novo dicionário

faturamento = {
'SP' : 67836.43,
'RJ' : 36678.66,
'MG' : 29229.88,
'ES' : 27165.48,
'Outros' : 19849.53,
}

resultado = calculo_percent(faturamento) #Chamada da função construída acima

for estado, percentual in resultado.items(): #Loop que percorre cada item no dicionário "percentuais", retornado pela função
    print(f'{estado}:{percentual:.2f}%') #Imprime os percentuais de representação de cada estado