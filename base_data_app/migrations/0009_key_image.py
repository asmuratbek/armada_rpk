# Generated by Django 2.2 on 2019-05-13 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_data_app', '0008_key_keyslider'),
    ]

    operations = [
        migrations.AddField(
            model_name='key',
            name='image',
            field=models.ImageField(null=True, upload_to='key', verbose_name='Картинка'),
        ),
    ]
