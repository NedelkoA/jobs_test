from rest_framework import viewsets

from .models import Job
from .serializers import JobSerializer
from .utils import jobs, skills, data_api


class JobView(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def perform_create(self, serializer):
        job_data = data_api.get_job(serializer.validated_data['title'])
        job = jobs.JobItem(job_data)
        serializer.save(
            title_id=job.uuid,
            normalized_title=job.normalized_job_title
        )
        skills_data = data_api.get_skills(job.uuid)
        skill_items = skills.skill_items(skills_data, serializer.instance)
        skills.save_skills(skill_items)
        return serializer
