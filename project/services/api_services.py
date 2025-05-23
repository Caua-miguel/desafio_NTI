import requests
import time
from typing import List, Dict
from logging import error, debug, info

class BranchesAlfa():
    def __init__(self, cnpjs: List[str]):
        self.cnpjs = cnpjs
    
    def get_data_branches(self, cnpj: str) -> Dict[str, str]:
        
        url = f'https://receitaws.com.br/v1/cnpj/{cnpj}'

        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            error(f"Erro ao obter dados para o CNPJ {cnpj}: {e}")
            return {}
        
        if response.status_code == 200:
            date = response.json()
            debug(f"CNPJ added: {cnpj}")
            return {
                'cnpj': date["cnpj"],
                'name': date["nome"],
                'city': date["municipio"],
                'state': date["uf"],
            }
        else:
            error(f"Erro ao obter dados para o CNPJ {cnpj}. Código: {response.status_code}")
            return {}
        
    def collect_branches_data(self) -> List[Dict[str, str]]:

        branches_data = []

        for cnpj in self.cnpjs:
            branche_data = self.get_data_branches(cnpj)
            if branche_data:
                branches_data.append(branche_data)
                info(f"CNPJ: {cnpj} - added successfully!")
                info("Waiting 20 seconds...")
            time.sleep(20)
        return branches_data