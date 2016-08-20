from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('jobsboard.web.urls')),
    url(r'^jobs/', include('jobsboard.jobs.urls')),
]
