from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    year = models.IntegerField(default=1)
    phone = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} ({self.year} year) - {self.phone}"


class Res(models.Model):
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    time = models.FloatField(max_length=30)

    def __str__(self):
        return f"{self.path} ({self.method}) - {self.time}"
