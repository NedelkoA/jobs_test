from rest_framework import viewsets

from .models import Job
from .serializers import JobSerializer
from .utils.data_api import request_to_api, create_skills


class JobView(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def perform_create(self, serializer):
        get_job = request_to_api('/autocomplete?begins_with={}'.format(serializer.validated_data['title']))
        serializer.save(
            title_id=get_job[0]['uuid'],
            normalized_title=get_job[0]['normalized_job_title']
        )
        get_skills = request_to_api('/{}/related_skills'.format(get_job[0]['uuid']))
        create_skills(get_skills, serializer.instance)
        return serializer
