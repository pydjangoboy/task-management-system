import os
from django.core.wsgi import get_wsgi_application
from django.contrib.auth import authenticate
from fastapi import FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from Tasks.models import Task

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TaskManager.settings')
application = get_wsgi_application()

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class TaskUpdate(BaseModel):
    """
    Pydantic model for updating task status.
    """
    status: str


def authenticate_user(username: str, password: str):
    """
    Authenticate a user with the provided username and password.
    """
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
    """
    Endpoint to retrieve a list of all tasks.
    """
    tasks = Task.objects.all()
    return {"tasks": [task.title for task in tasks]}


class TaskData(BaseModel):
    """
    Pydantic model for representing task data.
    """
    title: str
    description: str
    due_date: str
    status: str


@app.get("/tasks/{task_id}")
def read_task(task_id: int):
    """
    Endpoint to retrieve details of a specific task.
    """
    try:
        task = Task.objects.get(id=task_id)
        formatted_due_date = task.due_date.strftime("%m/%d/%Y")
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
    """
    Endpoint to update the status of a specific task.
    """
    task = Task.objects.get(id=task_id)
    task.status = task_update.status
    task.save()
    return {"task": task.title, "status": task.status}
