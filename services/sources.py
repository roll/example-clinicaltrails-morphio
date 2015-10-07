"""
Service provides initial url generator for scrapers.
"""
import settings
from datetime import datetime
from urllib import urlencode
from collections import OrderedDict


def make_start_urls(base):
    """ Return start_urls.
    """
    query = OrderedDict()
    date_from = datetime.strptime(settings.DATE_FROM, '%Y-%m-%d')
    date_to = datetime.strptime(settings.DATE_TO, '%Y-%m-%d')
    query['lup_s'] = date_from.strftime('%m/%d/%Y')
    query['lup_e'] = date_to.strftime('%m/%d/%Y')
    return [base + '?' + urlencode(query)]


def make_pattern(base):
    """ Return pattern.
    """
    return base + r'\?lup_s=[^&]+&lup_e=[^&]+(&pg=\d+)?$'
