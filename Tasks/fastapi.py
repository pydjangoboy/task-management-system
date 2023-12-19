import os
from datetime import date

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TaskManager.settings')
application = get_wsgi_application()

from django.contrib.auth import authenticate
from fastapi import FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

from Tasks.models import Task

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class TaskUpdate(BaseModel):
    status: str


def authenticate_user(username: str, password: str):
    user = authenticate(username=username, password=password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


@app.get("/tasks/")
def read_tasks():
    tasks = Task.objects.all()
    return {"tasks": [task.title for task in tasks]}


class TaskData(BaseModel):
    title: str
    description: str
    due_date: str  # Change the type to string for formatted date
    status: str


@app.get("/tasks/{task_id}")
def read_task(task_id: int):
    # Assume you have a Task model in Django
    from Tasks.models import Task

    try:
        # Fetch the task from the database based on task_id
        task = Task.objects.get(id=task_id)

        # Format the due_date to "MM/DD/YYYY" string
        formatted_due_date = task.due_date.strftime("%m/%d/%Y")

        # Convert the Django model to a Pydantic model for serialization
        task_data = TaskData(
            title=task.title,
            description=task.description,
            due_date=formatted_due_date,
            status=task.status
        )

        return {"task": task_data}
    except Task.DoesNotExist:
        raise HTTPException(status_code=404, detail="Task not found")


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_update: TaskUpdate):
    task = Task.objects.get(id=task_id)
    task.status = task_update.status
    task.save()
    return {"task": task.title, "status": task.status}
