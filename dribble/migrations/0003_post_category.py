# Generated by Django 3.0 on 2019-12-12 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dribble', '0002_auto_20191212_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='', max_length=255),
        ),
    ]
