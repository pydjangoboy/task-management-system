import os
import django
import random
from faker import Faker
from django.utils import timezone

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TaskManager.settings")
django.setup()

from Tasks.models import Task

fake = Faker()


def generate_fake_task():
    title = fake.text(max_nb_chars=50)  # Limit title to 50 characters
    description = fake.text(max_nb_chars=100)  # Limit description to 100 characters
    due_date = fake.future_datetime()
    status = random.choice(['TO_DO', 'IN_PROGRESS', 'DONE'])

    Task.objects.create(
        title=title,
        description=description,
        due_date=due_date,
        status=status
    )


def generate_fake_tasks(num_tasks):
    for _ in range(num_tasks):
        generate_fake_task()


if __name__ == '__main__':
    num_tasks = 10  # You can change this number based on your requirement
    generate_fake_tasks(num_tasks)
    print(f'{num_tasks} fake tasks have been generated.')
