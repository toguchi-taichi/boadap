# Generated by Django 3.1.4 on 2020-12-28 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boadapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boadmodel',
            name='good',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='boadmodel',
            name='read',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='boadmodel',
            name='readtext',
            field=models.CharField(blank=True, default='a', max_length=200, null=True),
        ),
    ]
