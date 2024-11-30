from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import RegexValidator,MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
# Create your models here.
class Fasilitas(models.Model):
    fasilitas= models.CharField(max_length=250)
    keunggulan = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.fasilitas

class Kamar(models.Model):
    name = models.CharField(max_length=100)
    fasilitas_kamar = models.TextField(blank=True, null=True)
    image=CloudinaryField('image')
    def __str__(self):
        return self.name


class UserSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.user.username} - {self.session_key}"

