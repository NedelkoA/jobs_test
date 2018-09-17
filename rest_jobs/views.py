from rest_framework import viewsets

from .models import Job
from .serializers import JobSerializer
from .utils import jobs, skills


class JobView(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def perform_create(self, serializer):
        job = jobs.JobItem(serializer.validated_data['title'])
        serializer.save(
            title_id=job.uuid,
            normalized_title=job.normalized_job_title
        )
        skills.save_skills(serializer.instance)
        return serializer
