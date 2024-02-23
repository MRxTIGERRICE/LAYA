# Generated by Django 3.1.5 on 2021-01-24 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0013_song_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='tags',
            field=models.CharField(choices=[('Classical', 'Classical'), ('Romantic', 'Romantic'), ('Pop', 'Pop'), ('Rock', 'Rock'), ('Devotional', 'Devotional'), ('Bhajan', 'Bhajan'), ('Dance', 'Dance'), ('Disco', 'Disco'), ('Ghazal', 'Ghazal'), ('Qawwali', 'Qawwali')], default='Classical', max_length=20),
        ),
    ]