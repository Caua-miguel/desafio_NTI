import requests
import time

cnpjs = [
    '82110818000121','82110818000202', '82110818000393',
    '82110818001608', '82110818000806', '82110818002760', 
    '82110818002094', '82110818002507', '82110818002841'
]

lista_filiais = []

def dados_filiais():
    for cnpj in cnpjs:
        url = f'https://receitaws.com.br/v1/cnpj/{cnpj}'
        response = requests.get(url)

        if response.status_code == 200:
            filiais = response.json()
            lista_filiais.append({
            'cnpj': filiais["cnpj"],
            'nome': filiais["nome"],
            'cidade': filiais["municipio"],
            'estado': filiais["uf"]
            })
        else:
            print(f"Erro ao obter dados para o CNPJ {cnpj}. Codigo: {response.status_code}")

        time.sleep(20)
    return lista_filiais
