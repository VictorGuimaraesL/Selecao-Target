import json
import xml.etree.ElementTree as ET

#Função que recebe o caminho para um arquivo JSON ou XML e retorna o menor valor de faturamento, o maior valor de faturamento e o número de dias no mês em que o valor de faturamento diário foi superior à média mensal
def analisar_faturamento(arquivo):
    try:
        # Tenta carregar o arquivo como JSON
        with open(arquivo, 'r') as f:
            data = json.load(f)
            faturamentos = [item['valor'] for item in data if 'valor' in item]
    except json.JSONDecodeError:
        # Se não for JSON, tenta como XML
        try:
            tree = ET.parse(arquivo)
            root = tree.getroot()
            faturamentos = [float(item.text) for item in root.findall('.//valor') if item.text]
        except ET.ParseError:
            raise ValueError("Formato de arquivo inválido. Deve ser JSON ou XML.")

    # Remove valores nulos ou negativos
    faturamentos = [valor for valor in faturamentos if valor > 0]

    # Calcula o menor, maior valor e a média
    menor_valor = min(faturamentos)
    maior_valor = max(faturamentos)
    media = sum(faturamentos) / len(faturamentos)

    # Conta os dias acima da média
    dias_acima_media = sum(1 for valor in faturamentos if valor > media)

    return menor_valor, maior_valor, dias_acima_media

arquivo = 'faturamento.json'  # Substitua pelo caminho do arquivo
menor, maior, dias_acima_media = analisar_faturamento(arquivo) #Chama a função

print(f"Menor valor: R$ {menor:.2f}") #Imprime o menor valor de faturamento
print(f"Maior valor: R$ {maior:.2f}") #Imprime o maior valor de faturamento
print(f"Número de dias acima da média: {dias_acima_media}") #Imprime número de dias no mês em que o valor de faturamento diário foi superior à média mensal