import requests


def get_job(title):
    return requests.get(
        'http://api.dataatwork.org/v1/jobs/autocomplete',
        params={
            'begins_with': title
        }
    ).json()[0]


def get_skills(uuid):
    response = requests.get(
        'http://api.dataatwork.org/v1/jobs/{}/related_skills'.format(uuid),
    ).json()
    if 'skills' in response:
        return response['skills']
