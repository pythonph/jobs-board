from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Job

from jobsboard.jobs.forms import JobForm


class JobListView(ListView):
    model = Job
    queryset = Job.objects.all()
    template_name = 'job_list.html'
    context_object_name = 'jobs'


class JobDetailView(DetailView):
    model = Job
    context_object_name = 'job'
    template_name = 'job_detail.html'


class JobCreateView(CreateView):
    model = Job
    template_name = 'job_create.html'
    form_class = JobForm

    def post(self, request, *args, **kwargs):
        form = JobForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.creator = request.user
            job.save()

        return HttpResponse("Saved!")