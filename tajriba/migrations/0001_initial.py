# Generated by Django 5.0.1 on 2024-01-23 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tajriba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('started_at', models.DateField()),
                ('ended_at', models.DateField()),
                ('position', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Tajriba',
                'verbose_name_plural': 'Tajriba',
                'ordering': ['created_at'],
            },
        ),
    ]
