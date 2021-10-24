from django.shortcuts import redirect, render, get_object_or_404
from .models import Todo
from .forms import TodoAppForm, TodoUpdateForm


def home(request):
    return render(request, "todo/home.html")

# CRUD (CREATE-READ-UPDATE-DELETE) OPERATIONS

# CREATE - READ
def todo_list(request):
    todos = Todo.objects.all()
    form = TodoAppForm()
    if request.method == 'POST':
        form = TodoAppForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {
        'todos': todos,
        'form': form
    }
    return render(request, 'todo/todo_list.html', context)

# UPDATE
def todo_update(request, id):
    todo = get_object_or_404(Todo, id=id)
    form = TodoUpdateForm(instance=todo)
    if request.method == 'POST':
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {
        'form': form,
        'todo': todo,
    }
    return render(request, 'todo/todo_update.html', context)

# DELETE
def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        todo.delete()
        return redirect('list')
    context = {
        'todo': todo
    }
    return render(request, 'todo/todo_delete.html', context)
