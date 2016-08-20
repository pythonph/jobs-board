import factory

from jobsboard.common.factories import UserFactory

from .models import Job


class JobFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Job

    creator = factory.SubFactory(UserFactory)
    title = factory.Faker('job')
    description = factory.Faker('paragraph')
    url = factory.Faker('uri')
