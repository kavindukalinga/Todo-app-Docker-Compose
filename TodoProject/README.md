## Docker-compose project
- Title: Todo - Task writing App
- Author: Kavindu Kalinga
- Languages: `python3` , `HTML`
- Framework: `Django`
- Databse: `postgreSQL`
- Containerization tools and APIs: `Docker`
- Reference:
- - YouTube:
  - - [Build Django To-Do App with PostgreSQL](https://youtu.be/Nnoxz9JGdLU?si=s_GEqClwIGInNs9i)
    - [Docker volumes](https://www.youtube.com/watch?v=eJrR1X38pk4)
    - [Pagination](https://www.youtube.com/watch?v=N-PB-HMFmdo)    

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

```
docker ps -a
```
