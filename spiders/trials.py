import json
import logging
import xmltodict
from functools import partial
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from services import sources
from items import trial
logger = logging.getLogger(__name__)


class Trials(CrawlSpider):

    # Public

    name = 'trials'
    allowed_domains = ['clinicaltrials.gov']
    start_urls = sources.make_start_urls(
        'https://www.clinicaltrials.gov/ct2/results')
    rules = [
        Rule(LinkExtractor(
            allow=sources.make_pattern('ct2/results'),
        )),
        Rule(LinkExtractor(
            allow=r'ct2/show/NCT\d+',
            process_value=lambda value: value+'&resultsxml=true',
        ), callback='parse_item'),
    ]

    def parse_item(self, res):

        # Create item
        item = trial.Trial()

        # Extraction tools
        gtext = partial(self.__get_text, res)
        gdict = partial(self.__get_dict, res)
        glist = partial(self.__get_list, res)

        # Plain value fields
        item['download_date'] = gtext('required_header/download_date')
        item['link_text'] = gtext('required_header/link_text')
        item['url'] = gtext('required_header/url')
        item['org_study_id'] = gtext('id_info/org_study_id')
        item['nct_id'] = gtext('id_info/nct_id')
        item['brief_title'] = gtext('brief_title')
        item['official_title'] = gtext('official_title')
        item['source'] = gtext('source')
        item['brief_summary'] = gtext('brief_summary/textblock')
        item['detailed_description'] = gtext('detailed_description/textblock')
        item['overall_status'] = gtext('overall_status')
        item['start_date'] = gtext('start_date')
        item['completion_date'] = gtext('completion_date')
        item['primary_completion_date'] = gtext('primary_completion_date')
        item['phase'] = gtext('phase')
        item['study_type'] = gtext('study_type')
        item['study_design'] = gtext('study_design')
        item['number_of_arms'] = gtext('number_of_arms')
        item['enrollment'] = gtext('enrollment')
        item['verification_date'] = gtext('verification_date')
        item['lastchanged_date'] = gtext('lastchanged_date')
        item['firstreceived_date'] = gtext('firstreceived_date')
        item['is_fda_regulated'] = gtext('is_fda_regulated')
        item['has_expanded_access'] = gtext('has_expanded_access')

        # Dict value fields

        item['oversight_info'] = gdict('oversight_info')
        item['primary_outcome'] = gdict('primary_outcome')
        item['eligibility'] = gdict('eligibility')
        item['overall_official'] = gdict('overall_official')
        item['responsible_party'] = gdict('responsible_party')
        item['clinical_results'] = gdict('clinical_results')

        # List value fields

        item['sponsors'] = glist('sponsors/child::*')
        item['secondary_outcomes'] = glist('secondary_outcome')
        item['conditions'] = glist('condition')
        item['arm_groups'] = glist('arm_group')
        item['interventions'] = glist('intervention')
        item['locations'] = glist('location')
        item['location_countries'] = glist('location_countries/child::*')
        item['removed_countries'] = glist('removed_countries/child::*')
        item['keywords'] = glist('keyword/text()')

        return item

    # Private

    @staticmethod
    def __get_text(res, path):
        base = ''
        path = '%s/text()' % path
        return res.xpath(path).extract_first() or base

    @staticmethod
    def __get_dict(res, path):
        base = {}
        path = '%s/node()' % path
        node = ''.join(res.xpath(path).extract())
        try:
            value = xmltodict.parse(node) or base
        except Exception as exception:
            logger.debug(exception)
            value = base
        return json.dumps(value)

    @staticmethod
    def __get_list(res, path):
        base = []
        path = '%s' % path
        nodes = res.xpath(path).extract()
        try:
            value = map(xmltodict.parse, nodes) or base
        except Exception as exception:
            logger.debug(exception)
            value = base
        return json.dumps(value)
