# Generated by Django 5.2.1 on 2025-05-28 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='image',
            field=models.ImageField(default='branch_images/oqtepa_lavash.jpg', upload_to='branch_images/'),
        ),
    ]
