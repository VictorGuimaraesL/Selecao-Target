def calculo_percent(dados):
    total = sum(dados.values())
    percentuais = {}
    for estado, valor in dados.items():
        percentuais[estado] = (valor / total) * 100
    return percentuais

faturamento = {
'SP' : 67836.43,
'RJ' : 36678.66,
'MG' : 29229.88,
'ES' : 27165.48,
'Outros' : 19849.53,
}

resultado = calculo_percent(faturamento)

for estado, percentual in resultado.items():
    print(f'{estado}:{percentual:.2f}%')