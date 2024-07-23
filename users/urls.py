
from django.urls import include, path
from rest_framework import routers


from users.views import UserListView

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('users/',UserListView.as_view()),
]