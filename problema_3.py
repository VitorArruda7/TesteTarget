import json
import xml.etree.ElementTree as ET

def carregar_json(caminho):
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)

def carregar_xml(caminho):
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()

    xml_corrigido = f"<dados>{conteudo}</dados>"
    root = ET.fromstring(xml_corrigido)
    dados = []
    
    for row in root.findall('row'):
        dia = int(row.find('dia').text)
        valor = float(row.find('valor').text)
        dados.append({'dia': dia, 'valor': valor})
    
    return dados

def resolver():
    caminho_json = "dados.json"
    caminho_xml = "dados.xml"

    dados_json = carregar_json(caminho_json)
    dados_xml = carregar_xml(caminho_xml)
    
    faturamento_diario = dados_json + dados_xml
    valores_diarios = [dia['valor'] for dia in faturamento_diario if dia['valor'] > 0]

    menor_valor = min(valores_diarios)
    maior_valor = max(valores_diarios)
    media_mensal = sum(valores_diarios) / len(valores_diarios)
    dias_acima_da_media = sum(1 for valor in valores_diarios if valor > media_mensal)

    print(f"Menor faturamento diário: R${menor_valor:.2f}")
    print(f"Maior faturamento diário: R${maior_valor:.2f}")
    print(f"Dias acima da média mensal: {dias_acima_da_media}")

if __name__ == "__main__":
    resolver()
