

# 🦺 Gestão EPI Smart

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.x-green?logo=django)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?logo=bootstrap)](https://getbootstrap.com/)
[![SQLite](https://img.shields.io/badge/SQLite-3-lightgrey?logo=sqlite)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

---

**Gestão EPI Smart** é uma aplicação web desenvolvida em **Python/Django**, criada para gerenciar o empréstimo de Equipamentos de Proteção Individual (**EPIs**) em ambientes de trabalho, como a construção civil.

O sistema permite controle detalhado de **colaboradores, equipamentos e empréstimos**, garantindo **segurança** e **conformidade com normas trabalhistas**.

🚀 Projeto desenvolvido como parte da avaliação do curso de **Desenvolvimento de Sistemas**.

---

## ✨ Funcionalidades

* 👷 **Gestão de Colaboradores** – CRUD completo (Criar, Ler, Atualizar, Excluir).
* 🦺 **Gestão de Equipamentos** – CRUD de EPIs, com controle de estoque (total e disponível).
* 📦 **Controle de Empréstimos** – Registro de retirada e devolução vinculados a colaboradores.
* 🔄 **Estoque Automatizado** – Atualização automática do estoque a cada empréstimo/devolução.
* 🔐 **Sistema de Autenticação** – Login e senha, com possibilidade de alterar credenciais.

---

## 🛠️ Tecnologias Utilizadas

* **Backend**: Python, Django
* **Frontend**: HTML, CSS, Bootstrap 5, JavaScript
* **Banco de Dados**: SQLite 3

---

## ⚙️ Como Executar o Projeto Localmente

### 📌 Pré-requisitos

* Python **3.10+**
* Git

### 🚀 Instalação

1. **Clonar o repositório**

   ```bash
   git clone <https://github.com/kouvaxx/Projeto_GestaoEPI_SMART.git>
   cd GestaoEPI_Smart
   ```

2. **Criar e ativar ambiente virtual**

   * **Windows**

     ```bash
     python -m venv .venv
     .\.venv\Scripts\activate
     ```

   * **macOS/Linux**

     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Instalar dependências**

   ```bash
   pip install -r requirements.txt
   ```

4. **Aplicar migrações**

   ```bash
   python manage.py migrate
   ```

5. **Criar superusuário (admin)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Rodar o servidor**

   ```bash
   python manage.py runserver
   ```

7. **Acessar a aplicação**
   👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🔑 Acesso ao Sistema

> Para testes iniciais, utilize as seguintes credenciais:
> **Login:** `admin`
> **Senha:** `admin`

---

## 📂 Estrutura do Projeto

```
GestaoEPI_Smart/
├── core/            # Aplicação principal (models, views, templates)
├── gestao_epi/      # Configurações do projeto Django
├── .gitignore       # Arquivos ignorados pelo Git
├── db.sqlite3       # Banco de dados SQLite
├── manage.py        # Utilitário de linha de comando do Django
└── requirements.txt # Lista de dependências Python
```

---

👨‍💻 **Desenvolvido por:** Jaisson Bertolini

---


