from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    pengguna = models.ForeignKey(User, on_delete=models.CASCADE)
    tanggal = models.DateField(default=timezone.now)
    judul = models.CharField(max_length=50)
    deskripsi = models.TextField()
    status = models.BooleanField(default=False)