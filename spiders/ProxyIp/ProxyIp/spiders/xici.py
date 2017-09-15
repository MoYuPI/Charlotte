# -*- coding: utf-8 -*-
import scrapy
from ..items import ProxyipDjangoItem

class XiciSpider(scrapy.Spider):
    name = 'xici'
    allowed_domains = ['xicidaili.com']
    start_urls = ['http://www.xicidaili.com/nn/{0}']

    headers = {
        "HOST": "www.xicidaili.com",
        "Referer": "http://www.xicidaili.com/",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"
    }

    def start_requests(self):
        urls = []
        page = 50
        for i in range(1,page):
            urls.append("http://www.xicidaili.com/nn/{0}".format(i))
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        all_trs = response.selector.css("#ip_list tr")
        ip_list=[]
        for tr in all_trs[1:]:
            item = ProxyipDjangoItem()
            speed_str = tr.css(".bar::attr(title)").extract()[0]
            if speed_str:
                speed = float(speed_str.split("秒")[0])
            all_texts = tr.css("td::text").extract()

            ip = all_texts[0]
            port = all_texts[1]
            proxy_type = all_texts[5]

            item['ip'] = ip
            item['port'] = port
            item['speed'] = speed
            item['proxy_type'] = proxy_type

            yield item