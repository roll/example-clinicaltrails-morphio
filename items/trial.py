import scrapy


class Trial(scrapy.Item):

    # Public

    download_date = scrapy.Field()
    link_text = scrapy.Field()
    url = scrapy.Field()
    org_study_id = scrapy.Field()
    nct_id = scrapy.Field()
    brief_title = scrapy.Field()
    official_title = scrapy.Field()
    sponsors = scrapy.Field()
    source = scrapy.Field()
    oversight_info_authority = scrapy.Field()
    brief_summary = scrapy.Field()
    detailed_description = scrapy.Field()
    overall_status = scrapy.Field()
    start_date = scrapy.Field()
    completion_date = scrapy.Field()
    phase = scrapy.Field()
    study_type = scrapy.Field()
    study_design = scrapy.Field()
    primary_outcome = scrapy.Field()
    secondary_outcome = scrapy.Field()
    enrollment = scrapy.Field()
    conditions = scrapy.Field()
    interventions = scrapy.Field()
    eligibility = scrapy.Field()
    overall_official = scrapy.Field()
    location = scrapy.Field()
    location_countries = scrapy.Field()
    verification_date = scrapy.Field()
    lastchanged_date = scrapy.Field()
    firstreceived_date = scrapy.Field()
    keywords = scrapy.Field()
