from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

class UIForm(models.Model):
    created_at = models.DateTimeField(default=datetime.now())
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

class UIFormField(models.Model):
    FIELD_TYPE_CHOICES = (
        ('b', 'Boolean'),
        ('i', 'Integer'),
        )
    field_type = models.CharField(max_length=1, choices=FIELD_TYPE_CHOICES)
    created_at = models.DateTimeField(default=datetime.now())
    label = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    ui_form = models.ForeignKey(UIForm)
