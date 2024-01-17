from django.db import models

# Create your models here.
class Todo(models.Model): # ORM - Object Relational Mapper
    content = models.TextField() # CharField, TextField