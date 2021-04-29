import scrapy
from ..items import HousePricesItem
from scrapy.loader import ItemLoader

class HouseSpider(scrapy.Spider):
    name = 'houses'

    start_urls = ["https://www.primelocation.com/to-rent/property/england/?page_size=20&pn=1&view_type=list"]
    page_number = 1

    def parse(self, response):
        for val in response.xpath("//div[@class='listing-results-right clearfix']"):
            loader = ItemLoader(item=HousePricesItem(), selector=val)

            loader.add_xpath('price', "normalize-space(.//a[@class='listing-price']/text())")
            loader.add_xpath('living_rooms', ".//span[@class='num-icon num-reception']/text()")
            loader.add_xpath('bedrooms', ".//span[@class='num-icon num-beds']/text()")
            loader.add_xpath('bathrooms', ".//span[@class='num-icon num-baths']/text()")
            loader.add_xpath('town_city', ".//a/div[@class='listing-results-sections listing-description']/span/text()")
            loader.add_xpath('postcode', ".//a/div[@class='listing-results-sections listing-description']/span/text()")
            loader.add_xpath('property_type', "normalize-space(.//h2[@class='listing-results-attr']/text())")
            loader.add_xpath('desc', "normalize-space(.//a/div[@class='listing-results-sections listing-description']/p/text())")

            yield loader.load_item()

            next_page = "https://www.primelocation.com/to-rent/property/england/?identifier=england&page_size=20&q=England&radius=0&view_type=list&pn={}".format(str(HouseSpider.page_number))

            if HouseSpider.page_number <= 500:
                HouseSpider.page_number += 1
                yield response.follow(next_page, callback = self.parse)