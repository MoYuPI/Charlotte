# -*- coding: utf-8 -*-
import scrapy
import re
from decimal import *
from scrapy.http.request import Request
from ..items import NewHouseDjangoItem

class NbnewhouseSpider(scrapy.Spider):
    name = "nbnewhouse"
    allowed_domains = ["cnnbfdc.com"]
    start_urls = ['http://cnnbfdc.com/']
    base_url = 'http://newhouse.cnnbfdc.com'

    headers = {
        "HOST": "cnnbfdc.com/",
        "Referer": "http://cnnbfdc.com/",
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
    }

    def start_requests(self):
        urls = []
        page = 6
        for i in range(page):
            urls.append(NbnewhouseSpider.base_url + '/projects?page=%s' % i)
        urls = [
            'https://newhouse.cnnbfdc.com/projects'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        # yield scrapy.Request(url='https://newhouse.cnnbfdc.com/project/18058', callback=self.parse_detail)

    def parse(self, response):
        projects = response.xpath("//div[@class='group-right']")
        for item in projects:
            # tutorialItem = TutorialItem()
            # tutorialItem['name'] = item.xpath("div/a/text()").extract()[0].strip()
            # tutorialItem['href'] = item.xpath('div/a/@href').extract()[0].strip()
            # tutorialItem['lic'] = item.xpath("div[2]/text()").extract()[0].strip()
            # tutorialItem['address'] = item.xpath("div[3]/div/div[1]/span/text()").extract()[0].strip()
            # tutorialItem['developer'] = item.xpath("div[3]/div/div[2]/span/text()").extract()[0].strip()
            # tutorialItem['type'] = item.xpath("div")[-1].xpath('text()').extract()
            href = '{}/{}'.format(NbnewhouseSpider.base_url, item.xpath('div/a/@href').extract()[0].strip())
            request = Request(url=href, callback=self.parse_data_stats)
            yield request

    def parse_data_stats(self, response):
        pattern = re.compile(r'\d+(?:\.\d+)?')
        newHouseItem = NewHouseDjangoItem()
        data_stats = response.xpath("//div[@id='all-data']").xpath('div/div/div/div/div')
        newHouseItem['name'] = response.xpath("//div[@class='project-detail__name']/h1/text()").extract()[0].strip()
        newHouseItem['reserve_area'] = pattern.findall(data_stats[0].xpath('div/div')[0].xpath('div/text()').extract()[-1].strip())[0]
        newHouseItem['sold_area'] = pattern.findall(data_stats[0].xpath('div/div')[1].xpath('div/text()').extract()[-1].strip())[0]
        newHouseItem['sold_residential_area'] = pattern.findall(data_stats[0].xpath('div/div')[3].xpath('div/text()').extract()[-1].strip())[0]
        newHouseItem['saleable_area'] = pattern.findall(data_stats[0].xpath('div/div')[4].xpath('div/text()').extract()[-1].strip())[0]
        newHouseItem['residential_area'] = pattern.findall(data_stats[0].xpath('div/div')[5].xpath('div/text()').extract()[-1].strip())[0]
        newHouseItem['online_saleable_area'] = pattern.findall(data_stats[0].xpath('div/div')[0].xpath('div/text()').extract()[-1].strip())[0]

        newHouseItem['online_saleable_flats'] = pattern.findall(data_stats[1].xpath('div/div')[0].xpath('div/text()').extract()[-1].strip())[0]
        newHouseItem['reserve_flats'] = pattern.findall(data_stats[1].xpath('div/div')[0].xpath('div/text()').extract()[-1].strip())[0]
        newHouseItem['sold_flats'] = pattern.findall(data_stats[1].xpath('div/div')[1].xpath('div/text()').extract()[-1].strip())[0]
        newHouseItem['sold_residential_flats'] = pattern.findall(data_stats[1].xpath('div/div')[3].xpath('div/text()').extract()[-1].strip())[0]
        newHouseItem['saleable_flats'] = pattern.findall(data_stats[1].xpath('div/div')[4].xpath('div/text()').extract()[-1].strip())[0]
        newHouseItem['residential_flats'] = pattern.findall(data_stats[1].xpath('div/div')[5].xpath('div/text()').extract()[-1].strip())[0]
        # todo
        # other attributes
        yield newHouseItem

    def parse_room_types(self, response):
        # todo
        pass

    def parse_building_list(self, response):
        # todo
        pass