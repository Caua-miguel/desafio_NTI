# Desafio NTI

Projeto para resolver o desafio bonus do NTI da Alfa Transportes. Os dados foram puxados da API https://receitaws.com.br/api por cnpj.

## Principais tecnologias

- python == 3.11.9
- postgres == 17.4

As bibliotecas usadas para o projeto funcionar podem ser encontradas no requirementes.py.

## Como o programa funciona

O projeto está dividido em várias partes, cada uma com uma responsabilidade específica:

- main: Responsável por executar o fluxo principal do programa.
- config: Contém funções auxiliares e configurações gerais.
- api: Faz as requisições dos dados, uma a cada 20 segundos para seguir a regra de 3 por minuto da API, utilizando o CNPJ e armazena as informações em uma lista.
- database: Responsável pela interação com o banco de dados, incluindo:
  - Conexão com o banco.
  - Criação das tabelas.
  - Inserção de dados: Além de realizar o insert, esse módulo também trata o CNPJ, que chega da API com 18 caracteres, ajustando-o para 14 caracteres (apenas números) antes de inserir no banco.
