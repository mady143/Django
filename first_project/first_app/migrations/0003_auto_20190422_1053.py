# Generated by Django 2.2 on 2019-04-22 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Users',
        ),
    ]