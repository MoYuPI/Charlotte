from django.db import models

# Create your models here.
from django.db import models

class NewHouse(models.Model):
    name = models.CharField("项目名称", max_length=255)
    supervision_bank = models.CharField("资金监管银行", max_length=255)
    supervision_acount = models.CharField("监管帐号", max_length=255)
    project_state = models.CharField("项目状态", max_length=255)
    address = models.CharField("项目地址", max_length=255)
    dev_company = models.CharField("开发公司", max_length=255)
    license_authority = models.CharField("发证机关", max_length=255)
    sale_permit = models.CharField("预(现)售证名称", max_length=255)
    license_key = models.CharField("预(现)售许可证号", max_length=255)
    online_saleable_area = models.DecimalField("纳入网上可售面积", max_digits=10, decimal_places=2)
    online_saleable_flats = models.DecimalField("纳入网上可售套数", max_digits=10, decimal_places=2)
    saleable_area = models.DecimalField("当前可售面积", max_digits=10, decimal_places=2)
    saleable_flats = models.DecimalField("当前可售套数", max_digits=10, decimal_places=2)
    sold_area = models.DecimalField("已售面积", max_digits=10, decimal_places=2)
    sold_flats = models.DecimalField("已售套数", max_digits=10, decimal_places=2)
    residential_area = models.DecimalField("当前(住宅)可售面积", max_digits=10, decimal_places=2)
    residential_flats = models.DecimalField("当前(住宅)可售套数", max_digits=10, decimal_places=2)
    sold_residential_area = models.DecimalField("已售(住宅)面积", max_digits=10, decimal_places=2)
    sold_residential_flats = models.DecimalField("已售(住宅)套数", max_digits=10, decimal_places=2)
    reserve_area = models.DecimalField("预定面积", max_digits=10, decimal_places=2)
    reserve_flats = models.DecimalField("预定套数", max_digits=10, decimal_places=2)
    saleable_parking_amount = models.DecimalField("车位可售套数", max_digits=10, decimal_places=2)
    saleable_garage_amount = models.DecimalField("车库可售套数", max_digits=10, decimal_places=2)
    sold_avg_price = models.DecimalField("已售(住宅)平均价", max_digits=10, decimal_places=2)
    districts = models.CharField("所在区县", max_length=255)
    contact_phone = models.CharField("售楼电话", max_length=255)
    remark = models.CharField("备注", max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        managed = True
        ordering = ('created',)
        db_table = 'new_house'