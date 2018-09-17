# Generated by Django 2.1.1 on 2018-09-12 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('title_id', models.UUIDField()),
                ('normalized_title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_uuid', models.UUIDField()),
                ('skill_name', models.CharField(max_length=100)),
                ('skill_type', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('normalized_skill_name', models.CharField(max_length=100)),
                ('importance', models.FloatField()),
                ('level', models.FloatField()),
                ('score', models.FloatField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='rest_jobs.Job')),
            ],
        ),
    ]