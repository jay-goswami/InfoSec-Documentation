# Generated by Django 4.0.6 on 2022-07-31 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Documentation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='command',
            old_name='tool_name',
            new_name='tool',
        ),
    ]