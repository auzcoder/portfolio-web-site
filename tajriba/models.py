from django.db import models
from cked.fields import RichTextField


class Tajriba(models.Model):
    name = models.CharField(verbose_name='Tajriba nomi: ', max_length=200, blank=False, null=False)
    position = models.CharField(verbose_name='Lavozimi: ', max_length=100, blank=False, null=False)
    content = models.TextField(verbose_name='Qisqacha izoh: ', blank=False, null=False)
    started_at = models.DateField(verbose_name='Boshlanish vaqti: ', null=False, blank=False)
    ended_at = models.DateField(verbose_name='Tugash vaqti: ', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'Tajriba'

    def __str__(self):
        return self.name

