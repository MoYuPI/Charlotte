# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from spiders.models import NewHouse
class CralwerPipeline(object):
    def process_item(self, item, spider):
        print(item)
        try:
            new_house = NewHouse.objects.get(name=item['name'])
            new_house.update(item.values())
        except NewHouse.DoesNotExist:
            item.save()