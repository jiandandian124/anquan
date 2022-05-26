# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnquanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #id = scrapy.Field()
    title = scrapy.Field()
    text = scrapy.Field()
    tags = scrapy.Field()
    concern = scrapy.Field()
    url = scrapy.Field()