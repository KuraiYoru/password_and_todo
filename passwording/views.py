from django.shortcuts import render, redirect, get_object_or_404
from .helper import password
from .forms import TodoForm
from .models import Todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def generate(request):
    if request.method == 'GET':
        return render(request, 'passwording/index.html')
    else:
        if not request.POST['password'].isdigit():
            return render(request, 'passwording/index.html', {'error': 'password must be integer'})
        if not (5 <= int(request.POST['password']) <= 80):
            return render(request, 'passwording/index.html', {'error': 'Password does not match the given length'})
        uppercase = request.POST.get('capital')
        numbers = request.POST.get('numbers')
        symbols = request.POST.get('symbols')
        return render(request, 'passwording/password.html', {'password': password(int(request.POST['password']), uppercase=uppercase, special=symbols,
                                 numbers=numbers)})



@login_required
def createtodo(request):
    if request.method == 'GET':
        return render(request, 'passwording/todos.html', {'form': TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('/mytodos')
        except ValueError:
            return render(request, 'passwording/todos.html',
                          {'form': TodoForm(), 'error': 'Bad data passed in. Try again.'})

@login_required
def currenttodos(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=True)
    paginator = Paginator(todos, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.method == 'GET':

        return render(request, 'passwording/currenttodos.html', {'aaa': page_obj})
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('/mytodos')
        except ValueError:
            return render(request, 'passwording/todos.html',
                          {'form': TodoForm(), 'error': 'Bad data passed in. Try again.'})


@login_required
def viewtodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request, 'passwording/currenttodo.html', {'todo': todo, 'form': form})
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('/mytodos')
        except ValueError:
            return render(request, 'passwording/currenttodo.html', {'todo': todo, 'form': form, 'error': 'Bad info'})


@login_required
def complete(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.datecompleted = timezone.now()
        todo.save()
        return redirect('currenttodos')


@login_required
def delete(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('passed')



def test(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=False)
    paginator = Paginator(todos, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'passwording/passed.html', {'todos': page_obj})



