# Generated by Django 5.0.1 on 2024-06-21 06:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loyiha', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sertifikat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Sertifikat nomi: ')),
                ('name_uz', models.CharField(max_length=200, null=True, verbose_name='Sertifikat nomi: ')),
                ('name_en', models.CharField(max_length=200, null=True, verbose_name='Sertifikat nomi: ')),
                ('description', models.TextField(verbose_name='Qisqa izoh: ')),
                ('description_uz', models.TextField(null=True, verbose_name='Qisqa izoh: ')),
                ('description_en', models.TextField(null=True, verbose_name='Qisqa izoh: ')),
                ('company', models.CharField(max_length=200, verbose_name='Qayerdan olindi')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Sertificat/', verbose_name='Post rasmi')),
                ('started_at', models.DateField(verbose_name='Boshlanish vaqti: ')),
                ('ended_at', models.DateField(blank=True, null=True, verbose_name='Tugash vaqti: ')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Sertifikat linki: ')),
                ('is_active', models.BooleanField(default=False, verbose_name='Faol yoki nofaollik: ')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tag', models.ManyToManyField(related_name='tags', to='loyiha.texnologiyalar', verbose_name='Teglar')),
                ('techno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loyiha.texnologiyalar', verbose_name='Texnologiyalar')),
            ],
            options={
                'verbose_name_plural': 'Sertifikatlar',
                'ordering': ['-created_at'],
            },
        ),
    ]
