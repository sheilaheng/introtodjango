# Generated by Django 3.0.5 on 2023-07-28 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangosheilah', '0005_auto_20230728_0617'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='city',
            field=models.CharField(default='Nairobi', max_length=30),
        ),
        migrations.AddField(
            model_name='people',
            name='country',
            field=models.CharField(default='Keny', max_length=30),
        ),
    ]