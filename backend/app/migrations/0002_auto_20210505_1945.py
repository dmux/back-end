# Generated by Django 3.1.9 on 2021-05-05 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='date',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Data'),
        ),
    ]
