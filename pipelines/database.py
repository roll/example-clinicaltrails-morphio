import scraperwiki


class Database(object):

    # Public

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        scraperwiki.sqlite.save(
            unique_keys=['nct_id'],
            data=item)
        return item
