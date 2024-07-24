
from django.urls import include, path
from rest_framework import routers
from tasks.views import TaskViewSet

# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r'', TaskViewSet)

urlpatterns = [
    path('', include(router.urls))
    ]
