from django.db import models
from colorfield.fields import ColorField
from cked.fields import RichTextField


class Texnologiyalar(models.Model):
    name = models.CharField(verbose_name='Texnologiya nomi: ', max_length=50, blank=False, null=False)
    color = ColorField(default='#007bff')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Texnologiyalar'

    def __str__(self):
        return self.name


class Loyiha(models.Model):
    name = models.CharField(verbose_name='Tajriba nomi: ', max_length=200, blank=False, null=False)
    center = models.CharField(verbose_name='Ishlagan joyi: ', max_length=100, blank=False, null=False)
    # iframe = RichTextField(verbose_name='Qisqacha izoh: ', blank=False, null=False)
    content = RichTextField(verbose_name="Barcha ma'lumotlar: ", blank=False, null=False)
    started_at = models.DateField(verbose_name='Boshlanish vaqti: ', null=False, blank=False)
    ended_at = models.DateField(verbose_name='Tugash vaqti: ', blank=True, null=True)
    is_active = models.BooleanField(verbose_name='Hozirgi ish joyim: ', default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Lohiyalar'

    def __str__(self):
        return self.name
