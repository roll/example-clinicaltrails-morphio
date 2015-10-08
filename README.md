# opentrials-clinicaltrailsgov-data

This is a scraper that runs on [Morph](https://morph.io). To get started [see the documentation](https://morph.io/documentation).

## Documents

- [Scraping strategy overview](https://github.com/okfn/opentrials-clinicaltrailsgov-data/blob/master/STRATEGY.md)
- [Data model of clinicaltrials.gov](https://github.com/okfn/opentrials-clinicaltrailsgov-data/blob/master/MODEL.md)

## Configuration

Environment variables to configure the scraper:

- DATE_FROM

  Get trials with last updated mark => this date.

- DATE_TO

  Get trials with last updated mark <= this date.

- DOWNLOAD_DELAY

  Requests we're making to clinicaltrials.gov interval.

## Workflow

We need to download around 200 000 pages and we want to be polite to the source webserver:

- 1s delay -> 60 hours
- 0.5s delay -> 30 hours (more than morph.io can do for us)
- etc

So we can scrape manually by years then pull updates for the last year automatically:

- 1 year (60 000 pages) + 1s delay -> 32 hours
- 1 year (60 000 pages) + 0.5s delay -> 16 hours
- 1 year (60 000 pages) + 0.25s delay -> 8 hours
- etc

Proposed settings for the scraping some year:

```
DATE_FROM='2010-01-01'
DATE_TO='2010-12-31'
DOWNLOAD_DELAY='0.25'
```

Proposed settings for the database updating:

```
DATE_FROM='2015-10-01'
DATE_TO='2015-12-31'
DOWNLOAD_DELAY='0.5'
```
