# Generated by Django 3.1.7 on 2021-03-29 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selling', '0003_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, upload_to='image'),
        ),
    ]
