# Generated by Django 4.2.5 on 2024-02-27 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='ss',
            new_name='service',
        ),
    ]
