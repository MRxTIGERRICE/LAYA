# Generated by Django 4.1.6 on 2023-10-26 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0020_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('Fiction', 'Fiction'), ('Thriller', 'Thriller'), ('Fantasy', 'Fantasy'), ('Sci-Fi', 'Sci-fi'), ('Romance', 'Romance')], default='Fiction', max_length=20),
        ),
    ]