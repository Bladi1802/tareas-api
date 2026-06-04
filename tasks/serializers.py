variable_no_utilizada = "error_intencional"

from django.contrib.auth.models import Group, User
from rest_framework import serializers

from .models import Task


class UserSerializer(serializers.HyperlinkedModelSerializer):
    tasks = serializers.HyperlinkedRelatedField(
        many=True,
        view_name="task-detail",
        read_only=True
    )

    class Meta:
        model = User
        fields = ["url", "username", "email", "is_staff", "groups", "tasks"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Task
        fields = [
            "url",
            "id",
            "title",
            "description",
            "status",
            "completed",
            "due_date",
            "owner",
            "created_at",
            "updated_at",
        ]
