import requests
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TaskForm
from .models import Task


def task_list(request):
    """
    View function to display a list of tasks based on user input query.
    """
    query = request.GET.get('q', '')

    if query:
        tasks = Task.objects.filter(
            Q(title__icontains=query) | Q(status__icontains=query)
        ).order_by('-id')  # Order by the 'id' field in descending order (latest first)
    else:
        tasks = Task.objects.all().order_by('-id')  # Order by the 'id' field in descending order (latest first)

    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'query': query})


def task_detail(request, pk):
    """
    View function to display the details of a specific task.
    """
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})


def task_new(request):
    """
    View function to create a new task.
    """
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()

            # Add a success message
            messages.success(request, 'Task created successfully.')

            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_edit.html', {'form': form})


def task_edit(request, pk):
    """
    View function to edit an existing task.
    """
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            messages.success(request, 'Task updated successfully.')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/task_edit.html', {'form': form, 'task': task})


def task_delete(request, pk):
    """
    View function to delete an existing task.
    """
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        # User has confirmed the delete action
        task.delete()
        messages.success(request, f'Task "{task.title}" deleted successfully.')
        return redirect('task_list')

    return render(request, 'tasks/task_confirm_delete.html', {'task': task})


def fastapi_task_detail(request, task_id):
    """
    View function to retrieve and display details of a FastAPI task.
    """
    response = requests.get(f'http://localhost:8081/tasks/{task_id}')
    task = response.json()['task']
    return render(request, 'fastapi/task_detail.html', {'task': task})
