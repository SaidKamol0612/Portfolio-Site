# Generated by Django 5.1.5 on 2025-01-28 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorinfo',
            name='logo',
            field=models.ImageField(default='logo', upload_to='images/home/'),
        ),
    ]
