from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # question(NMC): What is the value of the 'type' attribute?
    type = models.IntegerField()
    company = models.CharField(max_length=50, blank=True, default="")
