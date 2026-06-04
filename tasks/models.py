from django.db import models
from django_prometheus.models import ExportModelOperationsMixin


class Task(ExportModelOperationsMixin("task"), models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pendiente'),
        ('IN_PROGRESS', 'En progreso'),
        ('COMPLETED', 'Completada'),
    ]

    title = models.CharField(max_length=150)
    description = models.TextField(blank=False)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )
    completed = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)
    owner = models.ForeignKey(
        "auth.User",
        related_name="tasks",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.title
