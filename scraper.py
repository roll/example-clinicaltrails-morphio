import scraperwiki
import lxml.html


# Read in a page
# html = scraperwiki.scrape("http://foo.com")

# Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")

# Write out to the sqlite database using scraperwiki library
scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})

# An arbitrary query against the database
scraperwiki.sql.select("* from data where 'name'='peter'")
