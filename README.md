# Desafio NTI

Projeto para resolver o desafio bonus do NTI da Alfa Transportes. Os dados foram puxados da API https://receitaws.com.br/api por cnpj.

## Principais tecnologias

- python == 3.11.9

As bibliotecas usadas para o projeto funcionar podem ser encontradas no requirementes.py.

## Funcionamento do projeto

Para rodar o projeto você precisa criar sua pasta .env para armazenar a chave secreta do flask e seguir os seguintes passos:

Instalação dos requisitos

`pip install -r requirements.txt`

Iniciar e ajustar o banco de dados sqlite, seguindo a própria documentação do flask-migrate

```
flask db init

flask db migrate

flask db upgrade
```
Em seguida, basta executar o arquivo app.py

`python app.py`

Com a api rodando localmente, use a rota `/filiais` para inserir os dados. A requisição está no método GET:

`http://127.0.0.1:5000/filiais`
