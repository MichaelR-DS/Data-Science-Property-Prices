from itemadapter import ItemAdapter
from scrapy import item


class HousePricesPipeline:
    def process_item(self, items, spider):
        return items
