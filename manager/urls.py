from django.urls import path

from manager.views import (
    index,
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "tasks/",
        TaskListView.as_view(),
        name="task-list"
    ),
    path(
        "tasks/create/",
        TaskCreateView.as_view(),
        name="task-create"
    ),
    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view()
    )
]

app_name = "manager"
