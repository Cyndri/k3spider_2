# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class K3SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    店铺名称 = scrapy.Field()
    官方网址 = scrapy.Field()
    电话 = scrapy.Field()
    QQ号码 = scrapy.Field()
    拿货地址 = scrapy.Field()
