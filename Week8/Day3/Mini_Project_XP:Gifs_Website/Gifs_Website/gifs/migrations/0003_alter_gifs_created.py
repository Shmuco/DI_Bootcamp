# Generated by Django 3.2.3 on 2021-05-27 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifs', '0002_auto_20210526_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gifs',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]