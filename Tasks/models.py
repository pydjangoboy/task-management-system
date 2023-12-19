from django.db import models

# Create your models here.
from django.db import models


class Task(models.Model):
    STATUS_CHOICES = [
        ('TO_DO', 'To Do'),
        ('IN_PROGRESS', 'In Progress'),
        ('DONE', 'Done'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TO_DO')

    def __str__(self):
        return f"{self.id} - {self.title}"
