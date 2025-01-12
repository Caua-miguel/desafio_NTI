import re
from api import dados_filiais
from database.database import cursor

dados = dados_filiais()

def insert_filiais():
    
    for filial in dados: 
        filial['cnpj'] = re.sub(r'\D','', filial['cnpj'])
        try:
            cursor.execute(
                """
                INSERT INTO filiais (tbf_s_cnpj, tbf_s_nome, tbf_s_cidade, tbf_s_estado) VALUES (%s, %s, %s, %s)
                """, (filial['cnpj'], filial['nome'], filial['cidade'], filial['estado'])
                )
        except Exception as e:
            print(f'Ocorreu um erro: {e}')   


