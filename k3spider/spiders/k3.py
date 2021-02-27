import scrapy

from ..items import K3SpiderItem


class K3Spider(scrapy.Spider):
    name = 'k3'
    allowed_domains = ['k3.cn']
    start_urls = ['http://www.k3.cn/supplier/0,,0,newbie,1,2,.html']

    def parse(self, response):
        item = K3SpiderItem()
        for li in response.xpath("//ul[@class='seller_list']/li/div[@class='list_con']"):
            item['店铺名称'] = li.xpath('./div[@class="name"]/a/text()').extract()
            item['官方网址'] = li.xpath('./div[@class="url"][1]/a/text()').extract()
            item['电话'] = li.xpath(
                './div[@class="text"][1]/span/input/@value').extract()
            item['QQ号码'] = li.xpath('./div[@class="text"][1]/span[2]/text()').extract()
            item['拿货地址'] = li.xpath('./div[@class="text"][2]/text()').extract()
            yield item
        next_url = response.xpath('//span[@class="next"]/a/@href').extract_first()
        if next_url:
            next_url = "http://www.k3.cn" + next_url
            yield scrapy.Request(next_url, callback=self.parse)
