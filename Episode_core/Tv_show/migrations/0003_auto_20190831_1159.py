# Generated by Django 2.2.4 on 2019-08-31 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tv_show', '0002_auto_20190831_1125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name='running_status',
        ),
        migrations.AddField(
            model_name='show',
            name='runningStatus',
            field=models.CharField(default=False, max_length=50),
            preserve_default=False,
        ),
    ]
