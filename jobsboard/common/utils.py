from django.utils import timezone


def get_default_expiry(start=timezone.now()):
    '''
    This gives  datetime object that is 30 days
    after the `start` argument.

    :param start: The start date.
    :type start: datetime
    :returns: datetime -- a datetime object 30 days after `start`
    '''
    return start + timezone.timedelta(days=30)
