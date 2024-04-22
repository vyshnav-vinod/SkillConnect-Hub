# Generated by Django 5.0.1 on 2024-02-01 06:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_user_reg_age'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_reg',
            old_name='age',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='user_reg',
            name='name',
        ),
        migrations.AddField(
            model_name='user_reg',
            name='phone',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
