# Generated by Django 5.0.1 on 2024-06-21 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Talim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name="O'qish joyi: ")),
                ('name_uz', models.CharField(max_length=200, null=True, verbose_name="O'qish joyi: ")),
                ('name_en', models.CharField(max_length=200, null=True, verbose_name="O'qish joyi: ")),
                ('course', models.CharField(max_length=100, verbose_name="Yo'nalish nomi: ")),
                ('course_uz', models.CharField(max_length=100, null=True, verbose_name="Yo'nalish nomi: ")),
                ('course_en', models.CharField(max_length=100, null=True, verbose_name="Yo'nalish nomi: ")),
                ('content', models.TextField(verbose_name='Qisqacha izoh: ')),
                ('content_uz', models.TextField(null=True, verbose_name='Qisqacha izoh: ')),
                ('content_en', models.TextField(null=True, verbose_name='Qisqacha izoh: ')),
                ('started_at', models.DateField(verbose_name='Boshlanish vaqti: ')),
                ('ended_at', models.DateField(blank=True, null=True, verbose_name='Tugash vaqti: ')),
                ('is_active', models.BooleanField(default=False, verbose_name="Hozirgi o'qish joyim: ")),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Talim',
                'ordering': ['-created_at'],
            },
        ),
    ]
