# Generated by Django 2.2 on 2019-05-13 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_data_app', '0009_key_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='image',
            field=models.ImageField(null=True, upload_to='about', verbose_name='Картинка'),
        ),
    ]
