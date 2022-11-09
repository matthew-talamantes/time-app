from django.db import models

from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
from django.urls import reverse

from PIL import Image
import uuid

# Create your models here.
class CustomUser(AbstractUser):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.username