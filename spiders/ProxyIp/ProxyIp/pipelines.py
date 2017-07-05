# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from spiders.models import ProxyIp
from spiders.tools.proxyip import GetIP

class ProxyipPipeline(object):
    def process_item(self, item, spider):
        get_ip = GetIP()
        if not ProxyIp.objects.filter(ip = item['ip'], port = item['port']):
            # if get_ip.validate(item['ip'],item['port']):
            #     print('save {0}'.format(item['ip']))
            item.save()