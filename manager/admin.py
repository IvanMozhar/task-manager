from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from manager.models import Worker, TaskType, Task, Position


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("name", )


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    search_fields = ("name", )
