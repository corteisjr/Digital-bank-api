# Digital-bank-api

## Desafio Backend

esté é um projeto feito para  desafio backend.

## Critérios de aceite

- Autenticação(JWT)
- Criar um usuário
- Consultar saldo da carteira de um usuário
- Adicionar saldo à carteira
- Criar uma transferência entre usuários (carteiras)
- Listar transferências realizadas por um usuário, com filtro opcional por período de data

## COnfiguração do ambiente
Siga as etapas abaixo para configurar o ambiente de desenvolvimento

1. Certifique-se de ter o python instalado. Recomenda-se utilizar a versão 3.10 ou superior
2. Clone o repositório para seu a ambiente local
 ``` git clone https://github.com/corteisjr/Digital-bank-api.git ```
3. Acesse o diretório
   ```cd Digital-bank-api```
4. Crie o ambiente virtual para isolar as depedências do projeto.
    ```python3.11 -m venv venv```
5.Ative o ambiente virtual:
-No Windows:
```venv\Scripts\activate```
-No Linux ou macOS:
```source venv/bin/activate```

6. Instale as dependências do projeto:
   ```pip install -r requirements.txt```
7. Configure a base de dados Postgres(Lembre-se de ter o PSQL instalado na sua máquina)
  Para usuários linux
   ```shell
     sudo su postgres
   ```
   De seguida, pqsl

   Crie a a base de dados
      ```shell
         CREATE DATABASE coredb;
      ```
   Para conectar a base de dados, é necessário ter um USER com a Senha
         ```shell
             CREATE USER core WITH PASSWORD 'suasenha';
          ```
   Garantir acesso a base de dados
     ```shell
       GRANT ALL PRIVILEGES ON DATABASE coredb TO core;
     ```
9.  Adicione um arquivo .env
    ```shell
          SECRET_KEY = '...'
          POSTGRES_DB = '...'
          POSTGRES_USER = '...'
          POSTGRES_PASSWORD = '...'
          DB_PORT = '...'
     ```
10.  Execute as migrações do banco de dados:

   ```shell
     python manage.py makemigrations
     python manage.py migrate
   ```
11. Inicie o servidor de desenvolvimento:

   ```shell
     python manage.py runserver
   ```
## COnfiguração do ambiente (Docker)
1. Pré-requisitos
   Antes de começar, certifique-se de que você tem:
   - Docker instalado
   - Docker Compose instalado → Já vem com o Docker nas versões mais recentes
   Para verificar se estão instalados, rode:
   ```
   docker --version
   docker-compose --version
   ```
2. Construir e iniciar os containers
   ```docker-compose up --build```

3. Criar e aplicar migrações do banco
    ```
    docker-compose exec web python manage.py makemigrations
    docker-compose exec web python manage.py migrate
    docker-compose exec web python manage.py createsuperuser
    ```

    #### NB: Não esqueça de adicionar o arquivo .env como mostrado acima!!
