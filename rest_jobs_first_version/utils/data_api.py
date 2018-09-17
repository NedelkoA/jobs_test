import requests

from ..models import Skill


def request_to_api(url):
    base_url = 'http://api.dataatwork.org/v1/jobs'
    return requests.get(base_url + url).json()


def create_skills(skill_list, job_instance):
    skills = [
        Skill(
            skill_uuid=skill['skill_uuid'],
            skill_name=skill['skill_name'],
            skill_type=skill['skill_type'],
            description=skill['description'],
            normalized_skill_name=skill['normalized_skill_name'],
            importance=skill['importance'],
            level=skill['level'],
            score=skill['importance'] + skill['level'] / 2,
            job=job_instance,
        )
        for skill in skill_list['skills']
    ]
    Skill.objects.bulk_create(skills)
