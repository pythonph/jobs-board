from django.conf.urls import url
from jobsboard.jobs.views import JobListView

urlpatterns = [
    url(r'^$', JobListView.as_view(), name='job-list'),
]
