# Todo-app-Docker-Compose
This repo contains a Todo App created using python frameworks and containerized using Docker and Docker-compose


```docker
docker-compose run kkwebapp python3 manage.py migrate
docker-compose up
```

### Useful Docker Commands for this project
```docker
docker image ls
docker image rm -f xxx

docker ps -a
docker container rm -f $(docker container ls -aq)

docker-compose up
docker-compose down
```

### 3 steps of Django migration
```bash
python3 manage.py makemigrations todos
>>> xxx
python3 manage.py sqlmigrate todos xxx
python3 manage.py migrate
```
