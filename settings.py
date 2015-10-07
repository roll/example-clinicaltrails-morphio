import os

# Platform

PLATFORM = os.getenv('PLATFORM')
if not PLATFORM:
    PLATFORM = 'DEVELOPMENT'

# General

BOT_NAME = 'clinicaltrials'
SPIDER_MODULES = ['spiders']
NEWSPIDER_MODULE = 'spiders'

# Throttle

DOWNLOAD_DELAY = 1
AUTOTHROTTLE_ENABLED = True

# Pipelines

ITEM_PIPELINES = {
    'pipelines.Normalize': 200,
    'pipelines.Jsonfile': 250,
    'pipelines.Database': 250,
}
