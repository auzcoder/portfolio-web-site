from django.db import models
from colorfield.fields import ColorField
from tinymce import models as tinymce_models
from django.contrib.auth.models import User


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


class Tag(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Tag nomi: ')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Maqola(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Muxarrir: ',
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        default=1
    )
    name = models.CharField(verbose_name='Loyiha nomi: ', max_length=200, blank=False, null=False)
    description = models.CharField(verbose_name="Qisqa izoh: ", max_length=500, blank=False, null=False)
    menu = models.ForeignKey(
        Menu,
        verbose_name="Menyuni tanlang: ",
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    content = tinymce_models.HTMLField(verbose_name="Barcha ma'lumotlar: ", blank=False, null=False)
    image = models.ImageField(
        verbose_name="Maqola rasmi",
        blank=True,
        null=True,
        upload_to='Loyiha/',
        default='assets/pythondjango.jpg'
    )
    is_active = models.BooleanField(verbose_name='Nashr etilsinmi? : ', default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Maqolalar'

    def __str__(self):
        return self.name

