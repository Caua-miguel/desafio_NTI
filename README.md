# Desafio NTI

Projeto para resolver o desafio bonus do NTI da Alfa Transportes. Os dados foram puxados da API https://receitaws.com.br/api por cnpj. 

É importante lembrar que a api só permite três requisições por minuto, portanto, o programa vai rodar ao longo de três minutos para retornar os dados.

## Requisitos

- python == 3.11.9

### Tecnologias Utilizadas

As bibliotecas usadas para o projeto funcionar podem ser encontradas no `requirements.txt`.

- **Flask**: Framework para criação da API
- **SQLite**: Banco de dados utilizado no projeto
- **Flask-Migrate**: Para gerenciamento de migrações do banco de dados

## Preparação

As dependências do projeto estão listadas no arquivo `requirements.txt`.

1. **Renomeie o arquivo `.env.example` para `.env`**.
2. **Adicione sua chave secreta (secret key)** no arquivo `.env`.

Essa chave é **necessária** para o funcionamento adequado do projeto.

## Execução do projeto

Iniciar e ajustar o banco de dados sqlite, seguindo a própria documentação do flask-migrate

```shell
python -m flask db init

python -m flask db migrate

python -m flask db upgrade
```
Em seguida, basta executar o arquivo app.py

```shell
python app.py
```

## Testando a aplicação

Com a api rodando localmente, use a rota `/filiais` para inserir os dados. A requisição está no método GET:

`http://127.0.0.1:5000/filiais`
