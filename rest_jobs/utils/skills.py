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


def save_skills(items_list):
    skills = [
        Skill(**item.__dict__)
        for item in items_list
    ]
    Skill.objects.bulk_create(skills)
