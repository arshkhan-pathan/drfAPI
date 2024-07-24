from django.contrib.auth import get_user_model
from rest_framework import serializers

from tasks.models import Tasks, User
from users.serializers import UserLoginSerializer


class TasksSerializer(serializers.ModelSerializer):
    created_by = UserLoginSerializer(read_only=True)
    class Meta:
        model = Tasks
        fields = "__all__"

    def create(self, validated_data):
        created_by = get_user_model().objects.get(id=1)
        return Tasks.objects.create(**validated_data, created_by=created_by)

    def update(self, instance, validated_data):
        return instance.update(**validated_data)
