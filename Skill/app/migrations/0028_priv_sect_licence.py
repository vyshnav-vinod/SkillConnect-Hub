# Generated by Django 5.0.1 on 2024-04-19 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_rename_ss_feedback_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='priv_sect',
            name='licence',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
