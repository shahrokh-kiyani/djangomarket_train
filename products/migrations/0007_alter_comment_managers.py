# Generated by Django 4.0.2 on 2022-10-18 16:52

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_comment_time'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='comment',
            managers=[
                ('active_comments_manager', django.db.models.manager.Manager()),
            ],
        ),
    ]
