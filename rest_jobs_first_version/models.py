from django.db import models


class Job(models.Model):
    title = models.CharField(
        max_length=100
    )
    location = models.CharField(
        max_length=100
    )
    title_id = models.UUIDField()
    normalized_title = models.CharField(
        max_length=100
    )


class Skill(models.Model):
    skill_uuid = models.UUIDField()
    skill_name = models.CharField(
        max_length=100
    )
    skill_type = models.CharField(
        max_length=100
    )
    description = models.TextField()
    normalized_skill_name = models.CharField(
        max_length=100
    )
    importance = models.FloatField()
    level = models.FloatField()
    score = models.FloatField()
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name='skills'
    )
