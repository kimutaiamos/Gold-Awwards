# Generated by Django 3.2 on 2021-12-12 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0002_profile_profile_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_photo',
            field=models.ImageField(default='Image', upload_to='projectpics/'),
        ),
    ]