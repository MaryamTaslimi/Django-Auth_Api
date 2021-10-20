from django.db import models


# Create your models here.
class Person(models.Model):
    email = models.CharField(max_length=60, null=True, blank=False)
    otp = models.CharField(max_length=6, null=True, blank=False)

    def __str__(self):
        return self.email
