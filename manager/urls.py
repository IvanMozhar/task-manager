from django.urls import path

from manager.views import (
    index,
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDetailView,
    TaskDeleteView,
    WorkerListView,
    TaskTypeListView,
    TaskTypeCreateView,
    TaskTypeDeleteView,
    TaskTypeDetailView,
    toggle_task_completed,
    WorkerDetailView,
    home_page
)


urlpatterns = [
    path("", index, name="index"),
    path(
        "home/",
        home_page,
        name="home"
    ),
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
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "tasks/<int:pk>/detail/",
        TaskDetailView.as_view(),
        name="task-detail"
    ),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "workers/",
        WorkerListView.as_view(),
        name="worker-list"
    ),
    path(
        "workers/<int:pk>/detail/",
        WorkerDetailView.as_view(),
        name="worker-detail"
    ),
    path(
        "task-types/",
        TaskTypeListView.as_view(),
        name="task-type-list"
    ),
    path(
        "task-types/<int:pk>/detail/",
        TaskTypeDetailView.as_view(),
        name="task-type-detail"
    ),
    path(
        "task-types/create/",
        TaskTypeCreateView.as_view(),
        name="task-type-create"
    ),
    path(
        "task-types/<int:pk>/delete/",
        TaskTypeDeleteView.as_view(),
        name="task-type-delete"
    ),
    path(
        "tasks/<int:pk>/toggle-complete/",
        toggle_task_completed,
        name="task-toggle-complete",
    ),
]

app_name = "manager"
