# Overview

A document describes existent and proposed solutions to get data from clinicaltrials.gov.

## Existent solutions

### List of some existent solutions

#### datasets/clinical-trials-us

https://github.com/datasets/clinical-trials-us

Rufus's simple script to process all data from clinicaltrials.gov.

- **Pros** - simple
- **Cons** - not fully automated (a deal breaker)

#### tinfante/ClinicalTrialsScraper

https://github.com/tinfante/ClinicalTrialsScraper

www.clinicaltrials.gov scraper for www.estudiosclinicos.org.

- **Pros** - simple
- **Cons** - pure python implementation (no framework), 0 starts on github

#### codeforamerica/clinical_trials_python

https://github.com/codeforamerica/clinical_trials_python

A wrapper around the clinicaltrials API.

- **Pros** - neat interface
- **Cons** - not very flexible, lase commit on 2011 year

#### p2/py-clinical-trials

https://github.com/p2/py-clinical-trials

Library to access clinicaltrials.gov

- **Cons** - over-complicated

### Assessment of existent solutions

There is no industry standard or well-maintained package to build our project to be dependent upon. A cost of in-house solution can be much lesser then a cost of learning and maintaining a side solution.

## Proposed solution

Because of lack of the mature existent clinicaltrials.gov scraper it have been proposed to write in-house solution. We can see a list of pros of this approach:
- usage  of the industry standard scraping framework [Scrapy](http://scrapy.org/)
- simple implementation because of xml exposed by clinicaltrials.gov
- unlimited flexibility and full code control

Here is a prototype/boilerplate for the full-featured in-house scraper based on Scrapy:

https://github.com/roll/clinicaltrials-scraper
