from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel


class Account(TimeStampedModel):
    """User account information

    .. NOTE: More account info related fields may be added here in the future.
        i.e. Birthday, Location, Photo, etc.

    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    is_active = models.BooleanField(default=True)


class Organization(TimeStampedModel):
    """Organization account information

    .. NOTE: More account info related fields may be added here in the future.
        i.e. Photo, etc.

    """
    name = models.CharField(max_length=128)
    owner = models.ForeignKey(User, related_name='owner')
    admins = models.ManyToManyField(
        User,
        related_name='admins',
        limit_choices_to={
            'account__is_active': True,
            'is_active': True,
        },
        blank=True,
    )
    members = models.ManyToManyField(
        User,
        related_name='members',
        limit_choices_to={
            'account__is_active': True,
            'is_active': True,
        },
        blank=True,
    )
    is_active = models.BooleanField(default=True)
