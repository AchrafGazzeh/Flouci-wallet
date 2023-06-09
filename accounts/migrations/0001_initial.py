# Generated by Django 3.1.5 on 2021-01-14 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecordModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=40)),
                ('category', models.CharField(max_length=40)),
                ('sub_category', models.CharField(max_length=40)),
                ('payment', models.CharField(max_length=40)),
                ('amount', models.FloatField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]
