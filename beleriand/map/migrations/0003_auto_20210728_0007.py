# Generated by Django 3.0.5 on 2021-07-28 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='legend',
        ),
        migrations.DeleteModel(
            name='Legend',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
