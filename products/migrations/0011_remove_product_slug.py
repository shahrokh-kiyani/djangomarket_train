# Generated by Django 4.1.4 on 2023-01-08 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_comment_managers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]
