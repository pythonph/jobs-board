from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def validate_user_email_exists(value):
    user = User.objects.filter(email__iexact=value)
    if user.exists():
        msg = _('A user with that email already exists.')
        raise ValidationError(msg)
