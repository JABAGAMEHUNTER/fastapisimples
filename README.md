# Fast API simples

Este repo segue o tutorial contido em este video: https://youtu.be/gQTRsZpR7Gw

Voce pode seguir o tutorial para recriar do zero o projeto.

## Table of Contents

1. [Sobre e Requisitos](#requisitos)
1. [Executando localmente](#executando)
1. [Tech Stack](#tech-stack)
1. [Schema](#schema)

## Requisitos

Este sistema permite gerenciar alunos de cursos, no quais professores podem checar os cursos em que os alunos se encontram inscritos.

- Professores podem performar CRUD em alunos.
- Professores podem criar cursos com sessoes e blocos de conteudo para cada sessao.
- Professores podem associar cursos a estudantes.
- Estudantes podem interagir com os seus cursos em uma lista.
- Estudantes podem ver as seessoes e blocos de conteudo de cursos individuais que estao estudando.
- Estudantes podem ver seu progresso para cada curso.

## Executando

1. Assegure-se deu que Python, Poetry e Postgres estao instalados. Processo do Postgres deve estar funcionando.
2. Crie o ambiente virtual: `python -m venv venv`
3. Instale os pacotes: `poetry install`
4. Execute o server de desenvolvimento: `uvicorn main:app --reload`

## Tech Stack

- Fast API
- Python 3.9+
- Poetry
- Postgres
- SQL Alchemy 1.4+
- Alembic
- Pydantic
- Black
- Flake8
- Pre-commit

## Schema

**User**

- email: str
- role: enum (student, teacher)
- is_active: bool

**Profile**

- first_name: str
- last_name: str
- bio: str (TextField)
- user_id: fk

**Course**

- title: str
- description: str (TextField)
- user_id: fk

**Section**

- title
- description
- course_id

**ContentBlock**

- title
- description
- type
- url
- content
- section_id

**StudentCourse**

*Este modelo sera usado para associar cursos a estudantes. O booleano 'completed' fica False ate o estudante completar o curso inteiro.*

- student_id
- course_id
- completed

**CompletedContentBlock**

*Toda hora que um estudante completa um bloco de conteudo, uma linha sera criada nesta tabela. O professor pode editar esta informacao para darnota e feedback.*

- student_id
- content_block_id
- url
- feedback
- grade
