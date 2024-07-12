# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

"""
class Crowler01Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
"""
class Post(scrapy.Item):
    url = scrapy.Field()
    custamer = scrapy.Field()

