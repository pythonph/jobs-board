from django.test import TestCase

from ..factories import JobFactory
from ..models import Job


class JobModelCreateTest(TestCase):

    def test_initial_state(self):
        job = JobFactory()

        assert(job.creator)
        assert(not job.is_featured)
        assert(job.employment_type == Job.EMPLOYMENT_TYPE_FULL_TIME)
