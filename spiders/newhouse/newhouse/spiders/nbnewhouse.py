# -*- coding: utf-8 -*-
import scrapy
import re
from decimal import *
from scrapy.http.request import Request
from ..items import NewHouseItem,NewHouseDjangoItem

class NbnewhouseSpider(scrapy.Spider):
    name = "nbnewhouse"
    allowed_domains = ["cnnbfdc.com"]
    start_urls = ['http://cnnbfdc.com/']
    baseurl = 'http://newhouse.cnnbfdc.com'

    headers = {
        "HOST": "cnnbfdc.com/",
        "Referer": "http://cnnbfdc.com/",
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
    }

    def start_requests(self):
        urls = []
        page = 90
        for i in range(1,page):
            urls.append(NbnewhouseSpider.baseurl+'/lpxx.aspx?p=%s'%i)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        houses = response.xpath('//body/table[6]/tr/td[1]/table/tr[2]/td/table/tr')
        for i in range(1, len(houses)-1):
            house = houses[i]
            href = NbnewhouseSpider.baseurl+'/'+house.xpath('td')[1].xpath('a/@href').extract()[0].strip()
            name = house.xpath('td')[1].xpath('a/text()').extract()[0].strip()
            area = house.xpath('td')[2].xpath('span/text()').extract()[0].strip()
            address = house.xpath('td')[3].xpath('text()').extract()[0].strip()

            request = Request(url=href,callback=self.parse_detail)
            yield request

    def parse_detail(self, response):
        pattern = re.compile(r'\d+(?:\.\d+)?')
        newHouseItem = NewHouseDjangoItem()
        items = response.xpath('//table')[15].xpath('tr/td')
        newHouseItem['supervision_bank'] = items[1].xpath('text()').extract()[-1].strip()
        newHouseItem['supervision_acount']= items[3].xpath('text()').extract()[-1].strip()
        newHouseItem['name'] = items[5].xpath('span/text()').extract()[0].strip()
        newHouseItem['project_state'] = items[7].xpath('span/text()').extract()[0].strip()
        newHouseItem['address'] = items[9].xpath('text()').extract()[-1].strip()
        newHouseItem['dev_company'] = items[11].xpath('text()').extract()[-1].strip()
        newHouseItem['license_authority'] = items[13].xpath('text()').extract()[-1].strip()
        newHouseItem['sale_permit'] = items[15].xpath('text()').extract()[-1].strip()
        newHouseItem['license_key'] = pattern.findall(items[17].xpath('text()').extract()[-1].strip())[0]
        newHouseItem['online_saleable_area'] = Decimal(pattern.findall(items[19].xpath('text()').extract()[-1])[0])
        newHouseItem['online_saleable_flats'] = Decimal(pattern.findall(items[21].xpath('text()').extract()[-1])[0])
        newHouseItem['saleable_area'] = Decimal(pattern.findall(items[23].xpath('text()').extract()[-1])[0])
        newHouseItem['saleable_flats'] = Decimal(pattern.findall(items[25].xpath('text()').extract()[-1])[0])
        newHouseItem['sold_area'] = Decimal(pattern.findall(items[27].xpath('text()').extract()[-1])[0])
        newHouseItem['sold_flats'] = Decimal(pattern.findall(items[29].xpath('text()').extract()[-1])[0])
        newHouseItem['residential_area'] = Decimal(pattern.findall(items[31].xpath('text()').extract()[-1])[0])
        newHouseItem['residential_flats'] = Decimal(pattern.findall(items[33].xpath('text()').extract()[-1])[0])
        newHouseItem['sold_residential_area'] = Decimal(pattern.findall(items[35].xpath('text()').extract()[-1])[0])
        newHouseItem['sold_residential_flats'] = Decimal(pattern.findall(items[37].xpath('text()').extract()[-1])[0])
        newHouseItem['reserve_area'] = Decimal(pattern.findall(items[39].xpath('text()').extract()[-1])[0])
        newHouseItem['reserve_flats'] = Decimal(pattern.findall(items[41].xpath('text()').extract()[-1])[0])
        newHouseItem['saleable_parking_amount'] = Decimal(pattern.findall(items[43].xpath('text()').extract()[-1])[0])
        newHouseItem['saleable_garage_amount'] = Decimal(pattern.findall(items[45].xpath('text()').extract()[-1])[0])
        # newHouseItem['sold_avg_price'] = Decimal(pattern.findall(items[47].xpath('text()').extract()[-1].strip())[0])
        newHouseItem['sold_avg_price'] = 0
        newHouseItem['districts'] = items[47].xpath('text()').extract()[-1].strip()
        newHouseItem['contact_phone'] = items[49].xpath('text()').extract()[-1].strip()
        newHouseItem['high_price'] = Decimal(pattern.findall(items[51].xpath('text()').extract()[-1].strip())[0])
        newHouseItem['low_price'] = Decimal(pattern.findall(items[53].xpath('text()').extract()[-1].strip())[0])
        newHouseItem['remark'] = items[55].xpath('text()').extract()[-1].strip()
        return newHouseItem
        # print(items[15].xpath('text()').extract()[-1].strip())
        # print(items[17].xpath('text()').extract()[-1].strip())
        # print(pattern.findall(items[19].xpath('text()').extract()[-1].strip())[0])
        # print(pattern.findall(items[21].xpath('text()').extract()[-1])[0])
        # print(pattern.findall(items[23].xpath('text()').extract()[-1])[0])
        # print(pattern.findall(items[25].xpath('text()').extract()[-1])[0])
        # print(pattern.findall(items[27].xpath('text()').extract()[-1])[0])
        # print(pattern.findall(items[29].xpath('text()').extract()[-1])[0])
        # print(pattern.findall(items[31].xpath('text()').extract()[-1])[0])
        # print(pattern.findall(items[33].xpath('text()').extract()[-1])[0])
        # print(pattern.findall(items[35].xpath('text()').extract()[-1])[0])
        # print(pattern.findall(items[37].xpath('text()').extract()[-1])[0])
        # print(pattern.findall(items[39].xpath('text()').extract()[-1])[0])
        # print(pattern.findall(items[41].xpath('text()').extract()[-1])[0])
        # print(pattern.findall(items[43].xpath('text()').extract()[-1])[0])
        # print(pattern.findall(items[45].xpath('text()').extract()[-1])[0])
        # print(pattern.findall(items[47].xpath('text()').extract()[-1])[0])
        # print(items[49].xpath('text()').extract()[-1].strip())
        # print(items[51].xpath('text()').extract()[-1].strip())
        # print(items[53].xpath('text()').extract()[-1].strip())
        # for index, item in enumerate(response.xpath('//table')[15].xpath('tr/td')):
        #     # 0
        #     info = []
        #     info.append(item.xpath('text()').extract()[1].strip()) if index % 2 == 0 else info.append(
        #         item.xpath('text()').extract()[0].strip())
        #     print(info)