from djanog_extensions.models import TimeStampedModel

from django.db import models


class Job(TimeStampedModel):
    creator = models.ForeignKey('auth.User')
    title = models.CharField(max_length=40)
    description = models.TextField()
    url = models.URLField()
    is_featured = models.BooleanField(default=False)
