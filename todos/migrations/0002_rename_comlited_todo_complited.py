# Generated by Django 4.2.8 on 2023-12-07 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='comlited',
            new_name='complited',
        ),
    ]
