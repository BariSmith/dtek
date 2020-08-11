# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UkrEnergy(scrapy.Item):
    ukrenergy = scrapy.Field()
    table = scrapy.Field()
    position = scrapy.Field()
    direction = scrapy.Field()
    state = scrapy.Field()
    owner = scrapy.Field()
    publicgoods = scrapy.Field()
    transport = scrapy.Field()
    publicLoadDate= scrapy.Field()
    lot_quantity = scrapy.Field()
    label = scrapy.Field()
    inlabel = scrapy.Field()
    fullsize = scrapy.Field()
    initPrice = scrapy.Field()
    pawnPrice = scrapy.Field()
