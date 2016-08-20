from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Job


class JobListView(ListView):
    model = Job
    queryset = Job.objects.all()
    template_name = 'job_list.html'
    context_object_name = 'jobs'


class JobDetailView(DetailView):
    model = Job
    context_object_name = 'job'
    template_name = 'job_detail.html'
