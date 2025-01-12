from database.database import cursor

def create_filiais():
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS filiais (
        tbf_i_codigo SERIAL PRIMARY KEY,
        tbf_s_cnpj VARCHAR(14) NOT NULL,
        tbf_s_nome VARCHAR(255),
        tbf_s_cidade VARCHAR(255),
        tbf_s_estado CHAR(2)
        );
        '''
    )