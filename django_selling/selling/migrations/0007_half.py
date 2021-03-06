# Generated by Django 3.1.7 on 2021-03-30 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selling', '0006_auto_20210330_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='Half',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('avi_date', models.CharField(blank=True, max_length=20)),
                ('price', models.CharField(blank=True, max_length=10)),
                ('img', models.ImageField(blank=True, upload_to='image')),
            ],
        ),
    ]
