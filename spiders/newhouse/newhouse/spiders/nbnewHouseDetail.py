# -*- coding: utf-8 -*-
import scrapy
import re

class NbnewhouseDetailSpider(scrapy.Spider):
    name = "nbnewhousedetail"
    allowed_domains = ["cnnbfdc.com"]
    start_urls = ['http://cnnbfdc.com/']

    def start_requests(self):
        urls = [
            'http://newhouse.cnnbfdc.com/lpxxshow.aspx?projectid=14761'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        pattern = re.compile(r'\d+(?:\.\d+)?')
        items = response.xpath('//table')[15].xpath('tr/td')
        print(items[1].xpath('text()').extract()[-1].strip())
        print(items[3].xpath('text()').extract()[-1].strip())
        print(items[5].xpath('span/text()').extract()[0].strip())
        print(items[7].xpath('span/text()').extract()[0].strip())
        print(items[9].xpath('text()').extract()[-1].strip())
        print(items[11].xpath('text()').extract()[-1].strip())
        print(items[13].xpath('text()').extract()[-1].strip())
        print(items[15].xpath('text()').extract()[-1].strip())
        print(items[17].xpath('text()').extract()[-1].strip())
        print(pattern.findall(items[19].xpath('text()').extract()[-1].strip())[0])
        print(pattern.findall(items[21].xpath('text()').extract()[-1])[0])
        print(pattern.findall(items[23].xpath('text()').extract()[-1])[0])
        print(pattern.findall(items[25].xpath('text()').extract()[-1])[0])
        print(pattern.findall(items[27].xpath('text()').extract()[-1])[0])
        print(pattern.findall(items[29].xpath('text()').extract()[-1])[0])
        print(pattern.findall(items[31].xpath('text()').extract()[-1])[0])
        print(pattern.findall(items[33].xpath('text()').extract()[-1])[0])
        print(pattern.findall(items[35].xpath('text()').extract()[-1])[0])
        print(pattern.findall(items[37].xpath('text()').extract()[-1])[0])
        print(pattern.findall(items[39].xpath('text()').extract()[-1])[0])
        print(pattern.findall(items[41].xpath('text()').extract()[-1])[0])
        print(pattern.findall(items[43].xpath('text()').extract()[-1])[0])
        print(pattern.findall(items[45].xpath('text()').extract()[-1])[0])
        print(pattern.findall(items[47].xpath('text()').extract()[-1])[0])
        print(items[49].xpath('text()').extract()[-1].strip())
        print(items[51].xpath('text()').extract()[-1].strip())
        print(items[53].xpath('text()').extract()[-1].strip())

        # print(response.xpath('//table')[15].xpath('tr/td')[21].xpath('text()').extract()[-1])
        #
        # for index,item  in enumerate(response.xpath('//table')[15].xpath('tr/td')):
        #     # 0
        #     info = []
        #     info.append(item.xpath('text()').extract()[1].strip()) if index % 2 == 0 else info.append(item.xpath('text()').extract()[-1].strip())
        #     print(info)
