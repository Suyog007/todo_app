from django.db import models

class TodoItems(models.Model):
    content = models.TextField(max_length=100)
