# Generated by Django 5.0.1 on 2024-02-04 16:46

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aloqa', '0002_socialmedia_about'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='content2',
            new_name='biography',
        ),
        migrations.AddField(
            model_name='about',
            name='biography_en',
            field=tinymce.models.HTMLField(null=True, verbose_name="Barcha ma'lumotlar: "),
        ),
        migrations.AddField(
            model_name='about',
            name='biography_uz',
            field=tinymce.models.HTMLField(null=True, verbose_name="Barcha ma'lumotlar: "),
        ),
        migrations.AddField(
            model_name='about',
            name='content_en',
            field=tinymce.models.HTMLField(null=True, verbose_name="Bosh sahifa ma'lumotlar: "),
        ),
        migrations.AddField(
            model_name='about',
            name='content_uz',
            field=tinymce.models.HTMLField(null=True, verbose_name="Bosh sahifa ma'lumotlar: "),
        ),
        migrations.AddField(
            model_name='about',
            name='fullname_en',
            field=models.CharField(max_length=240, null=True, verbose_name='F.I.O: '),
        ),
        migrations.AddField(
            model_name='about',
            name='fullname_uz',
            field=models.CharField(max_length=240, null=True, verbose_name='F.I.O: '),
        ),
        migrations.AddField(
            model_name='about',
            name='manzil_en',
            field=models.CharField(max_length=240, null=True, verbose_name='Manzil: '),
        ),
        migrations.AddField(
            model_name='about',
            name='manzil_uz',
            field=models.CharField(max_length=240, null=True, verbose_name='Manzil: '),
        ),
        migrations.AddField(
            model_name='about',
            name='position_en',
            field=models.CharField(max_length=240, null=True, verbose_name='Lavozim: '),
        ),
        migrations.AddField(
            model_name='about',
            name='position_uz',
            field=models.CharField(max_length=240, null=True, verbose_name='Lavozim: '),
        ),
        migrations.AddField(
            model_name='about',
            name='social',
            field=models.ManyToManyField(to='aloqa.socialmedia', verbose_name='Ijtimoiy tarmoqlarim: '),
        ),
    ]
