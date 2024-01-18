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
### Verification:
```
docker images | head
```
| REPOSITORY                         | TAG     | IMAGE ID       | CREATED          | SIZE   |
| ---------------------------------- | ------- | -------------- | ---------------- | ------ |
| todoproject_kkwebapp               | latest  | #------------# | 33 minutes ago   | 1.08GB |
| todoproject_pgdb1                  | latest  | #------------# | 33 minutes ago   | 412MB  |
