from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest
from .models import Todo

#exception db
from django.db.utils import OperationalError

# import pagination stuff
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

# def list_todo_items(request):
#     context= {'todo_list' : Todo.objects.all() }
#     return render(request,'todos/todo_list.html', context)
def list_todo_items(request):
    try:
        context = Todo.objects.all()
        p = Paginator(Todo.objects.all().order_by('-id'), 2)
        page = request.GET.get('page')
        contexts = p.get_page(page)
        return render(request, 'todos/todo_list.html', {'todo_list': context, 'contexts': contexts})

    except OperationalError as e:
        return render(request, 'todos/database_unavailable.html')

    except EmptyPage:
        contexts = p.page(p.num_pages)
        return render(request, 'todos/todo_list.html', {'todo_list': context, 'contexts': contexts})

    except PageNotAnInteger:
        contexts = p.page(1)
        return render(request, 'todos/todo_list.html', {'todo_list': context, 'contexts': contexts})



def insert_todo_item(request:HttpRequest):
    todo  = Todo(content = request.POST['content'])
    todo.save()
    return redirect('/todos/list/')

def delete_todo_item(request:HttpRequest,todo_id):
    todo_to_delete = Todo.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect('/todos/list/')