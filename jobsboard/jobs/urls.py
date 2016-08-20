from django.conf.urls import url
from jobsboard.jobs.views import JobDetailView, JobListView

urlpatterns = [
    # /jobs/
    url(r'^$', JobListView.as_view(), name='job-list'),

    # /jobs/<pk>/
    url(r'^(?P<pk>\d+)/$', JobDetailView.as_view(), name='job-detail'),
]
