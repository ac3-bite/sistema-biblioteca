# Sistema de Gerenciamento de Biblioteca

## Objetivo

Desenvolver um sistema para apoiar o gerenciamento de usuários, livros, empréstimos, devoluções, disponibilidade, atrasos e relatórios de uma biblioteca.

## Principais funcionalidades

- Cadastro de usuários;
- Cadastro e alteração de livros;
- Consulta ao acervo;
- Controle de disponibilidade;
- Registro de empréstimos;
- Registro de devoluções;
- Controle de atrasos;
- Histórico de empréstimos;
- Geração de relatórios.

## Estrutura do projeto

```text
sistema-biblioteca/
├── README.md
├── docs/
│   └── requisitos.md
├── src/
│   ├── catalogo.py
│   ├── livro.py
│   ├── usuario.py
│   └── emprestimo.py
└── tests/
    └── test_catalogo.py

Versionamento

Projeto desenvolvido para a atividade prática de Gerência de Configuração.

Versão atual: v1.0.0

Histórico de alterações

Este projeto utiliza Git para registrar e controlar a evolução do sistema durante seu desenvolvimento.

Escopo da versão 1.0.0

Esta versão contempla a estrutura básica do Sistema de Gerenciamento de Biblioteca.

Funcionalidades principais:

Cadastro de livros;
Consulta de livros por título;
Cadastro e identificação de usuários;
Registro de empréstimos e devoluções;
Teste automatizado para consulta do catálogo.

Tecnologias utilizadas:

Python;
Git;
GitHub;
Testes automatizados com pytest.
