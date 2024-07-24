from django.urls import path
from tasks.views import TaskCreateListApiView, TaskUpdateDeleteApiView

urlpatterns = [
    path('', TaskCreateListApiView.as_view(), name='task-list'),
    path('<int:pk>/', TaskUpdateDeleteApiView.as_view(), name='task'),
]
