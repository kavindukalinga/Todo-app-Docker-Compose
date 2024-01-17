from django.urls import path
from . import views

# http://0.0.0.0:8000/todos/list/

urlpatterns = [
    path('list/',views.list_todo_items),
    path('insert_todo/',views.insert_todo_item,name='insert_todo_item'),
    path('delete_todo/<int:todo_id>/',views.delete_todo_item,name='delete_todo_item'),
]
