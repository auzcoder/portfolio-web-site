from django.db import models
from cked.fields import RichTextField


class Tajriba(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    started_at = models.DateField()
    ended_at = models.DateField()
    position = models.CharField(max_length=100, blank=False, null=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Tajriba'
        verbose_name_plural = 'Tajriba'

    def __str__(self):
        return self.name

