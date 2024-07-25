from rest_framework import serializers
from tasks.models import Tasks, User
from users.serializers import UserLoginSerializer


class TasksSerializer(serializers.ModelSerializer):
    created_by = UserLoginSerializer(read_only=True)

    class Meta:
        model = Tasks
        fields = ['id', 'name', 'description', 'created_at', 'is_Pending', 'created_by']
