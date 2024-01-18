## Docker-compose project
- Title: Hogwarts Magic School Student Registration App
- Author: Kavindu Kalinga
- Languages: `python3` , `HTML`
- Framework: `Flask`
- Databse: `postgreSQL`
- Containerization tools and APIs: `Docker`
- Reference: YouTube: [Flask app with PostgreSQL](https://www.youtube.com/watch?v=XZ_gAWdGzZk)  


### CMD
```bash
python ./app.py
```
### Verification:
```
docker images | head
```
| REPOSITORY                         | TAG     | IMAGE ID       | CREATED          | SIZE   |
| ---------------------------------- | ------- | -------------- | ---------------- | ------ |
| python_html_flask_hogwartzwebapp   | latest  | #------------# | 33 minutes ago   | 98.2MB |
| python_html_flask_pgdb2            | latest  | #------------# | 33 minutes ago   | 412MB  |

```
docker ps -a
```
