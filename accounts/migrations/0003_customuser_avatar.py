# Generated by Django 4.1.4 on 2023-01-01 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(default='download.png', upload_to='profile_pic'),
        ),
    ]
