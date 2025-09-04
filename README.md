# Gestão EPI Smart

**Gestão EPI Smart** é uma aplicação web desenvolvida em Python com o framework Django, criada para gerir o empréstimo de Equipamentos de Proteção Individual (EPIs) em ambientes de trabalho, como na construção civil. O sistema permite um controlo detalhado de colaboradores, equipamentos e dos empréstimos realizados, garantindo a segurança e a conformidade com as normas de trabalho.

Este projeto foi desenvolvido como parte da avaliação do curso de Desenvolvimento de Sistemas.

## Desenvolvedor: JAISSON BERTOLINI 

## Funcionalidades Principais

* **Gestão de Colaboradores:** CRUD (Criar, Ler, Atualizar, Excluir) completo para o registo de funcionários.
* **Gestão de Equipamentos:** CRUD completo para todos os EPIs, com controlo de stock (quantidade total e disponível).
* **Controlo de Empréstimos:** Sistema para registar a retirada e a devolução de equipamentos, associando-os a um colaborador.
* **Controlo de Stock Automatizado:** O stock de um equipamento é atualizado automaticamente sempre que um empréstimo ou devolução é realizado.
* **Sistema de Autenticação:** Acesso ao sistema protegido por login e senha, com uma página para que o administrador possa alterar as suas credenciais.

## Tecnologias Utilizadas

* **Backend:** Python, Django
* **Frontend:** HTML, CSS, Bootstrap 5, JavaScript
* **Base de Dados:** SQLite 3 (padrão do Django)

## Como Executar o Projeto Localmente

Siga os passos abaixo para configurar e executar o projeto no seu ambiente de desenvolvimento.

### Pré-requisitos

* Python 3.10 ou superior
* Git (para clonar o repositório)

### Passos de Instalação

1.  **Clone o repositório:**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO_GIT>
    cd Gestao_EPI_Smart
    ```

2.  **Crie e ative um ambiente virtual:**
    * No Windows:
        ```bash
        python -m venv .venv
        .\.venv\Scripts\activate
        ```
    * No macOS/Linux:
        ```bash
        python3 -m venv .venv
        source .venv/bin/activate
        ```

3.  **Instale as dependências do projeto:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplique as migrações da base de dados:**
    Este comando cria as tabelas necessárias na base de dados.
    ```bash
    python manage.py migrate
    ```

5.  **Crie um superutilizador (administrador):**
    Você precisará de um utilizador para aceder ao sistema. Siga as instruções no terminal para criar o seu utilizador. Para cumprir os requisitos do projeto, pode usar `admin` como nome de utilizador e senha.
    ```bash
    python manage.py createsuperuser
    ```

6.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

7.  **Aceda à aplicação:**
    Abra o seu navegador e aceda a [http://127.0.0.1:8000/](http://127.0.0.1:8000/). Você será redirecionado para a página de login. Utilize as credenciais que acabou de criar.

## Estrutura do Projeto

```
Gestao_EPI_Smart/
├── core/             # Aplicação principal com modelos, views e templates
├── gestao_epi/       # Ficheiros de configuração do projeto Django
├── .gitignore        # Ficheiros a serem ignorados pelo Git
├── db.sqlite3        # Ficheiro da base de dados
├── manage.py         # Utilitário de linha de comando do Django
└── requirements.txt  # Lista de dependências Python
```
