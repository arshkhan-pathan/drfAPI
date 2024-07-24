from django.shortcuts import  get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from tasks.models import Tasks
from tasks.serializers import TasksSerializer


# Create your views here.
class TaskViewSet(viewsets.ViewSet):
    queryset = Tasks.objects.all()
    serializer = TasksSerializer(queryset, many=True)
    def list(self, request):
        return Response(self.serializer.data)

    def retrieve(self, request, pk=None):
        return Response(self.serializer.data)
