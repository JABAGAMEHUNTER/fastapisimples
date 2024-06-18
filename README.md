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
- Students can see the sections and content blocks for individual courses that they are taking.
- Students are able to see their progress for each course.

## Running the App Locally

1. Make sure Python, Poetry, and Postgres are installed. Postgres must be running. *If you need help with this, please follow the instructions in the video linked at the top of this README.*
2. Create a virtual environment: `python -m venv venv`
3. Install packages: `poetry install`
4. Run the development server: `uvicorn main:app --reload`

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

*This model is used for teachers to assign courses to students. The 'completed' boolean is False until the student has completed the whole course.*

- student_id
- course_id
- completed

**CompletedContentBlock**

*Every time the student completes a content block, a row is created in this table. The teacher can then go and edit this information when they grade the content block and provide feedback.*

- student_id
- content_block_id
- url
- feedback
- grade
