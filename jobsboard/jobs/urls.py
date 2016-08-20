from django.conf.urls import url
from jobsboard.jobs.views import JobDetailView, JobListView, JobCreateView

urlpatterns = [
    # /jobs/
    url(r'^$', JobListView.as_view(), name='job-list'),

    # /jobs/<pk>/
    url(r'^(?P<pk>\d+)/$', JobDetailView.as_view(), name='job-detail'),

    # /jobs/new/
    url(r'^new/$', JobCreateView.as_view(), name='job-create'),

]
