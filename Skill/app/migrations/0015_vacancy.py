# Generated by Django 4.2.5 on 2024-02-26 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_services_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobtitle', models.CharField(max_length=50, null=True)),
                ('experience', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('qualification', models.CharField(max_length=50, null=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.priv_sect')),
            ],
        ),
    ]
