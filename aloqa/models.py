from django.db import models
from tinymce import models as tinymce_models
from loyiha.models import Texnologiyalar
from colorfield.fields import ColorField


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


class SocialMedia(models.Model):
    name = models.CharField(verbose_name="Tarmoq nomi: ", max_length=200, null=False, blank=False)
    icon = models.CharField(verbose_name="Icon kodi: ", max_length=100, null=False, blank=False)
    link = models.URLField(verbose_name='Havola: ', null=True, blank=True)
    color = ColorField(verbose_name="Media rangi: ", default='#007bff')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Ijtimoiiy medialar: '

    def __str__(self):
        return self.name


class About(models.Model):
    fullname = models.CharField(verbose_name='F.I.O: ', max_length=240, null=False, blank=False)
    position = models.CharField(verbose_name='Lavozim: ', max_length=240, null=False, blank=False)
    manzil = models.CharField(verbose_name='Manzil: ', max_length=240, null=False, blank=False)
    email = models.EmailField(verbose_name='Email: ', max_length=240, null=False, blank=False)
    skill = models.ManyToManyField(
        Texnologiyalar,
        verbose_name="Ko'nikmalarim: ",

    )
    social = models.ManyToManyField(
        SocialMedia,
        verbose_name="Ijtimoiy tarmoqlarim: ",
    )
    image = models.ImageField(
        verbose_name='Bosh sahifa rasmi: ',
        null=False,
        blank=False,
        upload_to='About/',
        default='assets/me.jpg',
    )
    image2 = models.ImageField(
        verbose_name='Men haqimdagi rasm: ',
        null=False,
        blank=False,
        upload_to='About/',
        default='assets/me.jpg',
    )
    content = tinymce_models.HTMLField(verbose_name="Bosh sahifa ma'lumotlar: ", blank=False, null=False)
    biography = tinymce_models.HTMLField(verbose_name="Barcha ma'lumotlar: ", blank=False, null=False)
    resume = models.FileField(
        verbose_name="Rezyume: ",
        upload_to="resume/",
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Rezyume: '

    def __str__(self):
        return self.fullname
