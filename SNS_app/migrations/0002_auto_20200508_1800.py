# Generated by Django 3.0.3 on 2020-05-08 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SNS_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snsmodel',
            name='good',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='snsmodel',
            name='read',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='snsmodel',
            name='readtext',
            field=models.CharField(blank=True, default='a', max_length=200, null=True),
        ),
    ]
