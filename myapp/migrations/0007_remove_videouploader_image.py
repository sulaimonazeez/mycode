# Generated by Django 4.1.3 on 2022-12-19 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_videouploader_delete_filehand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videouploader',
            name='image',
        ),
    ]
