# Generated by Django 3.2.6 on 2021-08-23 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_store', '0002_good_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='img',
            field=models.ImageField(blank=True, default='goods/default.jpg', null=True, upload_to='goods'),
        ),
    ]