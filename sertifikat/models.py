from django.db import models
from loyiha.models import Texnologiyalar


class Sertifikat(models.Model):
    name = models.CharField(verbose_name='Sertifikat nomi: ', max_length=200, blank=False, null=False)
    description = models.TextField(verbose_name="Qisqa izoh: ", blank=False, null=False)
    techno = models.OneToOneField(
        Texnologiyalar,
        verbose_name="Texnologiyalar",
        blank=False,
        null=False,
        on_delete=models.CASCADE
    )
    company = models.CharField(verbose_name='Qayerdan olindi', max_length=200, null=False, blank=False)
    image = models.ImageField(verbose_name="Post rasmi", blank=True, null=True, upload_to='Sertificat/')
    started_at = models.DateField(verbose_name='Boshlanish vaqti: ', null=False, blank=False)
    ended_at = models.DateField(verbose_name='Tugash vaqti: ', blank=True, null=True)
    link = models.URLField(verbose_name="Sertifikat linki: ", null=True, blank=True)
    tag = models.ManyToManyField(Texnologiyalar, verbose_name='Teglar', null=False, blank=False)
    is_active = models.BooleanField(verbose_name='Faol yoki nofaollik: ', default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Sertifikatlar'

    def __str__(self):
        return self.name
