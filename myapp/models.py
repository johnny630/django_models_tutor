import uuid
from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    age = models.IntegerField(null=True)
    momey = models.BigIntegerField(null=True)
    data = models.BinaryField(null=True)
    has_child = models.BooleanField(default=False)
    birthdoay = models.DateField(null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    period_at = models.DurationField(null=True)
    email = models.EmailField(null=True)
    ip = models.GenericIPAddressField(null=True)
    info = models.JSONField(null=True)  # New in Django 3.1.
    description = models.TextField(null=True)
    website_url = models.URLField(null=True)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
