# Generated by Django 2.1.1 on 2018-09-14 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_jobs', '0002_auto_20180912_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='skill_uuid',
            field=models.UUIDField(unique=True),
        ),
    ]