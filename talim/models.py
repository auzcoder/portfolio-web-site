
from django.db import models


class Talim(models.Model):
    name = models.CharField(verbose_name="O'qish joyi: ", max_length=200, blank=False, null=False)
    course = models.CharField(verbose_name="Yo'nalish nomi: ", max_length=100, blank=False, null=False)
    content = models.TextField(verbose_name='Qisqacha izoh: ', blank=False, null=False)
    started_at = models.DateField(verbose_name='Boshlanish vaqti: ', null=False, blank=False)
    ended_at = models.DateField(verbose_name='Tugash vaqti: ', blank=True, null=True)
    is_active = models.BooleanField(verbose_name="Hozirgi o'qish joyim: ", default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'Talim'

    def __str__(self):
        return self.name
