from django.db import models
from django.utils import timezone

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    phone = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'