## Docker-compose project
- Languages: `python3` , `HTML`
- Framework: `Django`
- Databse: `postgreSQL`
- Cintainerization tools and APIs: `Docker`  


### CMD
```docker
docker-compose run kkwebapp python3 manage.py migrate
docker-compose up
```

### 3 steps of Django migration
```bash
python3 manage.py makemigrations todos
>>> xxx
python3 manage.py sqlmigrate todos xxx
python3 manage.py migrate
```
