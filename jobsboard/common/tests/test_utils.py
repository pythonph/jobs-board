import datetime as dt

from django.test import TestCase

from ..utils import get_default_expiry


class ExpiryDateTest(TestCase):

    DATE_FORMAT = '%Y-%m-%d'

    def test_basic_cases(self):
        # December 31 jobs expire on January 30 the following year
        date_2015_01_01 = dt.date(2015, 12, 31)
        expiry = get_default_expiry(date_2015_01_01)
        expiry_str = expiry.strftime(self.DATE_FORMAT)
        assert(expiry_str == '2016-01-30')

        # January 1 jobs expire on January 31
        date_2016_01_01 = dt.date(2016, 1, 1)
        expiry = get_default_expiry(date_2016_01_01)
        expiry_str = expiry.strftime(self.DATE_FORMAT)
        assert(expiry_str == '2016-01-31')

        # January 2 jobs expire on February 1
        date_2016_01_02 = dt.date(2016, 1, 2)
        expiry = get_default_expiry(date_2016_01_02)
        expiry_str = expiry.strftime(self.DATE_FORMAT)
        assert(expiry_str == '2016-02-01')

    def test_leap_year(self):
        # Test leap year - 2016
        # January 2 jobs expire on February 1
        date_2016_02_01 = dt.date(2016, 2, 1)
        expiry = get_default_expiry(date_2016_02_01)
        expiry_str = expiry.strftime(self.DATE_FORMAT)
        assert(expiry_str == '2016-03-02')

        # Test non-leap year - 2015
        # January 2 jobs expire on February 1
        date_2015_02_01 = dt.date(2015, 2, 1)
        expiry = get_default_expiry(date_2015_02_01)
        expiry_str = expiry.strftime(self.DATE_FORMAT)
        assert(expiry_str == '2015-03-03')
