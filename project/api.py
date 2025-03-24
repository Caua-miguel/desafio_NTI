import requests
import time

cnpjs = [
    '82110818000121','82110818000202', '82110818000393',
    '82110818001608', '82110818000806', '82110818002760', 
    '82110818002094', '82110818002507', '82110818002841'
]

list_branches = []

def data_brances():
    for cnpj in cnpjs:
        url = f'https://receitaws.com.br/v1/cnpj/{cnpj}'
        response = requests.get(url)

        if response.status_code == 200:
            brances = response.json()
            list_branches.append({
            'cnpj': brances["cnpj"],
            'name': brances["nome"],
            'city': brances["municipio"],
            'state': brances["uf"]
            })
        else:
            print(f"Erro ao obter dados para o CNPJ {cnpj}. Codigo: {response.status_code}")

        time.sleep(20)
    return list_branches