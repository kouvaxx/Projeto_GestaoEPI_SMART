# Gestão EPI Smart

*Sistema de Gestão de Equipamentos de Proteção Individual desenvolvido com Python e Django.*

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.x-green?logo=django)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?logo=bootstrap)](https://getbootstrap.com/)

---

## Tabela de Conteúdos

* [Sobre o Projeto](#sobre-o-projeto)
* [Tecnologias Utilizadas](#tecnologias-utilizadas)
* [Configuração do Ambiente Local](#configuração-do-ambiente-local)
* [Estrutura do Projeto](#estrutura-do-projeto)
* [Licença](#licença)

---

## Sobre o Projeto

O **Gestão EPI Smart** é uma aplicação web que resolve a necessidade de controlo e gestão de Equipamentos de Proteção Individual (EPIs) em ambientes de trabalho. A plataforma oferece uma solução centralizada para registar, monitorizar e gerir a distribuição e devolução de EPIs, garantindo a segurança dos colaboradores e a conformidade com as normas de segurança.

### Funcionalidades Principais

*   **Gestão de Colaboradores:** CRUD (Criar, Ler, Atualizar, Excluir) de registos de colaboradores.
*   **Gestão de Equipamentos:** CRUD de EPIs, com controlo de quantidade total e disponível em stock.
*   **Gestão de Empréstimos:** Registo de empréstimos de EPIs a colaboradores, com data de empréstimo e devolução.
*   **Controlo de Stock:** Atualização automática do stock de equipamentos após cada operação de empréstimo ou devolução.
*   **Sistema de Autenticação:** Controlo de acesso com login/logout para utilizadores autorizados.
*   **Upload de Foto de Perfil:** Permite aos utilizadores personalizar os seus perfis com uma foto.
*   **Páginas de Ajuda e Sobre:** Secções informativas sobre o projeto e o seu funcionamento.
*   **Interface Moderna:** Tema visual desenvolvido com Bootstrap 5, totalmente responsivo.

---

## Tecnologias Utilizadas

*   **Python:** Linguagem de programação principal.
*   **Django:** Framework web para o desenvolvimento do backend.
*   **Bootstrap 5:** Framework CSS para a estilização e responsividade da interface.
*   **SQLite:** Sistema de gestão de base de dados para o ambiente de desenvolvimento.
*   **HTML/CSS/JavaScript:** Tecnologias padrão para a construção do frontend.

---

## Configuração do Ambiente Local

Siga os passos abaixo para configurar e executar o projeto no seu ambiente de desenvolvimento local.

### Pré-requisitos

*   **Python 3.x:** [Descarregar Python](https://www.python.org/downloads/)
*   **pip:** Gestor de pacotes do Python (normalmente instalado com o Python).
*   **Git:** [Descarregar Git](https://git-scm.com/downloads)

### Passo a Passo

1.  **Clonar o Repositório**

    ```bash
    git clone https://github.com/seu-usuario/gestao-epi-smart.git
    cd gestao-epi-smart
    ```

2.  **Criar e Ativar o Ambiente Virtual**

    *   **Windows:**
        ```bash
        python -m venv .venv
        .\.venv\Scripts\activate
        ```

    *   **macOS/Linux:**
        ```bash
        python3 -m venv .venv
        source .venv/bin/activate
        ```

3.  **Instalar as Dependências**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configurar a Base de Dados**

    Execute o comando abaixo para criar as tabelas da base de dados.

    ```bash
    python manage.py migrate
    ```

5.  **Criar um Superutilizador**

    Crie um utilizador administrador para aceder à área de administração do Django.

    ```bash
    python manage.py createsuperuser
    ```
    *Siga as instruções no terminal para definir o nome de utilizador, email e palavra-passe.*

6.  **Executar o Servidor**

    ```bash
    python manage.py runserver
    ```

    A aplicação estará disponível no seu navegador em: **http://127.0.0.1:8000/**

---

## Estrutura do Projeto

```
/
|-- gestao_epi/         # Ficheiros de configuração do projeto Django.
|-- core/               # Aplicação principal do projeto (models, views, forms, etc.).
|-- templates/          # Ficheiros HTML.
|-- static/             # Ficheiros estáticos (CSS, JS, imagens).
|-- media/              # Ficheiros de upload (fotos de perfil).
|-- requirements.txt    # Lista de dependências do projeto.
|-- manage.py           # Utilitário de linha de comando do Django.
`-- db.sqlite3          # Base de dados SQLite.
```

---

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o ficheiro `LICENSE` para mais detalhes.
