from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class extendeduser(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_num = models.IntegerField()
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    gen = {('male', 'Male'), ('female', 'Female'), ('custom', 'Custom')}
    gender = models.CharField(max_length=20, choices=gen, default="male")