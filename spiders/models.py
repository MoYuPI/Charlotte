from django.db import models

# Create your models here.
from django.db import models

class Demo_data(models.Model):
    iAutoId = models.AutoField(primary_key=True, default=None)
    title = models.CharField(max_length=256, default=None)