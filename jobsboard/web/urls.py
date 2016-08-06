from django.conf.urls import url
from jobsboard.web import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

