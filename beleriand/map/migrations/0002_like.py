# Generated by Django 3.0.5 on 2021-07-27 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legend', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='map.Legend')),
            ],
        ),
    ]