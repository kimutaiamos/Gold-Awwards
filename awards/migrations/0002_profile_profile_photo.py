# Generated by Django 3.2 on 2021-12-12 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(default='Image', upload_to='profilepics/'),
        ),
    ]