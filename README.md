# dnd-player-tools

## The Stack
* Python 3.8
* FastApi
* Postgres
* Alembic
* SQLAlechemy
* Vue
* Docker

## Things to focus on: 
* write tests for everything
* use dependency injection
* use docker to compose db, frontend, backend
* look at kubernetes how to scale a system like this.

## Ports and logins:
PG admin hosted on:
localhost:5050
username: pgadmin4@pgadmin.org
password: admin

connecting to db: 
server create -> connection
host: db
port: 5432
maintinance_db: test_db
username: postgres
password: admin

fast api is hosted on:
localhost:8000


## VS Code settings:
Python extension
Pylint extension

use these settings

```
"python.autoComplete.extraPaths": ["src/api"],
"python.analysis.extraPaths": ["src/api"]
```

If vscode fails to lint etc, select the virtual environment as the interpreter
```
ctrl+shift+p
python select interpreter
venv/Scripts/python  
```
To enable vscode formatting add this to user settings JSON
```
"python.formatting.autopep8Args": ["--max-line-length", "120", "--experimental"],
```


## Getting started without docker:
Start venv in terminal (bash)
```
cd src/api
py -m venv venv
source venv/Scripts/activate
```
Installing requirements
```
pip install pipenv
pipenv install
```

deactivating

```
deactivate
```

```
uvicorn main:app --reload
```

```
pipenv install alembic
```


```
alembic revision -c src/api/alembic.ini revision --autogenerate -m "migration name"
```

```
alembic -c src/api/alembic.ini upgrade head
```



## Docker get started (Preffered way)

build docker containers
```
docker-compose build   

```
bring up local env

```
docker-compose up

```
open a shell inside container

```
docker exec -it dnd-player-tools-web-1 bash
```
create migration

```
docker-compose run web alembic revision -c src/api/alembic.ini revision --autogenerate -m "migration name"

```
apply migration to container

```
docker-compose run web alembic -c src/api/alembic.ini upgrade head

```