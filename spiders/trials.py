import json
import xmltodict
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from services import sources
from items import trial


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

    # TODO: add xpaths methods?
    def parse_item(self, res):

        item = trial.Trial()

        # download_date
        path = '/clinical_study/required_header/download_date/text()'
        item['download_date'] = res.xpath(path).extract_first()

        # link_text
        path = '/clinical_study/required_header/link_text/text()'
        item['link_text'] = res.xpath(path).extract_first()

        # url
        path = '/clinical_study/required_header/url/text()'
        item['url'] = res.xpath(path).extract_first()

        # org_study_id
        path = '/clinical_study/id_info/org_study_id/text()'
        item['org_study_id'] = res.xpath(path).extract_first()

        # nct_id
        path = '/clinical_study/id_info/nct_id/text()'
        item['nct_id'] = res.xpath(path).extract_first()

        # brief_title
        path = '/clinical_study/brief_title/text()'
        item['brief_title'] = res.xpath(path).extract_first()

        # official_title
        path = '/clinical_study/official_title/text()'
        item['official_title'] = res.xpath(path).extract_first()

        # sponsors
        path = '/clinical_study/sponsors/child::*'
        item['sponsors'] = self.__listxml2tson(res.xpath(path).extract())

        # source
        path = '/clinical_study/source/text()'
        item['source'] = res.xpath(path).extract_first()

        # oversight_info
        path = '/clinical_study/oversight_info/node()'
        item['oversight_info'] = self.__dictxml2tson(''.join(res.xpath(path).extract()))

        # brief_summary
        path = '/clinical_study/brief_summary/textblock/text()'
        item['brief_summary'] = res.xpath(path).extract_first()

        # detailed_description
        path = '/clinical_study/detailed_description/textblock/text()'
        item['detailed_description'] = res.xpath(path).extract_first()

        # overall_status
        path = '/clinical_study/overall_status/text()'
        item['overall_status'] = res.xpath(path).extract_first()

        # start_date
        path = '/clinical_study/start_date/text()'
        item['start_date'] = res.xpath(path).extract_first()

        # completion_date
        path = '/clinical_study/completion_date/text()'
        item['completion_date'] = res.xpath(path).extract_first()

        # primary_completion_date
        path = '/clinical_study/primary_completion_date/text()'
        item['primary_completion_date'] = res.xpath(path).extract_first()

        # phase
        path = '/clinical_study/phase/text()'
        item['phase'] = res.xpath(path).extract_first()

        # study_type
        path = '/clinical_study/study_type/text()'
        item['study_type'] = res.xpath(path).extract_first()

        # study_design
        path = '/clinical_study/study_design/text()'
        item['study_design'] = res.xpath(path).extract_first()

        # primary_outcome
        path = '/clinical_study/primary_outcome/node()'
        item['primary_outcome'] = self.__dictxml2tson(''.join(res.xpath(path).extract()))

        # secondary_outcomes
        path = '/clinical_study/secondary_outcome'
        item['secondary_outcomes'] = self.__listxml2tson(res.xpath(path).extract())

        # number_of_arms
        path = '/clinical_study/number_of_arms/text()'
        item['number_of_arms'] = res.xpath(path).extract_first()

        # enrollment
        path = '/clinical_study/enrollment/text()'
        item['enrollment'] = res.xpath(path).extract_first()

        # conditions
        path = '/clinical_study/condition'
        item['conditions'] = self.__listxml2tson(res.xpath(path).extract())

        # arm_groups
        path = '/clinical_study/arm_group'
        item['arm_groups'] = self.__listxml2tson(res.xpath(path).extract())

        # interventions
        path = '/clinical_study/intervention'
        item['interventions'] = self.__listxml2tson(res.xpath(path).extract())

        # eligibility
        path = '/clinical_study/eligibility/node()'
        item['eligibility'] = self.__dictxml2tson(''.join(res.xpath(path).extract()))

        # overall_official
        path = '/clinical_study/overall_official/node()'
        item['overall_official'] = self.__dictxml2tson(''.join(res.xpath(path).extract()))

        # locations
        path = '/clinical_study/location'
        item['locations'] = self.__listxml2tson(res.xpath(path).extract())

        # location_countries
        path = '/clinical_study/location_countries/child::*'
        item['location_countries'] = self.__listxml2tson(res.xpath(path).extract())

        # removed_countries
        path = '/clinical_study/removed_countries/child::*'
        item['removed_countries'] = self.__listxml2tson(res.xpath(path).extract())

        # verification_date
        path = '/clinical_study/verification_date/text()'
        item['verification_date'] = res.xpath(path).extract_first()

        # lastchanged_date
        path = '/clinical_study/lastchanged_date/text()'
        item['lastchanged_date'] = res.xpath(path).extract_first()

        # firstreceived_date
        path = '/clinical_study/firstreceived_date/text()'
        item['firstreceived_date'] = res.xpath(path).extract_first()

        # responsible_party
        path = '/clinical_study/responsible_party/node()'
        item['responsible_party'] = self.__dictxml2tson(''.join(res.xpath(path).extract()))

        # keywords
        path = '/clinical_study/keyword/text()'
        item['keywords'] = json.dumps((res.xpath(path).extract()))

        # is_fda_regulated
        path = '/clinical_study/is_fda_regulated/text()'
        item['is_fda_regulated'] = res.xpath(path).extract_first()

        # has_expanded_access
        path = '/clinical_study/has_expanded_access/text()'
        item['has_expanded_access'] = res.xpath(path).extract_first()

        # clinical_results
        path = '/clinical_study/clinical_results/node()'
        item['clinical_results'] = self.__dictxml2tson(''.join(res.xpath(path).extract()))

        return item

    # Private

    @staticmethod
    def __dictxml2tson(xml):
        try:
            return json.dumps(xmltodict.parse(xml))
        except Exception:
            return None

    @staticmethod
    def __listxml2tson(xml):
        try:
            return json.dumps(map(xmltodict.parse, xml))
        except Exception:
            return None
