from .data_api import get_skills
from ..models import Skill


class SkillItem:
    def __init__(self, data, job):
        for key, value in data.items():
            setattr(self, key, value)
        self.score = self.get_score(self.importance, self.level)
        self.job = job

    def get_score(self, importance, level):
        if importance or level:
            return importance + level / 2


def skill_items(skills_data, job):
    return [
        SkillItem(data, job)
        for data in skills_data
    ]


def save_skills(job):
    api_skills = get_skills(job.title_id)
    if api_skills is not None:
        skill_items(api_skills, job)
        skills = [
            Skill(**item.__dict__)
            for item in skill_items
        ]
        Skill.objects.bulk_create(skills)
