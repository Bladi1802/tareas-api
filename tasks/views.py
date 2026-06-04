from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from .models import Task
from .serializers import GroupSerializer, TaskSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by("created_at")
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
