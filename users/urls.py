
from django.urls import include, path
from rest_framework import routers


from users.views import UserListView, UserLoginView

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', UserListView.as_view()),
    path('login/', UserLoginView.as_view()),
]