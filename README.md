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

**Opcional**
Você pode, também, adicionar um "MODE" para seu projeto. Esse modo vai escolher qual o tipo de ambiente
o projeto vai roda, podendo ser: produção, teste e desenvolvimento. Para escolher, você pode colocar no seu arquivo `.env` os modos:

- PRODUCTION
- DEVELOPMENT
- TESTING

Ex:

`MODE=PRODUCTION`

Caso não adicione nenhum modo, o programa vai pegar o modo de desenvolvimento por padrão.

## Execução do projeto

**Com o `.env` configurado**, podemos iniciar e ajustar o banco de dados sqlite, seguindo a própria documentação do flask-migrate

```shell
pip install --upgrade -r requirements.txt

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

Após 3 minutos, os dados vão ser inseridos no banco sqlite e podem ser visualizados com a rota `/` ou apenas com o endereço do localhost, também em método GET:

`http://127.0.0.1:5000/`
