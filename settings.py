import os

# Platform

PLATFORM = os.getenv('PLATFORM', 'DEVELOPMENT')

# Userdef

DATE_FROM = os.getenv('DATE_FROM', '2011-05-31')
DATE_TO = os.getenv('DATE_TO', '2011-05-31')

# General

BOT_NAME = 'clinicaltrials'
SPIDER_MODULES = ['spiders']
NEWSPIDER_MODULE = 'spiders'

# Throttle

DOWNLOAD_DELAY = float(os.getenv('DOWNLOAD_DELAY', 1))
AUTOTHROTTLE_ENABLED = True

# Pipelines

ITEM_PIPELINES = {
    'pipelines.normalize.Normalize': 200,
    'pipelines.database.Database': 250,
    # 'pipelines.jsonfile.Jsonfile': 300,
}
