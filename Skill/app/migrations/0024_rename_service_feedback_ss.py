# Generated by Django 4.2.5 on 2024-02-27 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='service',
            new_name='ss',
        ),
    ]