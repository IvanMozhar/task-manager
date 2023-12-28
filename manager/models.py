from django.contrib.auth.models import AbstractUser
from django.db import models


# check unique arguments for models
class Position(models.Model):
    name = models.CharField(max_length=63)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.SET_NULL,
        null=True,
        related_name="workers"
    )

    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class TaskType(models.Model):
    name = models.CharField(max_length=263)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Task(models.Model):
    name = models.CharField(max_length=263)
    description = models.TextField(max_length=600)
    deadline = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField()
    priority_choices = (
        ("Low", "Low"),
        ("Urgent", "Urgent"),
        ("High", "High"),
    )
    priority = models.CharField(
        max_length=63,
        choices=priority_choices
    )
    task_type = models.ForeignKey(
        TaskType,
        on_delete=models.SET_NULL,  # by deleting task type object, task is not deleted
        null=True,
        related_name="tasks"
    )
    assignees = models.ManyToManyField(Worker, related_name="tasks")

    class Meta:
        ordering = ["name"]

    # check str method
    def __str__(self):
        return f"{self.name}: {self.deadline} {self.is_completed}"
