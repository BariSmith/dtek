# -*- coding: utf-8 -*-
import scrapy
# import response
from dtek_scraper.items import UkrEnergy


class UbeSpider(scrapy.Spider):
    name = 'UbeSpider'
    allowed_domains = ['epbets.ueex.com.ua']
    start_urls = ['https://epbets.ueex.com.ua/public/PositionList.aspx?id_auc=3294127&view_type=positions&lan=ua']
'''
    def parse(self, response):
        item = UkrEnergy()
        item['table'] = response.xpath("//div[@class='field']/div/text()").get()
        item['position'] = response.xpath("//div[@lan_id='position']/div/text()").get()
        item['direction'] = response.xpath("//div[@lan_id='Direction' ]/div/text()").get()
        item['state'] = response.xpath("//div[@lan_id='State' ]/div/text()").get()
        item['owner'] = response.xpath("//div[@id='l_OwnerName' ]/div/text()").get()
        return item

'''


    def parse(self, response):
        item = UkrEnergy()
        position = response.css(".pnList.position.field.lan_id='position']/div/text()").extract()
        # item['direction'] = response.xpath("//div[@lan_id='Direction' ]/div/text()").get()
        # item['state'] = response.xpath("//div[@lan_id='State' ]/div/text()").get()
        # item['owner'] = response.xpath("//div[@id='l_OwnerName' ]/div/text()").get()
        # return item

        for item in zip(position):
            # create a dictionary to store the scraped info
            scraped_info = {
                'position': item[0],
                # 'vote': item[1],
                # 'created_at': item[2],
                # 'comments': item[3],
            }

            # yield or give the scraped info to scrapy
            yield scraped_info


    ''' publicgoods = scrapy.Field()
    transport = scrapy.Field()
    publicLoadDate = scrapy.Field()
    lot_quantity = scrapy.Field()
    label = scrapy.Field()
    inlabel = scrapy.Field()
    fullsize = scrapy.Field()
    initPrice = scrapy.Field()
    pawnPrice = scrapy.Field() '''

