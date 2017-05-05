# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from newhouse.models import NewHouse

class NewHouseDjangoItem(DjangoItem):
    # define the fields for your item here like:
    # name = scrapy.Field()
    django_model = NewHouse

class NewHouseItem(scrapy.Item):
    project_name = scrapy.Field()
    address = scrapy.Field()

    capital_supervision_bank = scrapy.Field()
    capital_supervision_acount = scrapy.Field()
    project_state = scrapy.Field()
    dev_company = scrapy.Field()
    licence_authority = scrapy.Field()
    sale_permit = scrapy.Field()
    license_key = scrapy.Field()
    online_saleable_area = scrapy.Field()
    online_saleable_flats = scrapy.Field()
    saleable_area = scrapy.Field()
    saleable_flats = scrapy.Field()

    sold_area = scrapy.Field()
    sold_flats = scrapy.Field()

    residential_area = scrapy.Field()
    residential_flats = scrapy.Field()
    sold_residential_area = scrapy.Field()
    sold_residential_flats = scrapy.Field()
    reserve_area = scrapy.Field()
    reserve_flats = scrapy.Field()

    saleable_parking_amount = scrapy.Field()
    saleable_garage_amount = scrapy.Field()
    sold_avg_price = scrapy.Field()
    districts = scrapy.Field()
    contact_phone = scrapy.Field()
    remark = scrapy.Field()
