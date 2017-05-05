from django.db import models

# Create your models here.

class NewHouse(models.Model):
    name = models.CharField("项目名称", max_length=255)
    supervision_bank = models.CharField("资金监管银行", max_length=255)
    supervision_acount = models.CharField("监管帐号", max_length=255)
    project_state =models.CharField("项目状态", max_length=255)
    address = models.CharField("项目地址", max_length=255)
    dev_company = models.CharField("开发公司", max_length=255)
    license_authority = models.CharField("发证机关", max_length=255)
    sale_permit = models.CharField("预(现)售证名称", max_length=255)
    license_key = models.CharField("预(现)售许可证号", max_length=255)
    online_saleable_area = models.FloatField("纳入网上可售面积", decimal_places=2)
    online_saleable_flats = models.FloatField("纳入网上可售套数", decimal_places=2)
    saleable_area = models.FloatField("当前可售面积",decimal_places=2)
    saleable_flats = models.FloatField("当前可售套数",decimal_places=2)
    sold_area = models.FloatField("已售面积",decimal_places=2)
    sold_flats = models.CharField("已售套数",max_length=255)
    residential_area = models.CharField("当前(住宅)可售面积",max_length=255)
    residential_flats = models.CharField("当前(住宅)可售套数",max_length=255)
    sold_residential_area = models.CharField("已售(住宅)面积",max_length=255)
    sold_residential_flats = models.CharField("已售(住宅)套数",max_length=255)
    reserve_area = models.CharField("预定面积",max_length=255)
    reserve_flats = models.CharField("预定套数",max_length=255)
    saleable_parking_amount = models.CharField("车位可售套数",max_length=255)
    saleable_garage_amount = models.CharField("车库可售套数",max_length=255)
    sold_avg_price = models.CharField("已售(住宅)平均价",max_length=255)
    districts = models.CharField("所在区县",max_length=255)
    contact_phone = models.CharField("售楼电话",max_length=255)
    remark = models.CharField("备注",max_length=255)

    class Meta:
        managed = True
        db_table = 'new_house'
