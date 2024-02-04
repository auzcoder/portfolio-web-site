from django.db import models


class Contact(models.Model):
    firstname = models.CharField(max_length=200, null=False, blank=False)
    lastname = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False)
    message = models.TextField(max_length=1500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Aloqalar'

    def __str__(self):
        return self.firstname


class About(models.Model):
    fullname = models.CharField(max_length=240, null=False, blank=False)
    position = models.CharField(max_length=240, null=False, blank=False)
    manzil = models.CharField(max_length=240, null=False, blank=False)
    email = models.EmailField(max_length=240, null=False, blank=False)
    image = models.ImageField(null=False, blank=False, upload_to='About/')


