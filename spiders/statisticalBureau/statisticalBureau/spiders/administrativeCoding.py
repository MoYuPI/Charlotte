# -*- coding: utf-8 -*-
import scrapy
from ..items import AdministrativeCodingItem

class AdministrativecodingSpider(scrapy.Spider):
    name = 'administrativeCoding'
    allowed_domains = ['stats.gov.cn']
    start_urls = ['http://stats.gov.cn/']

    baseurl = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016'

    def start_requests(self):
        result_item = []
        url = AdministrativecodingSpider.baseurl+'/index.html'
        yield scrapy.Request(url=url, callback=self.parse)
        # url = "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/11.html"
        # yield scrapy.Request(url=url, callback=self.parse_city)

    def parse(self, response):
        coding = response.xpath('//tr[contains(@class, "provincetr")]')

        provinceItem = AdministrativeCodingItem()
        for province in coding:
            for td in province.xpath('td'):
                province_name = td.xpath('a/text()').extract()
                province_url = AdministrativecodingSpider.baseurl+'/%s' % td.xpath('a/@href').extract()[0]
                province_id = td.xpath('a/@href').extract()[0].split('.')[0]+"0000000000"
                request = scrapy.Request(url=province_url, callback=self.parse_city, meta={"id":province_id,"name":province_name,"url":province_url})

                provinceItem['pid'] = province_id
                provinceItem['coding'] = province_id
                provinceItem['level'] = 0
                provinceItem['name'] = province_name

                yield request

    def parse_city(self, response):
        province_name = response.meta['name']
        province_url = response.meta['url']
        province_id = response.meta['id']
        cities = response.xpath('//tr[contains(@class, "citytr")]')
        cityItem = AdministrativeCodingItem()
        for city in cities:
            coding = city.xpath('td')[0].xpath('a/text()').extract()[0].strip()
            name = city.xpath('td')[-1].xpath('a/text()').extract()[0].strip()
            city_url = AdministrativecodingSpider.baseurl + '/%s' % city.xpath('td')[1].xpath('a/@href').extract()[0].strip()
            request = scrapy.Request(url=city_url, callback=self.parse_county,meta={"id": coding, "url": city_url})

            cityItem['pid'] = province_id
            cityItem['coding'] = coding
            cityItem['level'] = 1
            cityItem['name'] = name

            yield cityItem
            yield request

    def parse_county(self, response):
        city_id = response.meta['id']
        city_url = response.meta['url']
        counties = response.xpath('//tr[contains(@class, "countytr")]')
        countyItem = AdministrativeCodingItem()
        for county in counties:
            coding = county.xpath('td')[0].xpath('a/text()').extract()[0].strip()
            name = county.xpath('td')[-1].xpath('a/text()').extract()[0].strip()
            county_url = AdministrativecodingSpider.baseurl +'/%s' % coding[:2]+ '/%s' % county.xpath('td')[1].xpath('a/@href').extract()[0].strip()
            request = scrapy.Request(url=county_url, callback=self.parse_town,meta={"id": coding, "url": county_url})

            countyItem['pid'] = city_id
            countyItem['coding'] = coding
            countyItem['level'] = 2
            countyItem['name'] = name

            yield countyItem
            yield request

    def parse_town(self, response):
        county_id = response.meta['id']
        county_url = response.meta['url']
        towns = response.xpath('//tr[contains(@class, "towntr")]')
        townItem = AdministrativeCodingItem()
        for town in towns:
            coding = town.xpath('td')[0].xpath('a/text()').extract()[0].strip()
            name = town.xpath('td')[-1].xpath('a/text()').extract()[0].strip()
            town_url = AdministrativecodingSpider.baseurl +'/%s' % coding[:2]+'/%s' % coding[2:4]+  '/%s' % town.xpath('td')[1].xpath('a/@href').extract()[0].strip()
            request = scrapy.Request(url=town_url, callback=self.parse_village,meta={"id": coding, "url": town_url})

            townItem['pid'] = county_id
            townItem['coding'] = coding
            townItem['level'] = 3
            townItem['name'] = name

            yield townItem
            yield request

    def parse_village(self, response):
        town_id = response.meta['id']
        town_url = response.meta['url']
        villages = response.xpath('//tr[contains(@class, "villagetr")]')
        villageItem = AdministrativeCodingItem()
        for village in villages:
            coding = village.xpath('td')[0].xpath('text()').extract()[0].strip()
            level = village.xpath('td')[1].xpath('text()').extract()[0].strip()
            name = village.xpath('td')[-1].xpath('text()').extract()[0].strip()
            villageItem['pid'] = town_id
            villageItem['coding'] = coding
            villageItem['level'] = 4
            villageItem['name'] = name
            villageItem['classification_code'] = level
            yield villageItem