from django.contrib.auth.models import User
from django.db import models


class Cv(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    photo = models.ImageField()


class Experience(models.Model):
    cv = models.ForeignKey(Cv, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    company_name = models.CharField(max_length=128)
    job_position = models.CharField(max_length=128)
    description = models.TextField()


class Skil(models.Model):
    cv = models.ForeignKey(Cv, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)


class Education(models.Model):
    cv = models.ForeignKey(Cv, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    institution_name = models.CharField(max_length=128)


class Contacts(models.Model):
    cv = models.ForeignKey(Cv, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=64)
    email = models.EmailField()
    social_links = models.TextField()
