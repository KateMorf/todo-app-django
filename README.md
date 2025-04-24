# Todo App

Uma aplicação simples de gerenciamento de tarefas desenvolvida com Django.

## Sobre o Projeto

Este projeto é uma aplicação web de Lista de Tarefas (Todo App) que permite aos usuários criar, visualizar, editar e excluir tarefas. Desenvolvida com Django, esta aplicação demonstra os conceitos fundamentais de desenvolvimento web com este poderoso framework Python.

## Funcionalidades

- Listar todas as tarefas
- Visualizar detalhes de uma tarefa específica
- Adicionar novas tarefas
- Editar tarefas existentes
- Marcar tarefas como concluídas
- Excluir tarefas

## Tecnologias Utilizadas

- Python 3.10+
- Django 5.2
- Bootstrap 5 (para estilização)
- SQLite (banco de dados padrão)

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/todo_app.git
   cd todo_app
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # No Windows
   source venv/bin/activate  # No Linux/Mac
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute as migrações:
   ```bash
   python manage.py migrate
   ```

5. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

6. Acesse a aplicação em `http://127.0.0.1:8000/` localmente ou `https://karolinefarias.pythonanywhere.com`

## Estrutura do Projeto

```
todo_app/
│
├── tasks/                  # Aplicação principal
│   ├── migrations/         # Migrações do banco de dados
│   ├── templates/tasks/    # Templates HTML
│   ├── admin.py            # Configuração do admin
│   ├── forms.py            # Formulários
│   ├── models.py           # Modelos de dados
│   ├── urls.py             # Rotas da aplicação
│   └── views.py            # Views e lógica da aplicação
│
├── todo_app/               # Configurações do projeto
│   ├── settings.py         # Configurações do Django
│   ├── urls.py             # Rotas principais
│   └── wsgi.py             # Configuração WSGI
│
├── manage.py               # Script de gerenciamento
└── requirements.txt        # Dependências do projeto
```

## Como Usar

- Acesse a página inicial para ver a lista de todas as tarefas
- Clique em "Nova Tarefa" para adicionar uma nova tarefa
- Clique no título de uma tarefa para ver seus detalhes
- Na página de detalhes, você pode editar ou excluir a tarefa
- Marque tarefas como concluídas na tela de edição

## Tutorial Completo

Este projeto foi desenvolvido seguindo o tutorial "Desvendando o Django: Desenvolvimento Web Rápido e Eficiente", publicado no Medium. Se você quiser aprender como desenvolver e fazer deploy dessa aplicação passo a passo, confira o tutorial completo:

### Desvendando o Django: Desenvolvimento Web Rápido e Eficiente

**Sumário**
- [Parte 1 — Introdução](https://medium.com/@karoline.farias_18209/desvendando-o-django-desenvolvimento-web-r%C3%A1pido-e-eficiente-parte-1-3c30338727ff)
- [Parte 2 — Pré-requisitos](https://medium.com/@karoline.farias_18209/desvendando-o-django-desenvolvimento-web-r%C3%A1pido-e-eficiente-parte-2-ae030c0f6225)
- [Parte 3 — Preparando o Ambiente](https://medium.com/@karoline.farias_18209/desvendando-o-django-desenvolvimento-web-r%C3%A1pido-e-eficiente-parte-3-641d2d05258b)
- [Parte 4 — Deploy da Aplicação](https://medium.com/@karoline.farias_18209/desvendando-o-django-desenvolvimento-web-r%C3%A1pido-e-eficiente-parte-4-cc548b05d224)
- [Parte 5 — Construção da Aplicação "Lista de Tarefas"](https://medium.com/@karoline.farias_18209/desvendando-o-django-desenvolvimento-web-r%C3%A1pido-e-eficiente-parte-5-1ccb7395f00f)
- [Parte 6 — Estilização e Integração com Bootstrap (Final)](https://medium.com/@karoline.farias_18209/desvendando-o-django-desenvolvimento-web-r%C3%A1pido-e-eficiente-parte-6-final-2185b0b1bd38)
- [Parte 7 - Parte 7 — Desafio Extra: Filtrando e Organizando Tarefas] (https://medium.com/@karoline.farias_18209/desvendando-o-django-desenvolvimento-web-r%C3%A1pido-e-eficiente-parte-7-desafio-extra-b0a31a4d032d)


## Licença

MIT
