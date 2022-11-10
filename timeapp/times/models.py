from django.db import models

import uuid

from useraccount.models import CustomUser

# Create your models here.

class Client(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, editable=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='', blank=False)
    company = models.CharField(max_length=50, default='', blank=True)
    
