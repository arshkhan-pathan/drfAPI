from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from tasks.models import Tasks
from tasks.serializers import TasksSerializer
from tasks.permissions import IsOwner

class TaskCreateListApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tasks = Tasks.objects.filter(created_by=request.user)
        serializer = TasksSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TasksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskUpdateDeleteApiView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]

    def get(self, request, pk=None):
        task = get_object_or_404(Tasks, pk=pk, created_by=request.user)
        serializer = TasksSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk=None):
        task = get_object_or_404(Tasks, pk=pk, created_by=request.user)
        serializer = TasksSerializer(task, data=request.data)
        print("serializer", serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        task = get_object_or_404(Tasks, pk=pk, created_by=request.user)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
