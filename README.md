# Docker-Compose Example Projecs
This repo contains two apps  
1. [Todo App](https://github.com/kavindukalinga/Todo-app-Docker-Compose/tree/main/TodoProject)
2. [Hogwarts registration App](https://github.com/kavindukalinga/Todo-app-Docker-Compose/tree/main/Python_HTML_flask)

created using python frameworks
- `Django`
- `Flask`  

using `postgreSQL` as the database and

containerized using `Docker` and `Docker-compose` .
 

### Useful Docker Commands for this project
```docker
docker image ls
docker image rm -f xxx

docker ps -a
docker container rm -f $(docker container ls -aq)

docker-compose up
docker-compose down
```

### Port settings
```bash
sudo lsof -i :5432
sudo kill -9 1380
```
