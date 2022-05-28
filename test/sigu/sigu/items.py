# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SiguItem(scrapy.Item):

    label = scrapy.Field()
    text = scrapy.Field()
