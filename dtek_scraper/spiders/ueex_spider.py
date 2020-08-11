# # -*- coding: utf-8 -*-
# import scrapy
# from dtek_scraper.items import UkrEnergy
#
#
# class UbeSpider(scrapy.Spider):
#     name = 'UbeSpider'
#     allowed_domains = ['epbets.ueex.com.ua']
#     start_urls = ['https://epbets.ueex.com.ua/public/PositionList.aspx?id_auc=3294127&view_type=positions&lan=ua']
#
#     def parse(self, response):
#         item = UkrEnergy()
#         item['ukrenrgy'] = response.url
#         item['position'] = response.xpath("//div[@class='lan_r label']/div/text()").get()
#         item['direction'] = response.xpath("//div[@class='lan_r label']/div/text()").get()
#         item['state'] = response.xpath("//div[@class='lan_r label']/div/text()").get()
#         item['owner'] = response.xpath("//div[@class='label']/div/text()")
#         return item
#
#
#     ''' publicgoods = scrapy.Field()
#     transport = scrapy.Field()
#     publicLoadDate = scrapy.Field()
#     lot_quantity = scrapy.Field()
#     label = scrapy.Field()
#     inlabel = scrapy.Field()
#     fullsize = scrapy.Field()
#     initPrice = scrapy.Field()
#     pawnPrice = scrapy.Field() '''
#
