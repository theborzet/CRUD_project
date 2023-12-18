from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=128, blank=True)
    description = models.TextField(blank=True)
    complited = models.BooleanField(default=False)