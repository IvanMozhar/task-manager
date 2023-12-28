from django.test import TestCase

from manager.models import (
    Worker,
    Task,
    TaskType,
    Position
)


class ModelTest(TestCase):
    def test_worker_string_return(self):
        obj = Worker.objects.create()
        self.assertEqual(
            str(obj),
            f"{obj.username} ({obj.first_name} {obj.last_name})"
        )

    def test_type_task_string_return(self):
        obj = TaskType.objects.create()
        self.assertEqual(
            str(obj),
            obj.name
        )

    def test_task_string_return(self):
        task_type = TaskType.objects.create()
        obj = Task.objects.create(
            task_type=task_type,
            is_completed=True
        )
        self.assertEqual(
            str(obj),
            f"{obj.name}: {obj.deadline} {obj.is_completed}"
        )

    def test_position_string_return(self):
        obj = Position.objects.create()
        self.assertEqual(
            str(obj),
            obj.name
        )
