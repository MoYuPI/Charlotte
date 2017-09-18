# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# from spiders.models import AdministrativeCoding

class StatisticalbureauPipeline(object):
    def process_item(self, item, spider):
        item.save()
        return item
