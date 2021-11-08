from django.db import models
from django.contrib.auth.models import User


class Advisor(models.Model):
    name = models.CharField(max_length=150)
    users = models.ManyToManyField(User, through="Call")

    def __str__(self):
        return self.name


class Call(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    advisor = models.ForeignKey(Advisor, on_delete=models.CASCADE)
    booking_time = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} - with {self.advisor.name} at {self.booking_time}"
