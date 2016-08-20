from django.views.generic.list import ListView

from .models import Job


class JobListView(ListView):
    model = Job
    queryset = Job.objects.all()
    template_name = 'job_list.html'
    context_object_name = 'jobs'
