from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from services import sources
from items import trial


class Trials(CrawlSpider):

    # Public

    name = 'trials'
    allowed_domains = ['clinicaltrials.gov']
    start_urls = sources.make_start_urls('https://www.clinicaltrials.gov/ct2/results')
    rules = [
        Rule(LinkExtractor(
            allow=sources.make_pattern('ct2/results'),
        )),
        Rule(LinkExtractor(
            allow=r'ct2/show/NCT\d+',
            process_value=lambda value: value+'&resultsxml=true',
        ), callback='parse_item'),
    ]

    def parse_item(self, response):

        item = trial.Trial()

        # Id
        path = '/clinical_study/id_info/nct_id/text()'
        item['nct_id'] = response.xpath(path).extract_first()

        # Url
        path = '/clinical_study/required_header/url/text()'
        item['url'] = response.xpath(path).extract_first()

        return item
