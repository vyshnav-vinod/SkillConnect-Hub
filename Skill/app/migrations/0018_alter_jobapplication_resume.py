# Generated by Django 4.2.5 on 2024-02-26 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_jobapplication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='resume',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]