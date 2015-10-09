import scrapy


class Trial(scrapy.Item):

    # Public

    # Plain value fields
    download_date = scrapy.Field()
    link_text = scrapy.Field()
    url = scrapy.Field()
    org_study_id = scrapy.Field()
    nct_id = scrapy.Field()
    brief_title = scrapy.Field()
    official_title = scrapy.Field()
    source = scrapy.Field()
    brief_summary = scrapy.Field()
    detailed_description = scrapy.Field()
    overall_status = scrapy.Field()
    start_date = scrapy.Field()
    completion_date = scrapy.Field()
    primary_completion_date = scrapy.Field()
    phase = scrapy.Field()
    study_type = scrapy.Field()
    study_design = scrapy.Field()
    number_of_arms = scrapy.Field()
    enrollment = scrapy.Field()
    verification_date = scrapy.Field()
    lastchanged_date = scrapy.Field()
    firstreceived_date = scrapy.Field()
    is_fda_regulated = scrapy.Field()
    has_expanded_access = scrapy.Field()

    # Dict value fields
    oversight_info = scrapy.Field()
    primary_outcome = scrapy.Field()
    eligibility = scrapy.Field()
    overall_official = scrapy.Field()
    responsible_party = scrapy.Field()
    clinical_results = scrapy.Field()

    # List value fields
    sponsors = scrapy.Field()
    secondary_outcomes = scrapy.Field()
    conditions = scrapy.Field()
    arm_groups = scrapy.Field()
    interventions = scrapy.Field()
    locations = scrapy.Field()
    location_countries = scrapy.Field()
    removed_countries = scrapy.Field()
    keywords = scrapy.Field()
