from django.db import models


class Contact(models.Model):
    firstname = models.CharField(max_length=200, null=False, blank=False)
    lastname = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False)
    message = models.TextField(max_length=1500, null=False, blank=False)
