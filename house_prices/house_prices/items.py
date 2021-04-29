import scrapy
import re
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


def clean_price(value):
    return value.replace('£', '').replace(' pcm', '')


def remove_spaces(value):
    return value.strip()


def get_type(value):
    return value.replace(' to rent', '').lower()


def get_postcode(value):
    postcode = value.split(', ')[-1].split(' ')[-1]
    return postcode


def get_areacode(value):
    areacode = re.split('(\d+)', get_postcode(value))[0]
    return areacode


def is_in_london(value):
    london_areas = ['EC', 'NW', 'SE', 'SW', 'WC', 'N', 'W', 'E']
    for area in london_areas:
        if area == get_areacode(value):
            in_london = True
            break
        else:
            in_london = False
    return in_london


def get_town(value):
    if is_in_london(value):
        return('London')
    else:
        if 'St' in value:
            town = value.split(', ')[-1].split(' ')[0:2]
            return(' '.join(town))
        elif 'St' not in value:
            town = value.split(', ')[-1].split(' ')[0]
            return(town)
        elif ['North', 'South', 'East', 'West', 'New'] in value:
            town = value.split(', ').split(' ')[0:2]
            return ' '.join(town)
        else:
            town = value.split(', ')[-1].split(' ')[0]
            return(town)



class HousePricesItem(scrapy.Item):
    price = scrapy.Field(input_processor=MapCompose(remove_tags, clean_price), output_processor=TakeFirst())
    living_rooms = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    bedrooms = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    bathrooms = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    town_city = scrapy.Field(input_processor=MapCompose(remove_tags, remove_spaces, get_town),
                             output_processor=TakeFirst())
    postcode = scrapy.Field(input_processor=MapCompose(remove_tags, remove_spaces, get_postcode),
                            output_processor=TakeFirst())
    property_type = scrapy.Field(input_processor=MapCompose(remove_tags, remove_spaces, get_type),
                                 output_processor=TakeFirst())
    desc = scrapy.Field(input_processor=MapCompose(remove_tags, remove_spaces), output_processor=TakeFirst())
