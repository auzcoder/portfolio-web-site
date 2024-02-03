from django.db import models
from colorfield.fields import ColorField
from tinymce import models as tinymce_models


class Menu(models.Model):
    name = models.CharField(verbose_name='Menu nomi: ', max_length=150, blank=False, null=False)
    color = ColorField(default='#007bff')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Menyular'

    def __str__(self):
        return self.name


class Loyiha(models.Model):
    name = models.CharField(verbose_name='Loyiha nomi: ', max_length=200, blank=False, null=False)
    description = models.CharField(verbose_name="Qisqa izoh: ", max_length=500, blank=False, null=False)
    menu = models.ForeignKey(Menu, verbose_name="Menyuni tanlang", null=False, blank=False, on_delete=models.CASCADE)
    content = tinymce_models.HTMLField(verbose_name="Barcha ma'lumotlar: ", blank=False, null=False)
    image = models.ImageField(verbose_name="Post rasmi", blank=True, null=True, upload_to='Loyiha/')
    started_at = models.DateField(verbose_name='Boshlanish vaqti: ', null=False, blank=False)
    ended_at = models.DateField(verbose_name='Tugash vaqti: ', blank=True, null=True)
    link = models.URLField(verbose_name="Githubdagi linki: ", null=True, blank=True)
    is_active = models.BooleanField(verbose_name='Hozirgi ishlab chiqarish jarayonida: ', default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Lohiyalar'

    def __str__(self):
        return self.name

