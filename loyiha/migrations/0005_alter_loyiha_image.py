# Generated by Django 5.0.1 on 2024-01-27 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loyiha', '0004_loyiha_description_loyiha_description_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loyiha',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Loyiha/', verbose_name='Post rasmi'),
        ),
    ]
